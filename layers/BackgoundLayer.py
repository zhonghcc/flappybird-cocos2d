#coding=utf8
'''
Created on 2016年3月19日

@author: zhonghcc
'''
import pyglet
import threading
from cocos.layer import Layer

from config import CONFIG,ASSETS

class BackgroundLayer(Layer):
    '''
    classdocs
    '''


    def __init__(self,asset):
        # always call super()
        super(BackgroundLayer, self).__init__()

        # load the image form file
        self.asset = asset
        self.image = pyglet.resource.image(CONFIG['assetspath']+self.asset+'.png')
        
        self.x = CONFIG['originsize'][0]
        self.y = CONFIG['originsize'][1]
        self.pos1=0
        self.pos2=self.x
        # timer = threading.Timer(5, self.timerAction)
        # timer.start()
        pyglet.clock.schedule_interval(self.update, 1/120.0)

    def update(self,dt):
        spd = CONFIG['scrollspeed']
        print spd
        # self.image.blit(round(self.pos1,0), 0)
        # self.image.blit(round(self.pos2,0), 0)
        self.pos1=self.pos1-spd
        self.pos2=self.pos2-spd
        if self.pos1<0 and self.pos2<0:
            if self.pos1<self.pos2:
                self.pos1=self.pos2+self.x
            else:
                self.pos2=self.pos1+self.x

    def draw(self):
        # blit the image on every frame
        # spd = CONFIG['scrollspeed']
        # print spd
        self.image.blit(round(self.pos1,0), 0)
        self.image.blit(round(self.pos2,0), 0)
        # self.pos1=self.pos1-spd
        # self.pos2=self.pos2-spd
        pass
        
        