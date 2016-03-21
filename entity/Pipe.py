#coding=utf8
'''
Created on 2016年3月21日

@author: zhonghcc
'''
import pyglet
import threading
from cocos.layer import Layer

from config import CONFIG,ASSETS

class Pipe(object):
    '''
    classdocs
    '''


    def __init__(self,is_up,pos_x,pos_y):
        # always call super()
        

        # load the image form file
        self.image_x = 52
        self.image_y = 320
        self.image = None
        self.is_up = is_up
        if is_up:
            self.image = pyglet.resource.image(CONFIG['assetspath']+'pipe_up.png')
        else:
            self.image = pyglet.resource.image(CONFIG['assetspath']+'pipe_down.png')
        
        space = CONFIG['space']
        self.pos_x=pos_x
        if is_up:
            self.pos_y=-self.image_y+pos_y- space/2
        else:
            self.pos_y=pos_y+space/2
#         print self.pos_y

    def update(self,dt):
        spd = CONFIG['scrollspeed']
        # self.image.blit(round(self.pos1,0), 0)
        # self.image.blit(round(self.pos2,0), 0)
        self.pos_x=self.pos_x-round(spd*1000*dt,2)

    def draw(self):

        #self.image.blit(100, 200)
        self.image.blit(round(self.pos_x,0), round(self.pos_y,0))
        
        