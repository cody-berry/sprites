# @author Cody
# @date 2021.09.07
# experimenting with sprites! from Hajileee's Fantasy Characters Pack
#     https://hajileee.itch.io/hajileees-fantasy-characters-pack
#     https://www.youtube.com/watch?v=xFEKIWpd0sU
#
# . version comments
# . shell with setup, background
# . create Viking class with particle code including apply_force
# idle animation: loadImage, spritesheet.get
# idle animation: Viking.index, .frames, %
# keyboard input: A, D
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
    victor = Viking(spritesheet, width/2, 64, 0.1)
    

def draw():
    global victor
    background(0)
    gravity = PVector(0, 0.1)
    victor.apply_force(gravity)
    victor.update()
    victor.show()
    
    
    
    
    