import pygame
import random
import time
pygame.init()
HALLOWEEN_NIGHT = pygame.display.set_mode((1000,563))
pygame.display.set_caption('HALLOWEEN NIGHT')
clock = pygame.time.Clock()
play_im = [pygame.image.load('s1.gif'),pygame.image.load('s2.gif'),pygame.image.load('s3.gif'),pygame.image.load('s4.gif')]
menu_game = pygame.image.load('menu.png')
station = [pygame.image.load('p1_1.gif'),pygame.image.load('p_2.png'),pygame.image.load('3.png')]
dek_run = [pygame.image.load('dekrun2.png'),pygame.image.load('dekrun3.png'),pygame.image.load('dekrun4.png'),pygame.image.load('dekrun5.png'),pygame.image.load('dekrun6.png'),pygame.image.load('dekrun7.png')]
dek_yrun = pygame.image.load('dekrun1.png')
dek_dead = [pygame.image.load('dekd1.png'),pygame.image.load('dekd2.png')]
dek_j = [pygame.image.load('dekj2.png'),pygame.image.load('dekj3.png'),pygame.image.load('dekj4.png')]
gun_b = [pygame.image.load('dekpower1_b.png'),pygame.image.load('dekpower2_b.png'),pygame.image.load('dekpower3_b.png'),pygame.image.load('dekpower4_b.png'),pygame.image.load('dekpower5_b.png'),pygame.image.load('dekpower6_b.png')]
gun_r = [pygame.image.load('dekpower1_r.png'),pygame.image.load('dekpower2_r.png'),pygame.image.load('dekpower3_r.png'),pygame.image.load('dekpower4_r.png'),pygame.image.load('dekpower5_r.png'),pygame.image.load('dekpower6_r.png')]
gum_p = [pygame.image.load('dekpower_1p.png'),pygame.image.load('dekpower_2p.png'),pygame.image.load('dekpower_3p.png'),pygame.image.load('dekpower_4p.png'),pygame.image.load('dekpower_5p.png'),pygame.image.load('dekpower_6p.png')]
candy_1 = pygame.image.load('candy.png')
blooddek = [pygame.image.load('ji1.gif'),pygame.image.load('ji2.gif'),pygame.image.load('ji3.gif'),pygame.image.load('ji4.gif'),pygame.image.load('ji5.gif'),pygame.image.load('ji6.gif'),pygame.image.load('ji7.gif'),pygame.image.load('ji8.gif'),pygame.image.load('ji9.gif'),pygame.image.load('ji10.gif'),pygame.image.load('ji11.gif')]
boss_1 = [pygame.image.load('drun1.png'),pygame.image.load('drun2.gif'),pygame.image.load('drun3.gif'),pygame.image.load('drun4.gif'),pygame.image.load('drun5.png'),pygame.image.load('drun6.gif'),pygame.image.load('drun7.png'),pygame.image.load('drun8.png'),pygame.image.load('drun9.png')]
dpower_1 = [pygame.image.load('dpower1.gif'),pygame.image.load('dpower2.gif')]
dStand_1 = [pygame.image.load('dStand1.gif'),pygame.image.load('dStand2.png'),pygame.image.load('dStand3.png'),pygame.image.load('dStand4.png'),pygame.image.load('dStand5.png'),pygame.image.load('dStand6.png'),pygame.image.load('dStand7.png'),pygame.image.load('dStand9.png'),pygame.image.load('dStand10.png'),pygame.image.load('dStand11.png'),pygame.image.load('dStand12.png'),pygame.image.load('dStand13.png')]
boss_2 = [pygame.image.load('swalk1.gif'),pygame.image.load('swalk2.gif'),pygame.image.load('swalk3.gif'),pygame.image.load('swalk4.gif'),pygame.image.load('swalk5.gif')]
sdead_2 = [pygame.image.load('sdead1.gif'),pygame.image.load('sdead2.gif'),pygame.image.load('sdead3.gif'),pygame.image.load('sdead4.gif'),]
spower_2 = [pygame.image.load('spower2.gif'),pygame.image.load('spower3.gif'),pygame.image.load('spower4.gif'),pygame.image.load('spower5.gif'),pygame.image.load('spower6.gif')]
sStand_2 = [pygame.image.load('swalk1.gif'),pygame.image.load('swalk2.gif')]
boss_3 = [pygame.image.load('zrun1.gif'),pygame.image.load('zrun2.gif'),pygame.image.load('zrun3.gif'),pygame.image.load('zrun4.gif'),pygame.image.load('zrun5.gif'),pygame.image.load('zrun6.gif'),pygame.image.load('zrun7.gif')]
zpower_3 = [pygame.image.load('zpower1.gif'),pygame.image.load('zpower2.gif'),pygame.image.load('zpower3.gif'),pygame.image.load('zpower4.gif'),pygame.image.load('zpower5.gif'),pygame.image.load('zpower6.gif'),pygame.image.load('zpower7.gif'),pygame.image.load('zpower8.gif'),pygame.image.load('zpower9.gif'),pygame.image.load('zpower10.gif'),pygame.image.load('zpower11.gif'),pygame.image.load('zpower12.gif'),pygame.image.load('zpower13.gif'),pygame.image.load('zpower14.gif'),pygame.image.load('zpower15.gif')]
zStand_3 = [pygame.image.load('zstand1.gif'),pygame.image.load('zstand2.gif'),pygame.image.load('zstand3.gif'),pygame.image.load('zstand4.gif'),pygame.image.load('zstand5.gif'),pygame.image.load('zstand6.gif'),pygame.image.load('zstand7.gif')]
zdead_3 = [pygame.image.load('zdead1.gif'),pygame.image.load('zdead2.gif'),pygame.image.load('zdead3.gif'),pygame.image.load('zdead4.gif'),pygame.image.load('zdead5.gif'),pygame.image.load('zdead6.gif'),pygame.image.load('zdead7.gif'),pygame.image.load('zdead8.gif'),pygame.image.load('zdead9.gif'),pygame.image.load('zdead10.gif'),pygame.image.load('zdead11.gif'),pygame.image.load('zdead12.gif'),pygame.image.load('zdead13.gif'),pygame.image.load('zdead14.gif'),pygame.image.load('zdead15.gif'),pygame.image.load('zdead16.gif'),pygame.image.load('zdead17.gif'),pygame.image.load('zdead18.gif'),pygame.image.load('zdead19.gif')]
gunboss_1 = [pygame.image.load('dbullet.png'),pygame.image.load('dbullet2.png'),pygame.image.load('dbullet3.png'),pygame.image.load('dbullet4.png'),pygame.image.load('dbullet5.png')]
gunboss_2 = [pygame.image.load('sbullet1.png'),pygame.image.load('sbullet2.png'),pygame.image.load('sbullet3.png'),pygame.image.load('sbullet4.png'),pygame.image.load('sbullet5.png'),pygame.image.load('sbullet6.png')]
gunboss_3 = [pygame.image.load('zbullet1.png'),pygame.image.load('zbullet2.png'),pygame.image.load('zbullet3.png'),pygame.image.load('zbullet4.png'),pygame.image.load('zbullet5.png'),pygame.image.load('zbullet6.png')]
bloodz_3 = [pygame.image.load('zlod1.png'),pygame.image.load('zlod2.png'),pygame.image.load('zlod3.png'),pygame.image.load('zlod4.png'),pygame.image.load('zlod5.png'),pygame.image.load('zlod6.png'),pygame.image.load('zlod7.png')]
bloods_2 = [pygame.image.load('slod1.png'),pygame.image.load('slod2.png'),pygame.image.load('slod3.png'),pygame.image.load('slod4.png'),pygame.image.load('slod5.png'),pygame.image.load('slod6.png'),pygame.image.load('slod7.png')]
bloodd_1 = [pygame.image.load('dlod1.png'),pygame.image.load('dlod2.png'),pygame.image.load('dlod3.png'),pygame.image.load('dlod4.png'),pygame.image.load('dlod5.png'),pygame.image.load('dlod6.png'),pygame.image.load('dlod7.png')]
music_play_im = pygame.mixer.music.load('Opening.mp3')
drawback_1 =[pygame.image.load('k1.png'),pygame.image.load('k2.png'),pygame.image.load('k3.png')]
game_over_1 = [pygame.image.load('game-over-1.png'),pygame.image.load('game-over-2.png'),pygame.image.load('game-over-3.png')]
game_over_2 = [pygame.image.load('game-over-4.png'),pygame.image.load('game-over-5.png'),pygame.image.load('game-over-6.png')]
game_win_1 = [pygame.image.load('win1.gif'),pygame.image.load('win2.gif')]
game_win_2 = [pygame.image.load('win3.gif'),pygame.image.load('win4.gif')]
font = pygame.font.SysFont('comicsans', 40, True)
pygame.mixer.music.play(-1)

class bosse(object):
        
    def __init__(self):
        self.u = 0
        self.x = 1000
        self.y = 300
        self.hp = 6
        
    def move(self):
        self.u +=1
        global attack
        global hpd,e,levels,x_back
        global bossis
        global levels
        if(levels == 1):
            if(self.x >= 700):
                self.x -= 5
                
                HALLOWEEN_NIGHT.blit(boss_1[self.u//4%9],(self.x,self.y))
                
            else:
                
                if(attack <= 0):
                    HALLOWEEN_NIGHT.blit(dStand_1[(self.u//4)%12],(self.x,self.y))
                else:
                    HALLOWEEN_NIGHT.blit(boss_1[(self.u//15)%2],(self.x,self.y))
                if(hpd == 6):
                    HALLOWEEN_NIGHT.blit(bloodd_1[0],(self.x-15,self.y-50))
                if(hpd == 5):
                    HALLOWEEN_NIGHT.blit(bloodd_1[1],(self.x-15,self.y-50))
                if(hpd == 4):
                    HALLOWEEN_NIGHT.blit(bloodd_1[2],(self.x-15,self.y-50))
                if(hpd == 3):
                    HALLOWEEN_NIGHT.blit(bloodd_1[3],(self.x-15,self.y-50))
                if(hpd == 2):
                    HALLOWEEN_NIGHT.blit(bloodd_1[4],(self.x-15,self.y-50))
                if(hpd == 1):
                    HALLOWEEN_NIGHT.blit(bloodd_1[5],(self.x-15,self.y-50))
                if(hpd == 0):
                    bosslist.remove(self)
                    bossis = False
        if(levels == 2):
            if(self.x >= 700):
                self.x -= 5
                
                HALLOWEEN_NIGHT.blit(boss_2[self.u//4%5],(self.x,self.y+80))
                
            else:
                
                if(attack <= 0):
                    HALLOWEEN_NIGHT.blit(sStand_2[(self.u//16)%2],(self.x,self.y+80))
                else:
                    HALLOWEEN_NIGHT.blit(spower_2[(self.u//7)%4],(self.x,self.y+80))
                if(hpd == 7):
                    HALLOWEEN_NIGHT.blit(bloods_2[0],(self.x-40,self.y+50))
                if(hpd == 6):
                    HALLOWEEN_NIGHT.blit(bloods_2[1],(self.x-40,self.y+50))
                if(hpd == 5):
                    HALLOWEEN_NIGHT.blit(bloods_2[2],(self.x-40,self.y+50))
                if(hpd == 4):
                    HALLOWEEN_NIGHT.blit(bloods_2[3],(self.x-40,self.y+50))
                if(hpd == 3):
                    HALLOWEEN_NIGHT.blit(bloods_2[4],(self.x-40,self.y+50))
                if(hpd == 2):
                    HALLOWEEN_NIGHT.blit(bloods_2[5],(self.x-40,self.y+50))
                if(hpd == 1):
                    HALLOWEEN_NIGHT.blit(bloods_2[6],(self.x-40,self.y+50))
                if(hpd == 0):
                    bosslist.remove(self)
                    bossis = False
        if(levels == 3):
            if(self.x >= 700):
                self.x -= 5
                
                HALLOWEEN_NIGHT.blit(boss_3[self.u//4%7],(self.x-140,self.y-110))
                
            else:
                
                if(attack <= 0):
                    HALLOWEEN_NIGHT.blit(zStand_3[(self.u//4)%7],(self.x-140,self.y-110))
                else:
                    HALLOWEEN_NIGHT.blit(zpower_3[(self.u//2)%13],(self.x-140,self.y-110))
                if(hpd == 7):
                    HALLOWEEN_NIGHT.blit(bloodz_3[0],(self.x-15,self.y-80))
                if(hpd == 6):
                    HALLOWEEN_NIGHT.blit(bloodz_3[1],(self.x-15,self.y-80))
                if(hpd == 5):
                    HALLOWEEN_NIGHT.blit(bloodz_3[2],(self.x-15,self.y-80))
                if(hpd == 4):
                    HALLOWEEN_NIGHT.blit(bloodz_3[3],(self.x-15,self.y-80))
                if(hpd == 3):
                    HALLOWEEN_NIGHT.blit(bloodz_3[4],(self.x-15,self.y-80))
                if(hpd == 2):
                    HALLOWEEN_NIGHT.blit(bloodz_3[5],(self.x-15,self.y-80))
                if(hpd == 1):
                    HALLOWEEN_NIGHT.blit(bloodz_3[6],(self.x-15,self.y-80))
                if(hpd == 0):
                    bosslist.remove(self)
                    bossis = False

#class dek_de(object):
                
class gun_dek(object):
    def __init__(self,y):
        
        self.x = 100
        self.y = y
        self.u = 0
    def move(self):
            global hpd,e,levels,x_back
            self.u += 1
            self.x += 10
            if (levels == 3):
                HALLOWEEN_NIGHT.blit(gum_p[self.u//4%6],(self.x,self.y))
                if self.x > 1000:
                    gun_blist.remove(self)
                if 600 - self.x  < 10 and self.x - 600 > - 10  and y_dek-self.y < 20:
                    
                    if hpd > 0:   
                        hpd -= 1
                        if(hpd == 0 and levels == 3):
                            HALLOWEEN_NIGHT.blit(sdead_2[self.u//4%4],(self.x,self.y))
                            global i
                            i = 30
                            e = 10
                            x_back = 0
                            global p
                            p = 4
                            
                    gun_blist.remove(self)
            if (levels == 2):
                HALLOWEEN_NIGHT.blit(gun_r[self.u//4%6],(self.x,self.y))
                if self.x > 1000:
                    gun_blist.remove(self)
                if 600 - self.x  < 10 and self.x - 600 > - 10  and y_dek-self.y < 20:
                    if hpd > 0:   
                        hpd -= 1
                        if(hpd == 0 and levels == 2):
                            HALLOWEEN_NIGHT.blit(gum_p[self.u//4%6],(self.x,self.y))
                            e = 10
                            levels = 3
                            x_back = 0
                            
                    gun_blist.remove(self)
            if (levels == 1):
                HALLOWEEN_NIGHT.blit(gun_b[self.u//4%6],(self.x,self.y))
                if self.x > 1000:
                    gun_blist.remove(self)
                if 600 - self.x  < 10 and self.x - 600 > - 10  and y_dek-self.y < 20:
                    if hpd > 0:   
                        hpd -= 1
                        if(hpd == 0 and levels == 1): #เปลี่ยนด่านเมื่อบอสตาย
                            e = 10
                            levels = 2
                            x_back = 0
                          
                        
                    gun_blist.remove(self)

class gun_boss(object):
    def __init__(self,y):
        self.x = 650
        self.y = y
        self.u = 0
    def move(self):
            self.u += 1
            self.x -= 10
            global hp,levels
            if levels == 1:
                HALLOWEEN_NIGHT.blit(gunboss_1[self.u//4%5],(self.x,self.y))
            if levels == 2:
                HALLOWEEN_NIGHT.blit(gunboss_2[self.u//4%5],(self.x,self.y))
            if levels == 3:
                HALLOWEEN_NIGHT.blit(gunboss_3[self.u//4%5],(self.x,self.y-50))
            if self.x < -100 :
                gun_bosslist.remove(self)
            if self.x - 120 < 10 and self.x - 20 > - 10  and self.y - y_dek < 180:
                global hp,jidekna  #พลังชีวิตเด็กเมื่อชนเมื่อโดนพลังหมา
                if hp > 0:   
                    hp -= 1
                if jidekna < 10:
                    jidekna += 1
                gun_bosslist.remove(self)
            if(not bossis):
                gun_bosslist.remove(self)
            
class drawback(object):
    def __init__(self,choice):
        self.choice = choice
        
        if( self.choice == 1 ):
            
            self.y = 400
            self.x = random.randint(1100,1400)
        if( self.choice == 2 ):
            self.y = 405
            self.x = random.randint(1100,1400)
        if( self.choice == 3 ):
            self.y = 428
            self.x = random.randint(1100,1400)
    
    def move(self):
        
        self.x -= 5 #ความเร็วของการเลื่อนของสิ่งกีดขวาง
        if( self.choice == 1 ):
            HALLOWEEN_NIGHT.blit(drawback_1[0],(self.x,self.y))
        if( self.choice == 2 ):
            HALLOWEEN_NIGHT.blit(drawback_1[1],(self.x,self.y))
        if( self.choice == 3 ):
            HALLOWEEN_NIGHT.blit(drawback_1[2],(self.x,self.y))
            
        if self.x - 120 < 10 and self.x - 20 > - 10  and self.y - y_dek < 180:
            global hp,jidekna,score  #พลังชีวิตเด็กเมื่อชน
            if hp > 0:   
                hp -= 1
                if score > 0:
                    score -= 10
                if jidekna < 10:
                    jidekna += 1
            if hp == 0:
                dek_de_list.append(dek_de())
            drawbacklist.remove(self)
                  
          
class candy(object):
    def __init__(self,choice):
        self.choice = choice
        
        if( self.choice == 1 ):
            self.y = 180
            self.x = 1300
        if( self.choice == 2 ):
            self.y = 220
            self.x = 1300
        if( self.choice == 3 ):
            self.y = 240
            self.x = 1300
        if( self.choice == 4 ):
            self.y = 280
            self.x = 1300
    def move(self):
        self.x -= 3  #ความเร็วของการเลื่อนของลูกอม
        if( self.choice == 1 ):
            HALLOWEEN_NIGHT.blit(candy_1,(self.x,self.y))
        if( self.choice == 2 ):
            HALLOWEEN_NIGHT.blit(candy_1,(self.x,self.y))
        if( self.choice == 3 ):
            HALLOWEEN_NIGHT.blit(candy_1,(self.x,self.y))
        if( self.choice == 4 ):
            HALLOWEEN_NIGHT.blit(candy_1,(self.x,self.y))
        if self.x - 180 < 10 and x_dek - self.x < 10 and self.y - y_dek < 100 and y_dek - self.y < 50: #ลูกอมหายไป
            global score
            score += 20
            candylist.remove(self)
global p,x_back,e,i,score,hp,hpd,levels,attack,y_dek,x_dek,jidekna,jidna,drawbacklist,candylist,gun_bosslist,bosslist,bossis,dek_de_list,boss_de_lisy
game = True
while(game):
    p = 0
    crashed = False
    i = 0
    x_back = 0
    e = 4
    score = 0
    hp = 10
    levels = 1
    hpd = 6
    reload = 0
    attack = 0
    y_dek = 318
    x_dek = 80
    jidekna= 0
    jidna = 0
    up = False
    down = False   
    bossis = False
    drawbacklist = []
    candylist = []  
    bosslist = []
    gun_blist = []
    gun_bosslist = []
    dek_de_list = []
    boss_de_list = []
    
    while not crashed:
        i+=1
        if(attack > 0):
            attack-=1
        reload +=1
        play_game = pygame.key.get_pressed()
        if play_game[pygame.K_SPACE]:
            if p == 0:
                p = 1
                i = 0
        if play_game[pygame.K_UP] and reload >= 50 and bossis:
            if p == 2:
                reload = 0
                gun_blist.append(gun_dek(y_dek+100))
                
               
        if(i == 3000):
            i = 0

        if i % 300 == 0 and not bossis: #จำนวนสิ่งกีดขวางออกมา
            drawbacklist.append(drawback(random.choice([1,2,3])))
        if i % 100 == 0 and not bossis: #จำนวนลูกอม
            candylist.append(candy(random.choice([1,2,3,4])))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crashed = True
        if p == 0:

            HALLOWEEN_NIGHT.blit(play_im[(i//10)%4],(0,0))
            
        elif p == 1:
            
            if(i == 300):
                p = 2
            HALLOWEEN_NIGHT.blit(menu_game,(0,0))
        elif p == 2:
            if(levels == 1):
                HALLOWEEN_NIGHT.blit(station[0],(x_back,0))
            if(levels == 2):
                HALLOWEEN_NIGHT.blit(station[1],(x_back,0))
            if(levels == 3):
                HALLOWEEN_NIGHT.blit(station[2],(x_back,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            dek_j_go = pygame.key.get_pressed() 
            if dek_j_go[pygame.K_SPACE] : #เด็กกระโดด
                if y_dek == 318:      #ความเร็วกระโดด
                    up = True
            if( y_dek > 129 and up):
                y_dek -= 3
            if(up and y_dek == 129):
                down = True
                up = False
            if(down and y_dek <318):
                y_dek += 3
            if(down and y_dek == 318):
                down = False
                up = False

            
            if( not bossis):
                if(y_dek == 318):
                    HALLOWEEN_NIGHT.blit(dek_run[(i//10)%6],(50,y_dek))
                else:
                    HALLOWEEN_NIGHT.blit(dek_j[(i//40)%3],(50,y_dek))
            else:
                if(y_dek == 318):
                    HALLOWEEN_NIGHT.blit(dek_yrun,(50,y_dek))
                    
                else:
                    HALLOWEEN_NIGHT.blit(dek_j[(i//40)%3],(50,y_dek))
                if(i % 150 == 0):
                        gun_bosslist.append(gun_boss(400))
                        attack = 30
            
            if levels == 1 :
                x_back -= e
                if x_back == -7000:
                    x_back -= 1
                    i = 0
                    bosslist.append(bosse())
                    e = 0
                    bossis = True
                    hpd = 6
                    #HALLOWEEN_NIGHT.blit(boss_1[(i//10)%9],(1000,318))#สร้างบอสสสสส
            if levels == 2 :
                x_back -= e 
                if x_back == -10000:
                    x_back -= e
                    i = 0
                    bossis = True
                    bosslist.append(bosse())
                    hpd = 7
                    e = 0
            if levels == 3 :
                x_back -= e 
                if x_back == -13000:
                    x_back -= e
                    i = 0
                    bossis = True
                    bosslist.append(bosse())
                    hpd = 8
                    e = 0       
                


                
            for bosseiei in bosslist:
                bosseiei.move()
            for mon in drawbacklist:
                mon.move()
            for can in candylist:
                can.move()
            for gun__b in gun_blist:
                gun__b.move()
            for gun__boss in gun_bosslist:
                gun__boss.move()
            for boss__de in boss_de_list:
                boss__de.move()
            #for dek__de in dek_de_list:
                #dek__de.move()
            HALLOWEEN_NIGHT.blit(blooddek[jidekna],(20,20))
            text = font.render('Score: ' + str(score), 1, (0,0,0))
            HALLOWEEN_NIGHT.blit(text, (800, 20))
            if hp <= 0:
                p = 3
                i = 0
        if( p == 3 ):
                if(i < 40):
                    HALLOWEEN_NIGHT.blit(game_over_1[0],(0,0))
                if(i < 60 and i >=40):
                    HALLOWEEN_NIGHT.blit(game_over_1[1],(0,0))
                else:
                    HALLOWEEN_NIGHT.blit(game_over_1[2],(0,0))
                if(i > 100):
                    HALLOWEEN_NIGHT.blit(game_over_2[(i//8)%3],(0,0))
                if play_game[pygame.K_KP_ENTER]:
                    crashed = True
                   
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        crashed = True
                        game = False
        if (p == 4):
                
                if(i < 40):
                    HALLOWEEN_NIGHT.blit(game_win_1[0],(0,0))
                    i += 30
                if(i < 60 and i >=40):
                    HALLOWEEN_NIGHT.blit(game_win_1[1],(0,0))
                
                if(i > 100):
                    HALLOWEEN_NIGHT.blit(game_win_2[(i//8)%2],(0,0))
                text = font.render('Score: ' + str(score), 1, (0,0,0))
                HALLOWEEN_NIGHT.blit(text, (800, 20))
                
                if play_game[pygame.K_KP_ENTER]:
                    crashed = True
                   
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        crashed = True
                        game = False
                
            
        pygame.display.update()
        clock.tick(60)
    
pygame.quit()

