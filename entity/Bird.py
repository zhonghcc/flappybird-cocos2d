#coding=utf8
'''
Created on 2016年3月21日

@author: zhonghcc
'''
import pyglet
import threading
from cocos.sprite import Sprite
from pyglet.window import key
from cocos.actions import *
from config import CONFIG,ASSETS

class Bird(object):
    '''
    classdocs
    '''


    def __init__(self,layer,pos_x,pos_y):
        # always call super()
        

        # load the image form file
        self.image = []
        self.image.append( pyglet.resource.image(CONFIG['assetspath']+'bird0_0.png'))
        self.image.append( pyglet.resource.image(CONFIG['assetspath']+'bird0_1.png'))
        self.image.append( pyglet.resource.image(CONFIG['assetspath']+'bird0_2.png'))

        self.image[0].anchor_x = self.image[0].width // 2
        self.image[0].anchor_y = self.image[0].height // 2

        self.sprite = Sprite(self.image[0])
        self.sprite.position = pos_x,pos_y

        self.layer = layer
        self.layer.add(self.sprite)
        self.pos_x=pos_x
        self.pos_y=pos_y



    def update(self,dt):
        spd = CONFIG['scrollspeed']
        # self.image.blit(round(self.pos1,0), 0)
        # self.image.blit(round(self.pos2,0), 0)
        # self.pos_x=self.pos_x-round(spd*1000*dt,2)

    def draw(self):
        pass
        #self.image.blit(100, 200)
        #self.image[0].blit(round(self.pos_x,0), round(self.pos_y,0))

    def on_key_release(self, keys, mod):
        # LEFT: go to previous scene
        # RIGTH: go to next scene
        # ENTER: restart scene
        jumpheight = CONFIG['jumpheight']
        jumpduration = CONFIG['jumpduration']
        if keys == key.SPACE:
            act = JumpBy((0,-self.pos_y),jumpheight, 1, jumpduration)
            self.sprite.do(act)
            return True

        
        