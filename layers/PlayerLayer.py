#coding=utf8
'''
Created on 2016年3月21日

@author: zhonghcc
'''
import pyglet
import threading
from cocos.layer import Layer

from config import CONFIG,ASSETS
from entity.Pipe import Pipe
import random
import Queue
from entity.Bird import Bird

class PlayerLayer(Layer):
    '''
    classdocs
    '''
    is_event_handler = True

    def __init__(self):
        # always call super()
        super(PlayerLayer, self).__init__()

        # load the image form file
        startpos = CONFIG['startpos']
        self.player = Bird(self,startpos[0],startpos[1])




    def update(self,dt):
        spd = CONFIG['scrollspeed']
        # self.image.blit(round(self.pos1,0), 0)
        # self.image.blit(round(self.pos2,0), 0)
        self.player.update(dt)


    def draw(self):
        # blit the image on every frame
        # spd = CONFIG['scrollspeed']
        # print spd
        # self.pos1=self.pos1-spd
        # self.pos2=self.pos2-spd
        self.player.draw()       

    def on_key_release(self, keys, mod):
        self.player.on_key_release(keys,mod)
        
        