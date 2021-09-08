# @author Cody
# @date 2021.09.07
# experimenting with sprites! from Hajileee's Fantasy Characters Pack
#     https://hajileee.itch.io/hajileees-fantasy-characters-pack
#     https://www.youtube.com/watch?v=xFEKIWpd0sU
#
# . version comments
# . shell with setup, background
# . create Viking class with particle code including apply_force
# . idle animation: loadImage, spritesheet.get
# . idle animation: Viking.index, .frames, %
# keyboard input: A, D with run animation
# mirroring for moving left and right
# methods to create the other 5 animations stored in Viking class
# looping vs not looping animations
# gravity and jumping
# ...
# double jump
# particle effects
# collision detection
# projectile weapon with emitter
# coffee mug stuck onto shield that spills whenever the shield faces down
# cap level with max height

from Viking import *

def setup():
    global victor
    imageMode(CENTER)
    colorMode(HSB, 360, 100, 100, 100)
    spritesheet = loadImage("viking.png")
    size(700, 300)
    victor = Viking(spritesheet, width/2, height/2, 0.1)
    

def draw():
    global victor
    background(0)
    fill(50, 45, 97)
    rect(-60, 260, 820, 300)
    victor.animate()
    if victor.pos.y < height/2:
        victor.pos.y = height/2
    victor.update()
    victor.show()
    
    
def keyPressed():
    global victor
    if key == 'a':
        victor.vel = PVector(-4, 0)
        victor.set_animation(victor.run, True)
        victor.facing_left = True
    if key == 'd':
        victor.vel = PVector(4, 0)
        victor.set_animation(victor.run, True)
        victor.facing_left = False
    if key == ' ':
        victor.vel = PVector(0, 0)
        victor.set_animation(victor.jump, False)
        
def keyReleased():
    global victor
    if key == 'a' or key == 'd':
        victor.vel = PVector(0, 0)
        victor.set_animation(victor.idle, True)
    
    
