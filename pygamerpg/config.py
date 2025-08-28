#Settings
import pygame
import sys
import random
import time
pygame.init()
win_width=800
win_height=500
FPS=60
title="Game"
timer=15

#battle -player
player_hp=100
player_str=2
player_def=3
player_stamina=100
player_mp=50
player_lvl=1
money=100
player_battlebag=['H POTION','M POTION','S POTION']
player_equip={"weapon":"ASS","armour":"NONE","scroll":"LIGHTNING"}
player_attack1=['PUNCH','KICK','KNEE','SLAP','STRIKE','UPPERCUT','SMASH','ELBOW','LOW KICK','SIDEKICK']
player_attack2=['TAKEDOWN','BODY SLAM','DROP KICK','ROUNDHOUSE','SUPLEX']
player_inventory=['SWORD','SILVER SET','BRONZE SET','AXE','LIGHTNING','FIRE','DAGGER','GOLD SET']
all_items=['SWORD','SILVER SET','BRONZE SET','AXE','LIGHTNING','FIRE','DAGGER','GOLD SET','H POTION','M POTION','S POTION','WATER']
fire=["IN DARKNESS YOU BURN EVER SO BRIGHT","BOUNDLESS LIGHT NO END IN SIGHT","I KNEEL BEFORE YOUR GREAT MIGHT","O AGNI HEED MY SOULS DESIRE","CONSUME MY FOES WITH YOUR HEAVENLY FIRE"]
lightning=["IN DARKEND CLOUDS YOU HIDE","POWERS THAT STRIKE DOWN WITH PRIDE","CUT AND BURN EVERYTHING IN ITS STRIDE","O INDRA LEND ME YOUR BOLT","SHOW THEM THE POWER OF THE KILOVOLT"]
curse=["SPELL FOR CURSE","NEED FIVE LINES","COSTS PLAYER HEALTH","KILL OR HURT OR PARALYZE OPPONENT"]
plague=["SPELL FOR PLAGUE","DEALS POISON DAMAGE"]
earth=["RISE FROM YOUR SILENT LULL","SHIELD ME FROM ALL EVIL YOU SHALL","QUAKE THE LANDS WITH A POWERFULL SUNDER","O PRITHVI HEAR MY DIRE INVOCATION","TO BURRY MY FOES SIX FEET UNDER"]
water=["IN BATTLE I STAND","COVERED IN WOUNDS TORMENTED BY PAIN","MY WILL STANDS STRONG MY MIND REMAINS SANE","VARUNA I SUMMON ASSISTANCE ","FILL MY SOUL AGAIN WITH LIFES ESSENCE"]
guild='lightning'
glist=['FIRE','WATER','EARTH','LIGHTNING']
#monster



#fuctions for all
def drawtext(screen,font,text,color,size,alph,pos,angle=0):
    font=pygame.font.Font(font,size)
    text_surface=font.render(text,True,color)
    text_surface.set_alpha(alph)
    text_rect=text_surface.get_rect()
    text_rotate=pygame.transform.rotate(text_surface, angle)
    text_rect.x=pos[0]
    text_rect.y=pos[1]
    screen.blit(text_rotate,text_rect)

flag=index=alph=tempy=lock=-1
def typing(game,screen,font,words,length,posx,posy,inputtext,size=60,angle=[]):
    global flag,index,alph,tempy,lock,angles,err
    if game.input_text=='':
        flag=index=alph=tempy=lock=-1  
    inputtext=inputtext.upper()
    length=len(inputtext)
    for word in words:
        if inputtext==word[:length] and length>0:
            index=words.index(word)
            flag=1
            break
        elif flag!=1:
            flag=0
    try:
        if flag==1 and inputtext==words[index][:length]:
            game.battle.error=2
            if not angle:
                drawtext(screen,font,inputtext,'white',size,255,(posx[index],posy[index]),0)
            else:
                drawtext(screen,font,inputtext,'white',size,255,(posx[index],posy[index]),angle[index])
            alph=255
            tempy=posy[index]
        elif flag==1 and inputtext!=words[index][:length] and game.typeerror==1:
            if game.battle.error!=0:
                game.battle.error=1
            if lock==-1:
                lock=len(inputtext)
            if not angle:
                drawtext(screen,font,inputtext,'white',size,alph,(posx[index],tempy),0)
            if angle:
                drawtext(screen,font,inputtext,'white',size,alph,(posx[index],tempy),angle[index])
            if alph<=0:
                flag=index=alph=tempy=lock=-1  
                tempword=''
                game.input_text=''
                inputtext=''
                game.typeerror=1
            else:
                alph-=10
                tempy+=1
        elif flag==0:
            flag=index=alph=tempy=lock=-1  
            game.input_text=''
            inputtext=''
            game.typeerror=1
    except Exception as e:
        print("The error is: ",e ,index)

def typingsingle(game,screen,font,words,length,posx,posy,inputtext,size=60,angle=[]):
    global flag,index,alph,tempy,lock,angles,err
    if game.input_text=='':
        flag=index=alph=tempy=lock=-1  
    inputtext=inputtext.upper()
    length=len(inputtext)
    try:
        if game.attack==2:
            game.battle.error=0
            drawtext(screen,font,inputtext,'white',size,255,(posx,posy),0)
            alph=255    
            if inputtext!=words[:length]:
                game.input_text= game.input_text[:-1]
                game.action.spellmistake+=1
        elif inputtext==words[:length]:
            flag=1
            game.battle.error=2
            if not angle:
                drawtext(screen,font,inputtext,'white',size,255,(posx,posy),0)
            else:
                drawtext(screen,font,inputtext,'white',size,255,(posx,posy),angle)
            alph=255
            tempy=posy
        elif flag==1 and inputtext!=words[:length] and game.typeerror==1:
            if game.battle.error!=0:
                game.battle.error=1
            if lock==-1:
                lock=len(inputtext)
            if not angle:
                drawtext(screen,font,inputtext,'white',size,alph,(posx,tempy),0)
            if angle:
                drawtext(screen,font,inputtext,'white',size,alph,(posx,tempy),angle)
            if alph<=0:
                flag=index=alph=tempy=lock=-1  
                tempword=''
                game.input_text=''
                inputtext=''
                game.typeerror=1
            else:
                alph-=10
                tempy+=1
        elif flag==-1:
            flag=index=alph=tempy=lock=-1  
            game.input_text=''
            inputtext=''
            game.typeerror=1
    except Exception as e:
        print("The error is: ",e ,index)

def info(game,screen,font,hp,mp,stamina):
    drawtext(screen,font,'HEALTH : '+str(hp),'white',30,255,(200,200))
    drawtext(screen,font,'MANA : '+str(mp),'white',30,255,(200,215))
    drawtext(screen,font,'STAMINA : '+str(stamina),'white',30,255,(200,230))
    drawtext(screen,font,'WEAPON : '+str(player_equip["weapon"]),'white',40,255,(300,220))
    drawtext(screen,font,'ARMOUR : '+str(player_equip["armour"]),'white',40,255,(300,240))
    drawtext(screen,font,'SCROLL : '+str(player_equip["scroll"]),'white',40,255,(300,260))

def itemuse(game,screen,ch):
    if ch.upper()=='H POTION':
        game.battle.ran=50
        game.battle.hp+=50
        if game.battle.hp>player_hp:
            game.battle.hp=player_hp
    if ch.upper()=='M POTION':
        game.battle.ran=random.randint(25,45)
        game.battle.mp+=game.battle.ran
        if game.battle.mp>player_mp:
            game.battle.mp=player_mp
    if ch.upper()=='S POTION':
        game.battle.ran=random.randint(55, 75)
        game.battle.stamina+=game.battle.ran
        if game.battle.stamina>player_stamina:
            game.battle.stamina=player_stamina
def remove(item):
    player_battlebag.remove(item)
def changeequip(item,value):
    player_equip[item]=value;

def drawmultiple(screen,font,text,color,size,alph,posx,posy):
    if not isinstance(size, list):
        size = [size] * len(text)
    if not isinstance(alph, list):
        alph = [alph] * len(text)
    for index, x in enumerate(text):
        drawtext(screen,font,x,color,size[index],alph[index],(posx[index],posy[index]))
 
def inventory(action,item1,item2):
    if action==1:#exchange item from player equip and inventory
        player_inventory.remove(item2)
        if player_equip[item1]!='NONE':
            player_inventory.append(player_equip[item1])
        player_equip[item1]=item2
    if action==2: #if inventory full exchange item with other
        player_inventory.remove(item2)
        player_inventory.append(item1)
    if action==3: #add item to inventory
        player_inventory.append(item1)
    if action==4: #remove an item
        player_inventory.remove(item1)