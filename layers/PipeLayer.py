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


class PipeLayer(Layer):
    '''
    classdocs
    '''


    def __init__(self):
        # always call super()
        super(PipeLayer, self).__init__()

        # load the image form file
        self.pipes = []

        self.x = CONFIG['originsize'][0]
        self.y = CONFIG['originsize'][1]
        self.pos1=0
        self.pos2=self.x
        # timer = threading.Timer(5, self.timerAction)
        # timer.start()
        self.interval = CONFIG['interval']
        pyglet.clock.schedule_interval(self.update, self.interval)
        self.generatePipe()
        self.distance = 0.0

    def generatePipe(self):

        rdm = random.random()
        pos_y = rdm*200+230
#         print pos_y
        pipe1 = Pipe(True,320,pos_y)
        pipe2 = Pipe(False,320,pos_y)

        self.pipes.append(pipe1)
        self.pipes.append(pipe2)


    def update(self,dt):
        spd = CONFIG['scrollspeed']
        # self.image.blit(round(self.pos1,0), 0)
        # self.image.blit(round(self.pos2,0), 0)
        for itm in self.pipes:
            itm.update(dt)
        item = self.pipes[0]
        if (item.pos_x+item.image_x)<0:
            self.pipes = self.pipes[2:]
            #print "remove pipe"
        self.distance = self.distance+dt*1000*spd
        if self.distance>CONFIG['distance']:
            self.generatePipe()
            self.distance=0.0


    def draw(self):
        # blit the image on every frame
        # spd = CONFIG['scrollspeed']
        # print spd
        # self.pos1=self.pos1-spd
        # self.pos2=self.pos2-spd
        for item in self.pipes:
            item.draw()       
        
        