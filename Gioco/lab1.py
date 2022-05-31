"""
if ballrect.colliderect(r1):
        if ballrect.colliderect(r1.right) or ballrect.colliderect(r1.left): # Moving right; Hit the left side of the wall
            speed[0] = -speed[0]
        if ballrect.colliderect(r1.top) or ballrect.colliderect(r1.bottom): # Moving left; Hit the right side of the wall
            speed[1] = -speed[1]
"""
#COLLISIONI
"""
if ballrect.colliderect(canestrorect):
        if ballrect.right > canestrorect.left or ballrect.left > canestrorect.right:
           speed[0] = -speed[0]
        if ballrect.top > canestrorect.bottom or ballrect.bottom > canestrorect.top:
            speed[1] = -speed[1]
"""
#LABIRINTO
"""
#orange = (255,117,20)
#ballrect = pg.draw.rect(screen, orange, (80,429,20,20),0)
white = (255,255,255)
r1 = pg.draw.rect(screen, white, (80,80,15,335),0)
r2 = pg.draw.rect(screen, white, (96,80,623,15),0)
r3 = pg.draw.rect(screen, white, (704,96,15,303),0)
r5 = pg.draw.rect(screen, white, (96,400,111,15),0)
r6 = pg.draw.rect(screen, white, (144,352,15,47),0)
r7 = pg.draw.rect(screen, white, (96,208,63,15),0)
r8 = pg.draw.rect(screen, white, (144,224,15,63),0)
r9 = pg.draw.rect(screen, white, (160,272,287,15),0)
r10 = pg.draw.rect(screen, white, (208,288,15,63),0)
r11 = pg.draw.rect(screen, white, (224,336,47,15),0)
r12 = pg.draw.rect(screen, white, (256,352,15,127),0)
r13 = pg.draw.rect(screen, white, (208,464,47,15),0)
r14 = pg.draw.rect(screen, white, (256,96,15,63),0)
r15 = pg.draw.rect(screen, white, (144,144,111,15),0)
r16 = pg.draw.rect(screen, white, (208,160,15,63),0)
r17 = pg.draw.rect(screen, white, (224,208,47,15),0)
r18 = pg.draw.rect(screen, white, (368,96,15,63),0)
r19 = pg.draw.rect(screen, white, (320,144,47,15),0)
r20 = pg.draw.rect(screen, white, (560,96,15,127),0)
r21 = pg.draw.rect(screen, white, (576,208,79,15),0)
r22 = pg.draw.rect(screen, white, (640,144,15,63),0)
r23 = pg.draw.rect(screen, white, (624,144,15,15),0)
r24 = pg.draw.rect(screen, white, (624,336,79,15),0)
r25 = pg.draw.rect(screen, white, (624,272,15,63),0)
r26 = pg.draw.rect(screen, white, (640,272,15,15),0)
r27 = pg.draw.rect(screen, white, (80,464,15,255),0)
r28 = pg.draw.rect(screen, white, (96,704,623,15),0)
r29 = pg.draw.rect(screen, white, (704,448,15,255),0)
r30 = pg.draw.rect(screen, white, (640,448,63,15),0)
r31 = pg.draw.rect(screen, white, (640,400,15,47),0)
r32 = pg.draw.rect(screen, white, (560,400,79,15),0)
r33 = pg.draw.rect(screen, white, (560,272,15,127),0)
r34 = pg.draw.rect(screen, white, (448,336,111,15),0)
r35 = pg.draw.rect(screen, white, (496,352,15,47),0)
r36 = pg.draw.rect(screen, white, (496,272,63,15),0)
r37 = pg.draw.rect(screen, white, (496,144,15,127),0)
r38 = pg.draw.rect(screen, white, (432,144,63,15),0)
r30 = pg.draw.rect(screen, white, (432,160,15,63),0)
r40 = pg.draw.rect(screen, white, (320,208,111,15),0)
r41 = pg.draw.rect(screen, white, (640,560,63,15),0)
r42 = pg.draw.rect(screen, white, (640,512,15,47),0)
r43 = pg.draw.rect(screen, white, (448,512,191,15),0)
r44 = pg.draw.rect(screen, white, (576,464,15,47),0)
r45 = pg.draw.rect(screen, white, (448,448,15,63),0)
r46 = pg.draw.rect(screen, white, (464,448,47,15),0)
r47 = pg.draw.rect(screen, white, (640,576,15,79),0)
r48 = pg.draw.rect(screen, white, (576,528,15,127),0)
r49 = pg.draw.rect(screen, white, (512,640,63,15),0)
r50 = pg.draw.rect(screen, white, (512,576,15,63),0)
r51 = pg.draw.rect(screen, white, (384,576,127,15),0)
r52 = pg.draw.rect(screen, white, (384,592,15,63),0)
r53 = pg.draw.rect(screen, white, (448,640,15,63),0)
r54 = pg.draw.rect(screen, white, (320,336,79,15),0)
r55 = pg.draw.rect(screen, white, (384,352,15,175),0)
r56 = pg.draw.rect(screen, white, (320,400,15,143),0)
r57 = pg.draw.rect(screen, white, (272,528,47,15),0)
r58 = pg.draw.rect(screen, white, (272,544,15,63),0)
r59 = pg.draw.rect(screen, white, (320,640,15,63),0)
r60 = pg.draw.rect(screen, white, (272,640,47,15),0)
r61 = pg.draw.rect(screen, white, (208,656,15,47),0)
r62 = pg.draw.rect(screen, white, (96,464,63,15),0)
r63 = pg.draw.rect(screen, white, (144,480,15,63),0)
r64 = pg.draw.rect(screen, white, (160,528,63,15),0)
r65 = pg.draw.rect(screen, white, (208,544,15,63),0)
r66 = pg.draw.rect(screen, white, (144,592,63,15),0)
r67 = pg.draw.rect(screen, white, (144,608,15,47),0)
"""