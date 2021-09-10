

class Viking:
    def __init__(self, spritesheet, x, y, animation_speed):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.spritesheet = loadImage("viking.png")
        self.target_size = PVector(216, 216)
        self.index = 0
        self.facing_left = False
        self.loop = True
        self.speed = animation_speed
        self.max_speed = 8
        
        # animations:
        self.idle = self.select(0, 7)
        self.run = self.select(1, 6)
        self.jump = self.select(2, 5)
        self.attack = self.select(3, 9)
        self.shield = self.select(4, 9)
        self.die = self.select(5, 9)
        self.frames = len(self.idle)
        
        self.set_animation(self.idle, loop=True)
        self.finished = False # have we gotten to the last frame?
        
        
    # sets the position; setter method for position
    def set_pos(self, pos):
        self.pos = pos
        
    
    # wraps the edges
    def edges(self):
        if self.pos.x < 0:
            self.pos.x = width - self.target_size.x/2
        if self.pos.x + self.target_size.x/2 > width:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = height - self.target_size.y/2
        if self.pos.y + self.target_size.y/2 > height:
            self.pos.y = 0
                
                
    def select(self, row, columns, w=32, h=32):
        animation = []
        for i in range(columns):
            animation.append(self.spritesheet.get(i*w, row*h, w, h))
            
        return animation
    
    
    def set_animation(self, animation, loop):
        # people can't jump in the air.
        if animation != self.jump or self.is_not_in_the_air():
            self.animation = animation
            self.loop = loop
            # how do we know how many frames there are? If we don't, then we
            # will get an IndexError in Show.
            self.frames = len(self.animation)
            if self.animation != self.run:
                self.index = 0
            
    
    
    # How do we apply a force?
    def apply_force(self, force):
        # F = ma, so a = F/m, but m = 1, so a = F. 
        self.acc.add(force)
        
    
    # how do we update our index?
    def animate(self):
        # if we can loop, we are fine; we don't have any constraints.
        if self.loop:
            self.index += self.speed
            self.finished = False
        # Otherwise, we can't loop and only if we aren't finished, we should
        # update our speed.
        else:
            if not self.finished:
                self.index += self.speed
            else:
                # If we finish dieing, then we don't want to go to idle!
                # This also applies for shielding.
                if self.animation == self.die or self.animation == self.shield:
                    pass
                # Otherwise, we should go back to idle. We don't want to 
                # stay at the last frame.
                else:
                    self.set_animation(self.idle, True)
                    self.finished = False
        
        
    # returns if we're in the air or not    
    def is_not_in_the_air(self):
         return self.pos.y == height/2
    
    
    # updates the position, velocity, and acceleration
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        # what happens if we're going too fast? maybe I should add to the
        # spritesheet and name it fall-over
        if self.vel.mag() > self.max_speed:
            self.vel.setMag(self.max_speed)
        self.pos.y = constrain(self.pos.y, 0, height/2)
        self.acc = PVector(0, 0)
      
          
    # shows the victor
    def show(self):
        # in order to get what frame of the animation, we need to get the index.
        index = floor(self.index) % self.frames
        # If we have exceeded the amount of frames that we have, we should set
        # our finished variable to True, because that's what our finished 
        # variable keeps track of.
        if index == self.frames - 1:
            self.finished = True
        picture = self.animation[index]
        picture.resize(216, 216)
        if not self.facing_left:
            # If we're facing right, we don't need to do anything with the
            # picture as explained below.
            image(picture, self.pos.x, self.pos.y)
        else:
            # Oh no! We're facing left, and our spritesheet only accounts
            # for us facing right.
            pushMatrix()
            translate(self.pos.x, self.pos.y)
            scale(-1, 1)
            image(picture, 0, 0)
            popMatrix()
    
