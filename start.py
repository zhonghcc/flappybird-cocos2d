#coding=utf8
import sys
import os

from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.actions import JumpBy, Lens3D, Reverse
from layers.BackgoundLayer import *
from layers.PipeLayer import *
from layers.PlayerLayer import *

def main(argv=None):
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)
    
    print sys.argv
    
    init()
    
def init():
    
    width,height = CONFIG['originsize']
    director.init(width=width,height=height,resizable=False)


    layer_bg_day = BackgroundLayer('bg_day',0.5)
    layer_land = BackgroundLayer('land')
    layer_pipe = PipeLayer()
    layer_bird = PlayerLayer()
    scene1_layers = [layer_bg_day,layer_pipe,layer_land,layer_bird]
    scene = Scene(*scene1_layers)
    #scene.add(bg_day_layer)
    # Run!
    director.run(scene) 

if __name__ == "__main__":
    sys.exit(main())