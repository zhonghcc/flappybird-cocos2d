#coding=utf8
'''
Created on 2016年3月21日

@author: zhonghcc
'''
import pyglet
import threading


from config import CONFIG,ASSETS

class Bird(object):
    '''
    classdocs
    '''


    def __init__(self,pos_x,pos_y):
        # always call super()
        

        # load the image form file
        self.image = []
        self.image.append( pyglet.resource.image(CONFIG['assetspath']+'bird0_0.png'))
        self.image.append( pyglet.resource.image(CONFIG['assetspath']+'bird0_1.png'))
        self.image.append( pyglet.resource.image(CONFIG['assetspath']+'bird0_2.png'))
        
        self.pos_x=pos_x
        self.pos_y=pos_y

    def update(self,dt):
        spd = CONFIG['scrollspeed']
        # self.image.blit(round(self.pos1,0), 0)
        # self.image.blit(round(self.pos2,0), 0)
        # self.pos_x=self.pos_x-round(spd*1000*dt,2)

    def draw(self):

        #self.image.blit(100, 200)
        self.image[0].blit(round(self.pos_x,0), round(self.pos_y,0))
        
        