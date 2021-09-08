

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
        
        # animations:
        self.idle = self.select(0, 7)
        self.run = self.select(1, 6)
        self.jump = self.select(2, 5)
        self.attack = self.select(3, 9)
        self.shield = self.select(4, 9)
        self.die = self.select(5, 9)
        
        
        self.set_animation(self.idle, loop=True)
        self.finished = False # have we gotten to the last frame?
                
                
    def select(self, row, columns, w=32, h=32):
        animation = []
        for i in range(columns):
            animation.append(self.spritesheet.get(i*w, row*h, w, h))
            
        return animation
    
    
    def set_animation(self, animation, loop):
        self.animation = animation
        self.loop = loop
        # how do we know how many frames there are? If we don't, then we
        # will get an IndexError in Show.
        self.frames = len(self.animation)
    
    
    # How do we apply a force?
    def apply_force(self, force):
        # F = ma, so a = F/m, but m = 1, so a = F. 
        self.acc.add(force)
        
    
    def animate(self):
        self.index += self.speed
            
        
    
    
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc = PVector(0, 0)
        
        
    def show(self):
        # in order to get what frame of the animation, we need to get the index.
        index = floor(self.index) % self.frames
        if index > self.frames:
            self.finished = True
        picture = self.animation[index]
        picture.resize(216, 216)
        if not self.facing_left:
            image(picture, self.pos.x, self.pos.y)
        else:
            pushMatrix()
            translate(self.pos.x, self.pos.y)
            scale(-1, 1)
            image(picture, 0, 0)
            popMatrix()
    
