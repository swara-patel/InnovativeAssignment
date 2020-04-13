#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.locals import *
import sys
import time
import random
class Innovative:
    def __init__(self):
        self.w=750            
        self.h=550
        self.reset=True
        self.active = False
        self.ans=''      
        self.word = ''
        self.stime = 0  
        self.ttime = 0
        self.acrcy = '0%'    
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 204, 193)
        self.TEXT_C = (91, 191, 253)
        self.RESULT_C = (255,70,70)
        pygame.init()
        self.oimg = pygame.image.load('type-speed-open.jpg')  
        self.oimg = pygame.transform.scale(self.oimg, (self.w,self.h))
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (750,550))
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Typing Speed')
    def draw(self, screen, msg, y ,fsize, color):  
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1,color)
        rect = text.get_rect(center=(self.w/2, y))  
        screen.blit(text, rect)
        pygame.display.update()
    def getline(self):  
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence
    def show(self, screen):    
        if(not self.end):
            #time
            self.ttime = time.time() - self.stime
            #accuracy
            count = 0
            for i,c in enumerate(self.word):
                try:
                    if self.ans[i] == c:
                        count += 1
                except:
                    pass
            self.acrcy = count/len(self.word)*100
            #words per minute
            self.wpm = len(self.ans)*60/(5*self.ttime)
            self.end = True
            print(self.ttime)
            self.results = 'Time:'+str(round(self.ttime)) +" secs    Accuracy:"+ str(round(self.acrcy)) + "%" + '    Wpm: ' + str(round(self.wpm))
            #reset button
            self.t_img = pygame.image.load('reset.jpg')
            self.t_img = pygame.transform.scale(self.t_img, (150,150))
            #(80,320)
            screen.blit(self.t_img, (self.w/2-75,self.h-140))
            self.draw(screen,"", self.h - 70, 26, (100,100,100))
            print(self.results)
            pygame.display.update()
    def rungame(self):
        self.resetgame()
        self.running=True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
            # update
            self.draw(self.screen, self.ans, 274, 26,(250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # input box position
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        self.active = True
                        self.ans = ''
                        self.stime = time.time()
                     # reset box position
                    if(x>=310 and x<=510 and y>=390 and self.end):
                        self.resetgame()
                        x,y = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.ans)
                            self.show(self.screen)
                            print(self.results)
                            self.draw(self.screen, self.results,350, 28, self.RESULT_C)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.ans= self.ans[:-1]
                        else:
                            try:
                                self.ans+= event.unicode
                            except:
                                pass
            pygame.display.update()
        clock.tick(60)
    def resetgame(self):
            self.screen.blit(self.oimg, (0,0))
            pygame.display.update()
            time.sleep(1)
            self.reset=False
            self.end = False
            self.ans=''
            self.word = ''
            self.stime = 0
            self.ttime = 0
            self.wpm = 0
            #random sentence
            self.word = self.getline()
            if (not self.word): self.resetgame()
            #drawing heading
            self.screen.fill((0,0,0))
            self.screen.blit(self.bg,(0,0))
            msg = "Typing Speed Test"
            self.draw(self.screen, msg,80, 80,self.HEAD_C)
            #rectangle for input box
            pygame.draw.rect(self.screen,(255, 204, 193), (50,250,650,50), 2)
            #sentence string
            self.draw(self.screen, self.word,200, 28,self.TEXT_C)
            pygame.display.update()
Innovative().rungame()


# In[ ]:




