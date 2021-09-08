

class Viking:
    def __init__(self, spritesheet, x, y, animation_speed):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.spritesheet = loadImage("viking.png")
        self.idle = self.spritesheet.get(0, 0, 32, 32) 
        self.idle.resize(216, 216)
    
    
    
    # How do we apply a force?
    def apply_force(self, force):
        # F = ma, so a = F/m, but m = 1, so a = F. 
        self.acc.add(force)
        
        
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc = PVector(0, 0)
        
        
    def show(self):
        image(self.idle, self.pos.x, self.pos.y)
    
