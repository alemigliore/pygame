from string import whitespace
import numpy as np
import sys
import serial, time
import pygame as pg
from pygame.mixer import Sound
import threading, queue
import time


pg.init()
#PYGAME CONFIG

width = 800
height = 800
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

#CARICAMENTO SFONDO

sfondo = pg.image.load("./labirinto.png")
sfondorect = sfondo.get_rect()
sfondorect.centerx = width//2
sfondorect.centery = height//2

#MUSICA
def caricaSuono(file):
    return Sound(file)

musica = caricaSuono("./car-drive-561.mp3")
musica.play()

impatto = caricaSuono("./impatto.mp3")

#CARICAMENTO MURI DEL LABIRINTO

r1 = pg.image.load("./r1.png")
rect1 = r1.get_rect()
rect1.center = (88, 248)
r2 = pg.image.load("./r2.png")
rect2 = r2.get_rect()
rect2.center = (408, 88)
r3 = pg.image.load("./r3.png")
rect3 = r3.get_rect()
rect3.center = (712, 248)
r4 = pg.image.load("./r4.png")
rect4 = r4.get_rect()
rect4.center = (712, 576)
r5 = pg.image.load("./r5.png")
rect5 = r5.get_rect()
rect5.center = (408, 712)
r6 = pg.image.load("./r6.png")
rect6 = r6.get_rect()
rect6.center = (88,592)
r7 = pg.image.load("./r7.png")
rect7 = r7.get_rect()
rect7.center = (128, 472)
r8 = pg.image.load("./r8.png")
rect8 = r8.get_rect()
rect8.center = (152,512)
r9 = pg.image.load("./r9.png")
rect9 = r9.get_rect()
rect9.center = (192,536)
r10 = pg.image.load("./r10.png")
rect10 = r10.get_rect()
rect10.center = (216,576)
r11 = pg.image.load("./r11.png")
rect11 = r11.get_rect()
rect11.center = (216,680)
r12 = pg.image.load("./r12.png")
rect12 = r12.get_rect()
rect12.center = (328,672)
r13 = pg.image.load("./r13.png")
rect13 = r13.get_rect()
rect13.center = (456,672)
r14 = pg.image.load("./r14.png")
rect14 = r14.get_rect()
rect14.center = (680,568)
r15 = pg.image.load("./r15.png")
rect15 = r15.get_rect()
rect15.center = (648,584)
r16 = pg.image.load("./r16.png")
rect16 = r16.get_rect()
rect16.center = (544,520)
r17 = pg.image.load("./r17.png")
rect17 = r17.get_rect()
rect17.center = (584,488)
r18 = pg.image.load("./r18.png")
rect18 = r18.get_rect()
rect18.center = (584,592)
r19 = pg.image.load("./r19.png")
rect19 = r19.get_rect()
rect19.center = (544,648)
r20 = pg.image.load("./r20.png")
rect20 = r20.get_rect()
rect20.center = (520,608)
r21 = pg.image.load("./r21.png")
rect21 = r21.get_rect()
rect21.center = (448,584)
r22 = pg.image.load("./r22.png")
rect22 = r22.get_rect()
rect22.center = (456,480)
r23 = pg.image.load("./r23.png")
rect23 = r23.get_rect()
rect23.center = (328,472)
r24 = pg.image.load("./r24.png")
rect24 = r24.get_rect()
rect24.center = (296,536)
r25 = pg.image.load("./r25.png")
rect25 = r25.get_rect()
rect25.center = (280,576)
r26 = pg.image.load("./r26.png")
rect26 = r26.get_rect()
rect26.center = (360,344)
r27 = pg.image.load("./r27.png")
rect27 = r27.get_rect()
rect27.center = (392,440)
r28 = pg.image.load("./r28.png")
rect28 = r28.get_rect()
rect28.center = (152,408)
r29 = pg.image.load("./r29.png")
rect29 = r29.get_rect()
rect29.center = (376,128)
r30 = pg.image.load("./r30.png")
rect30 = r30.get_rect()
rect30.center = (264,128)
r31 = pg.image.load("./r31.png")
rect31 = r31.get_rect()
rect31.center = (200,152)
r32 = pg.image.load("./r32.png")
rect32 = r32.get_rect()
rect32.center = (128,240)
r33 = pg.image.load("./r33.png")
rect33 = r33.get_rect()
rect33.center = (152,256)
r34 = pg.image.load("./r34.png")
rect34 = r34.get_rect()
rect34.center = (304,280)
r35 = pg.image.load("./r35.png")
rect35 = r35.get_rect()
rect35.center = (216,320)
r36 = pg.image.load("./r36.png")
rect36 = r36.get_rect()
rect36.center = (248,344)
r37 = pg.image.load("./r37.png")
rect37 = r37.get_rect()
rect37.center = (264,416)
r38 = pg.image.load("./r38.png")
rect38 = r38.get_rect()
rect38.center = (664,344)
r39 = pg.image.load("./r39.png")
rect39 = r39.get_rect()
rect39.center = (632,304)
r40 = pg.image.load("./r40.png")
rect40 = r40.get_rect()
rect40.center = (672,456)
r41 = pg.image.load("./r41.png")
rect41 = r41.get_rect()
rect41.center = (648,424)
r42 = pg.image.load("./r42.png")
rect42 = r42.get_rect()
rect42.center = (600,408)
r43 = pg.image.load("./r43.png")
rect43 = r43.get_rect()
rect43.center = (568,336)
r44 = pg.image.load("./r44.png")
rect44 = r44.get_rect()
rect44.center = (504,344)
r45 = pg.image.load("./r45.png")
rect45 = r45.get_rect()
rect45.center = (528,280)
r46 = pg.image.load("./r46.png")
rect46 = r46.get_rect()
rect46.center = (504,208)
r47 = pg.image.load("./r47.png")
rect47 = r47.get_rect()
rect47.center = (464,152)
r48 = pg.image.load("./r48.png")
rect48 = r48.get_rect()
rect48.center = (440,192)
r49 = pg.image.load("./r49.png")
rect49 = r49.get_rect()
rect49.center = (376,216)
r50 = pg.image.load("./r50.png")
rect50 = r50.get_rect()
rect50.center = (568,160)
r51 = pg.image.load("./r51.png")
rect51 = r51.get_rect()
rect51.center = (616,216)
r52 = pg.image.load("./r52.png")
rect52 = r52.get_rect()
rect52.center = (648,176)

#CARICAMENTO IMMAGINE PALLA/CANESTRO/VITTORIA

ball = pg.image.load("./ball.png")
ballrect = ball.get_rect()
ballrect.centerx = 90
ballrect.centery = 440
canestro = pg.image.load("./canestro.png")
canestrorect = canestro.get_rect()
canestrorect.centerx = 750
canestrorect.centery = 420
win = pg.image.load("./win.png")
winrect = win.get_rect()
winrect.centerx = width//2
winrect.centery = height//2


black = 0, 0, 0
dt = 1
gamma = 0.05
q = queue.Queue()

#GESTIONE THREAD

class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = "COM6"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.01)

running = True
rm = Read_Microbit()
rm.start()
#GESTIONE VELOCITA'
speed = [0, 0]
while running:
    acc = q.get()
    speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/1024.
    speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/1024.
    q.task_done()
    ballrect = ballrect.move(speed)

    #COLLISIONI MARGINI SCHERMO

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        #impatto
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        #impatto

    #COLLISIONE IMMAGINI MURI LABIRINTO

    if ballrect.colliderect(rect1):
        if ballrect.right > rect1.left or ballrect.left > rect1.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect1.bottom or ballrect.bottom > rect1.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect2):
        if ballrect.right > rect2.left or ballrect.left > rect2.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect2.bottom or ballrect.bottom > rect2.top:
            speed[1] = -speed[1] 
            impatto.play()
    if ballrect.colliderect(rect3):
        if ballrect.right > rect3.left or ballrect.left > rect3.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect3.bottom or ballrect.bottom > rect3.top:
            speed[1] = -speed[1]
            impatto.play()   
    if ballrect.colliderect(rect4):
        if ballrect.right > rect4.left or ballrect.left > rect4.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect4.bottom or ballrect.bottom > rect4.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect5):
        if ballrect.right > rect5.left or ballrect.left > rect5.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect5.bottom or ballrect.bottom > rect5.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect6):
        if ballrect.right > rect6.left or ballrect.left > rect6.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect6.bottom or ballrect.bottom > rect6.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect7):
        if ballrect.right > rect7.left or ballrect.left > rect7.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect7.bottom or ballrect.bottom > rect7.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect8):
        if ballrect.right > rect8.left or ballrect.left > rect8.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect8.bottom or ballrect.bottom > rect8.top:
            speed[1] = -speed[1] 
            impatto.play()
    if ballrect.colliderect(rect9):
        if ballrect.right > rect9.left or ballrect.left > rect9.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect9.bottom or ballrect.bottom > rect9.top:
            speed[1] = -speed[1]
            impatto.play()   
    if ballrect.colliderect(rect10):
        if ballrect.right > rect10.left or ballrect.left > rect10.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect10.bottom or ballrect.bottom > rect10.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect11):
        if ballrect.right > rect11.left or ballrect.left > rect11.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect11.bottom or ballrect.bottom > rect11.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect12):
        if ballrect.right > rect12.left or ballrect.left > rect12.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect12.bottom or ballrect.bottom > rect12.top:
            speed[1] = -speed[1] 
            impatto.play()
    if ballrect.colliderect(rect13):
        if ballrect.right > rect13.left or ballrect.left > rect13.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect13.bottom or ballrect.bottom > rect13.top:
            speed[1] = -speed[1]
    if ballrect.colliderect(rect14):
        if ballrect.right > rect14.left or ballrect.left > rect14.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect14.bottom or ballrect.bottom > rect14.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect15):
        if ballrect.right > rect15.left or ballrect.left > rect15.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect15.bottom or ballrect.bottom > rect15.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect16):
        if ballrect.right > rect16.left or ballrect.left > rect16.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect16.bottom or ballrect.bottom > rect16.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect17):
        if ballrect.right > rect17.left or ballrect.left > rect17.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect17.bottom or ballrect.bottom > rect17.top:
            speed[1] = -speed[1] 
            impatto.play()
    if ballrect.colliderect(rect18):
        if ballrect.right > rect18.left or ballrect.left > rect18.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect18.bottom or ballrect.bottom > rect18.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect19):
        if ballrect.right > rect19.left or ballrect.left > rect19.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect19.bottom or ballrect.bottom > rect19.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect20):
        if ballrect.right > rect20.left or ballrect.left > rect20.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect20.bottom or ballrect.bottom > rect20.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect21):
        if ballrect.right > rect21.left or ballrect.left > rect21.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect21.bottom or ballrect.bottom > rect2.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect22):
        if ballrect.right > rect22.left or ballrect.left > rect22.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect22.bottom or ballrect.bottom > rect22.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect23):
        if ballrect.right > rect23.left or ballrect.left > rect23.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect23.bottom or ballrect.bottom > rect23.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect2):
        if ballrect.right > rect24.left or ballrect.left > rect24.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect24.bottom or ballrect.bottom > rect24.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect25):
        if ballrect.right > rect25.left or ballrect.left > rect25.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect25.bottom or ballrect.bottom > rect25.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect26):
        if ballrect.right > rect26.left or ballrect.left > rect26.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect26.bottom or ballrect.bottom > rect26.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect27):
        if ballrect.right > rect27.left or ballrect.left > rect27.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect27.bottom or ballrect.bottom > rect27.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect28):
        if ballrect.right > rect28.left or ballrect.left > rect28.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect28.bottom or ballrect.bottom > rect28.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect29):
        if ballrect.right > rect29.left or ballrect.left > rect29.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect29.bottom or ballrect.bottom > rect29.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect30):
        if ballrect.right > rect30.left or ballrect.left > rect30.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect30.bottom or ballrect.bottom > rect30.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect31):
        if ballrect.right > rect31.left or ballrect.left > rect31.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect31.bottom or ballrect.bottom > rect31.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect32):
        if ballrect.right > rect32.left or ballrect.left > rect32.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect32.bottom or ballrect.bottom > rect32.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect33):
        if ballrect.right > rect33.left or ballrect.left > rect33.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect33.bottom or ballrect.bottom > rect33.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect34):
        if ballrect.right > rect34.left or ballrect.left > rect34.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect34.bottom or ballrect.bottom > rect34.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect35):
        if ballrect.right > rect35.left or ballrect.left > rect35.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect35.bottom or ballrect.bottom > rect35.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect36):
        if ballrect.right > rect36.left or ballrect.left > rect36.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect36.bottom or ballrect.bottom > rect36.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect37):
        if ballrect.right > rect37.left or ballrect.left > rect37.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect37.bottom or ballrect.bottom > rect37.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect38):
        if ballrect.right > rect38.left or ballrect.left > rect38.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect38.bottom or ballrect.bottom > rect38.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect39):
        if ballrect.right > rect39.left or ballrect.left > rect39.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect39.bottom or ballrect.bottom > rect39.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect40):
        if ballrect.right > rect40.left or ballrect.left > rect40.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect40.bottom or ballrect.bottom > rect40.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect41):
        if ballrect.right > rect41.left or ballrect.left > rect41.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect41.bottom or ballrect.bottom > rect41.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect42):
        if ballrect.right > rect42.left or ballrect.left > rect42.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect42.bottom or ballrect.bottom > rect42.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect43):
        if ballrect.right > rect43.left or ballrect.left > rect43.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect43.bottom or ballrect.bottom > rect43.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect44):
        if ballrect.right > rect44.left or ballrect.left > rect44.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect44.bottom or ballrect.bottom > rect44.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect45):
        if ballrect.right > rect45.left or ballrect.left > rect45.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect45.bottom or ballrect.bottom > rect45.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect46):
        if ballrect.right > rect46.left or ballrect.left > rect46.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect46.bottom or ballrect.bottom > rect46.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect47):
        if ballrect.right > rect47.left or ballrect.left > rect47.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect47.bottom or ballrect.bottom > rect47.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect48):
        if ballrect.right > rect48.left or ballrect.left > rect48.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect48.bottom or ballrect.bottom > rect48.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect49):
        if ballrect.right > rect49.left or ballrect.left > rect49.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect49.bottom or ballrect.bottom > rect49.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect50):
        if ballrect.right > rect50.left or ballrect.left > rect50.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect50.bottom or ballrect.bottom > rect50.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect51):
        if ballrect.right > rect51.left or ballrect.left > rect51.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect51.bottom or ballrect.bottom > rect51.top:
            speed[1] = -speed[1]
            impatto.play()
    if ballrect.colliderect(rect52):
        if ballrect.right > rect52.left or ballrect.left > rect52.right:
           speed[0] = -speed[0]
           impatto.play()
        if ballrect.top > rect52.bottom or ballrect.bottom > rect52.top:
            speed[1] = -speed[1]
            impatto.play()
    
    #COLLISIONE CON CANESTRO E SCHERMATA VITTORIA

    if ballrect.colliderect(canestrorect):
        if ballrect.right > canestrorect.left or ballrect.left > canestrorect.right:
            screen.blit(win, winrect)
            pg.display.flip()
            pg.quit()
        if ballrect.top > canestrorect.bottom or ballrect.bottom > canestrorect.top:
            screen.blit(win, winrect)
            pg.display.flip()  
            pg.quit()  
    else:

        #IMPOSTA SFONDO

        screen.blit(sfondo, sfondorect)

        #IMPOSTA MURI LABIRINTO

        screen.blit(r1, rect1)
        screen.blit(r2, rect2)
        screen.blit(r3, rect3)
        screen.blit(r4, rect4)
        screen.blit(r5, rect5)
        screen.blit(r6, rect6)
        screen.blit(r7, rect7)
        screen.blit(r8, rect8)
        screen.blit(r9, rect9)
        screen.blit(r10, rect10)
        screen.blit(r11, rect11)
        screen.blit(r12, rect12)
        screen.blit(r13, rect13)
        screen.blit(r14, rect14)
        screen.blit(r15, rect15)
        screen.blit(r16, rect16)
        screen.blit(r17, rect17)
        screen.blit(r18, rect18)
        screen.blit(r19, rect19)
        screen.blit(r20, rect20)
        screen.blit(r21, rect21)
        screen.blit(r22, rect22)
        screen.blit(r23, rect23)
        screen.blit(r24, rect24)
        screen.blit(r25, rect25)
        screen.blit(r26, rect26)
        screen.blit(r27, rect27)
        screen.blit(r28, rect28)
        screen.blit(r29, rect29)
        screen.blit(r30, rect30)
        screen.blit(r31, rect31)
        screen.blit(r32, rect32)
        screen.blit(r33, rect33)
        screen.blit(r34, rect34)
        screen.blit(r35, rect35)
        screen.blit(r36, rect36)
        screen.blit(r37, rect37)
        screen.blit(r38, rect38)
        screen.blit(r39, rect39)
        screen.blit(r40, rect40)
        screen.blit(r41, rect41)
        screen.blit(r42, rect42)
        screen.blit(r43, rect43)
        screen.blit(r44, rect44)
        screen.blit(r45, rect45)
        screen.blit(r46, rect46)
        screen.blit(r47, rect47)
        screen.blit(r48, rect48)
        screen.blit(r49, rect49)
        screen.blit(r50, rect50)
        screen.blit(r51, rect51)
        screen.blit(r52, rect52)

        #IMPOSTA PALLA E CANESTRO

        screen.blit(ball, ballrect)
        screen.blit(canestro, canestrorect)

        pg.display.flip()
        clock.tick(10)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                Sound.stop()
                pg.quit()

   
rm.terminate()
rm.join()