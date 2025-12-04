import random
import sys
import pygame
from pygame.locals import *

FPS=30 
screenwidth= 290
screenheight= 511
screen= pygame.display.set_mode((screenwidth,screenheight))
groundy= screenheight* 0.8
game_sprites={}
game_audio={}
player= 'sprites/bird.png'
pipe= 'sprites/pipe-green.png'
background= 'sprites/background-night.png'

def welcomescreen():
    playex=int(screenwidth/5)
    playery=int((screenheight - game_sprites['player'].get_height())/1.99)
    messagex=int((screenwidth - game_sprites['message'].get_width())/2)
    messagey=int((screenheight*0.13))
    basex=0

    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_SPACE):
                pygame.quit()
                sys.exit()                
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return 
            else:
                screen.blit(game_sprites['background'],(0,0))
                screen.blit(game_sprites['player'],(playex,playery))
                screen.blit(game_sprites['message'],(messagex,messagey))
                screen.blit(game_sprites['base'],(basex,groundy))
                pygame.display.update()
                fpsclock.tick(FPS)
    
def maingame():
    score=0
    playerx= int(screenwidth/5)
    playery= int(screenwidth/2)
    basex= 0
    newpipe1= getrandompipe()
    newpipe2= getrandompipe()

    upperpipes=[
        {'x':screenwidth+200, 'y':newpipe1[0]['y']},
        {'x':screenwidth+200+ (screenwidth/2), 'y':newpipe2[0]['y']},
    ]
    lowepipes=[
        {'x':screenwidth+200, 'y':newpipe1[1]['y']},
        {'x':screenwidth+200+ (screenwidth/2), 'y':newpipe2[1]['y']},
    ]

    pipevelx= -4
    playervaly= 9
    playermaxvaly= 10
    playerminvaly= -8
    playeraccy= 1
    playerflapaccv= -8
    playerflapped= False

    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()                
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                playervaly= playerflapaccv
                playerflapped= True
                game_audio['wing'].play()

        crashtest= isCollide(playerx,playery,upperpipes,lowepipes)
        if crashtest:
            return
        
        playermidpos= playerx+ game_sprites['player'].get_width()/2
        for pipe in upperpipes:
            pipemidpos= pipe['x']+game_sprites['pipe'][0].get_width()/2
            if pipemidpos<= playermidpos < pipemidpos+4:
                score+=1
                print(f"your score is {score}")
                game_audio['point'].play()

        if playervaly< playermaxvaly and not playerflapped:
            playervaly+=playeraccy

        if playerflapped:
            playerflapped= False
        playerheight= game_sprites['player'].get_height()
        playery= playery+min(playervaly,groundy-playery-playerheight)

        for upipe, lpipe in zip(upperpipes, lowepipes):
            upipe['x'] += pipevelx
            lpipe['x'] += pipevelx


        if 0<upperpipes[0]['x']<5:
            newpipe= getrandompipe()
            upperpipes.append(newpipe[0])
            lowepipes.append(newpipe[1])

        if upperpipes[0]['x']< -game_sprites['pipe'][0].get_width():
            upperpipes.pop(0)
            lowepipes.pop(0)

        screen.blit(game_sprites['background'],(0,0))
        for upipe, lpipe in zip(upperpipes, lowepipes):
            screen.blit(game_sprites['pipe'][0], (upipe['x'], upipe['y']))
            screen.blit(game_sprites['pipe'][1], (lpipe['x'], lpipe['y']))

        screen.blit(game_sprites['base'],(basex,groundy))
        screen.blit(game_sprites['player'],(playerx,playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += game_sprites['numbers'][digit].get_width()
        Xoffset = (screenwidth - width)/2

        for digit in myDigits:
            screen.blit(game_sprites['numbers'][digit], (Xoffset, screenheight*0.12))
            Xoffset += game_sprites['numbers'][digit].get_width()
        pygame.display.update()
        fpsclock.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> groundy - 25  or playery<0:
        game_audio['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = game_sprites['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < game_sprites['pipe'][0].get_width()):
            game_audio['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + game_sprites['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < game_sprites['pipe'][0].get_width():
            game_audio['hit'].play()
            return True
    return False

def getrandompipe():
    pipeHeight = game_sprites['pipe'][0].get_height()
    offset = screenheight/3
    y2 = offset + random.randrange(0, int(screenheight - game_sprites['base'].get_height()  - 1.2 *offset))
    pipeX = screenwidth + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe

if __name__=="__main__":
    pygame.init()
    fpsclock= pygame.time.Clock()
    pygame.display.set_caption("flappy bird maze karo bhai")
    game_sprites['numbers']=(
        pygame.image.load('sprites/0.png').convert_alpha(),
        pygame.image.load('sprites/1.png').convert_alpha(),
        pygame.image.load('sprites/2.png').convert_alpha(),
        pygame.image.load('sprites/3.png').convert_alpha(),
        pygame.image.load('sprites/4.png').convert_alpha(),
        pygame.image.load('sprites/4.png').convert_alpha(),
        pygame.image.load('sprites/5.png').convert_alpha(),
        pygame.image.load('sprites/6.png').convert_alpha(),
        pygame.image.load('sprites/7.png').convert_alpha(),
        pygame.image.load('sprites/8.png').convert_alpha(),
        pygame.image.load('sprites/9.png').convert_alpha(),
    )
    game_sprites['message']= pygame.image.load('sprites/message.png')
    game_sprites['base']= pygame.image.load('sprites/base.png')
    game_sprites['pipe']= (
        pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180),
        pygame.image.load(pipe).convert_alpha(),
    )

    game_audio['die']= pygame.mixer.Sound('audio/die.wav')
    game_audio['hit']= pygame.mixer.Sound('audio/hit.ogg')
    game_audio['point']= pygame.mixer.Sound('audio/point.wav')
    game_audio['swoosh']= pygame.mixer.Sound('audio/swoosh.ogg')
    game_audio['wing']= pygame.mixer.Sound('audio/wing.wav')
    
    game_sprites['background']= pygame.image.load(background).convert()
    game_sprites['player']= pygame.image.load(player).convert_alpha()

    while True:
        welcomescreen()
        maingame()