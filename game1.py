import pygame
import random
import  math

pygame.init()

screen=pygame.display.set_mode((800,600))

background = pygame.image.load('abcd.png')

#for icon
pygame.display.set_caption("Space War")
icon = pygame.image.load('ufo1.png')
pygame.display.set_icon(icon)



playerImg =pygame.image.load('jet.png')
playerX=370
playerY=480
playerX_change=0
playerY_change=0

#ENEMY


enemyImg =pygame.image.load('ufo.png')
enemyX= random.randint(0,735)
enemyY= random.randint(50,150)
enemyX_change=3
enemyY_change=40

enemyImg2 =pygame.image.load('ufo.png')
enemyX2= random.randint(0,735)
enemyY2= random.randint(50,150)
enemyX2_change=3
enemyY2_change=40

enemyImg3 =pygame.image.load('ufo3.png')
enemyX3= random.randint(0,735)
enemyY3= random.randint(50,150)
enemyX3_change=4
enemyY3_change=40




#ready we can not see missile
#fire missile is out
bulletImg =pygame.image.load('missile.png')
bulletX= 0
bulletY= 480
bulletX_change=0
bulletY_change=10
bullet_state="ready"


#score
score_value =0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(x,y):
    score =font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))

#blit maens draw
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def enemy2(x,y):
    screen.blit(enemyImg2,(x,y))

def enemy3(x,y):
    screen.blit(enemyImg3,(x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return  False

def iscollision2(enemyX2,enemyY2,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX2-bulletX,2))+(math.pow(enemyY2-bulletY,2)))
    if distance<27:
        return True
    else:
        return  False


def iscollision3(enemyX3,enemyY3,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX3-bulletX,2))+(math.pow(enemyY3-bulletY,2)))
    if distance<27:
        return True
    else:
        return  False


running = True
while running:
    screen.fill((0, 0, 0))#RGB
    #background image

    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if we press arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0



# end line mate boudry
    playerX+=playerX_change

    if playerX <=0:
        playerX=0
    elif playerX >737:
        playerX =736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX > 737:
        enemyX_change = -3
        enemyY += enemyY_change

    enemyX2 += enemyX2_change

    if enemyX2<= 0:
        enemyX2_change = 3
        enemyY2 += enemyY2_change
    elif enemyX2> 737:
        enemyX2_change = -3
        enemyY2 += enemyY2_change

    enemyX3 += enemyX3_change

    if enemyX3 <= 0:
        enemyX3_change = 3
        enemyY3 += enemyY3_change
    elif enemyX3 > 737:
        enemyX3_change = -3
        enemyY3 += enemyY3_change

    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state is "fire":

        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

#hit bullet and score

    collision =iscollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY=480
        score_value +=1

        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)

    collision2 = iscollision2(enemyX2, enemyY2, bulletX, bulletY)
    if collision2:
        bulletY = 480
        score_value += 1

        enemyX2 = random.randint(0, 800)
        enemyY2 = random.randint(50, 150)

    collision2 = iscollision2(enemyX3, enemyY3, bulletX, bulletY)
    if collision2:
        bulletY = 480
        score_value += 3

        enemyX3 = random.randint(0, 800)
        enemyY3 = random.randint(50, 150)

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    enemy2(enemyX2, enemyY2)
    enemy3(enemyX3, enemyY3)

    show_score(textX,textY)
    pygame.display.update()




