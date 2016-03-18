#coding=utf8
'''
Created on 2016年3月19日

@author: zhonghcc
'''
import pyglet
from cocos.layer import Layer

from config import CONFIG,ASSETS

class BackgroundLayer(Layer):
    '''
    classdocs
    '''


    def __init__(self):
        # always call super()
        super(BackgroundLayer, self).__init__()

        # load the image form file
        self.image = pyglet.resource.image(CONFIG['assetspath']+'bg_day.png')
        
        self.x = CONFIG['originsize'][0]
        self.y = CONFIG['originsize'][1]
        self.pos1=0
        self.pos2=self.x

    def draw(self):
        # blit the image on every frame
        spd = CONFIG['scrollspeed']
        print spd
        self.image.blit(round(self.pos1,0), 0)
        self.image.blit(round(self.pos2,0), 0)
        self.pos1=self.pos1-spd
        self.pos2=self.pos2-spd
#     def update(self,dt):
#         print 'update'
        
        