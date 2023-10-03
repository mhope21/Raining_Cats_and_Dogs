import pygame
import random
import math

from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background_day.png")

# Music
mixer.music.load('100116happybgm.ogg')
mixer.music.play(-1)

# Title
pygame.display.set_caption("It's Raining Cats and Dogs")

# Score and lives
score_value = 0
lives = 9
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 5
textY = 5

# Player
playerImg = pygame.image.load("character_femalePerson_show_bigger.png")
playerX = 370
playerY = 400
playerX_change = 0
speed = 6

# Poop that sticks
yuck_image = pygame.image.load("mud.png")

# Falling Objects
objectImg = []
objectX = []
objectY = []
objectY_change = []


num_of_cats = 2


for i in range(num_of_cats):
    objectImg.append(pygame.image.load("kitty.png"))
    objectX.append(random.randint(0, 736))
    objectY.append(random.randint(0, 25))
    objectY_change.append(0.3)
    #objectImg.append(pygame.image.load("kitty.png"))


# Falling Objects
objectDogImg = []
objectDogX = []
objectDogY = []
objectDogY_change = []


num_of_dogs = 2


for i in range(num_of_dogs):
    objectDogImg.append(pygame.image.load("Untitled-Artwork(3).png"))
    objectDogX.append(random.randint(0, 736))
    objectDogY.append(random.randint(0, 25))
    objectDogY_change.append(0.3)


# Falling Objects
objectPoopImg = []
objectPoopX = []
objectPoopY = []
objectPoopY_change = []


num_of_Poop = 2


for i in range(num_of_Poop):
    objectPoopImg.append(pygame.image.load("poop.png"))
    objectPoopX.append(random.randint(0, 736))
    objectPoopY.append(random.randint(0, 25))
    objectPoopY_change.append(0.5)



over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over():
    over_text = over_font.render("GAME OVER", True, (50, 50, 50))
    screen.blit(over_text, (200, 250))


def object_fall(x, y):
    screen.blit(objectImg[i], (x, y))


def object_Dog(x, y):
    screen.blit(objectDogImg[i], (x, y))


def object_Poop(x, y):
    screen.blit(objectPoopImg[i], (x, y))

def yuck(x, y):
    screen.blit(yuck_image, (x, y))
def player(x, y):
    screen.blit(playerImg, (x, y))

def collision(playerX, playerY, objectX, objectY):
    distance = math.sqrt((math.pow(playerX - objectX, 2)) + (math.pow(playerY - objectY, 2)))
    if distance < 50:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (50, 50, 50))
    lives_amount = font.render("Lives =" + str(lives), True, (50, 50, 50))
    screen.blit(score, (x, y))
    screen.blit(lives_amount, (x, y +30))



# Game Loop, keep game window open
running = True
while running:
    screen.fill((2, 2, 2))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = - speed

        if event.key == pygame.K_RIGHT:
            playerX_change = speed

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= -10:
        playerX = -10
    elif playerX >= 680:
        playerX = 680

    for i in range(num_of_cats):
        objectY[i] += objectY_change[i]

        if objectY[i] > 600:
            objectY[i] = random.randint(0, 25)
            objectX[i] = random.randint(0, 736)
            lives -= 1

        elif lives <= 0:
            lives = 0
            game_over()
            break

    for i in range(num_of_dogs):
        objectDogY[i] += objectDogY_change[i]

        if objectDogY[i] > 600:
            objectDogY[i] = random.randint(0, 25)
            objectDogX[i] = random.randint(0, 736)
            lives -= 1

        elif lives <= 0:
            lives = 0
            game_over()
            break

    for i in range(num_of_Poop):
        objectPoopY[i] += objectPoopY_change[i]

        if objectPoopY[i] > 600:
            objectPoopY[i] = random.randint(0, 25)
            objectPoopX[i] = random.randint(0, 736)

        elif lives <= 0:
            lives = 0
            game_over()

            break


        catch = collision(playerX, playerY, objectX[i], objectY[i])
        if catch:
            hit_sound = mixer.Sound('Meow.ogg')
            hit_sound.play()
            score_value += 1
            objectY[i] = random.randint(0, 25)
            objectX[i] = random.randint(0, 736)
            objectY_change[i] = objectY_change[i] + 0.01

        object_fall(objectX[i], objectY[i])

        gotcha = collision(playerX, playerY, objectDogX[i], objectDogY[i])
        if gotcha:
            touch_sound = mixer.Sound('dogbark.wav')
            touch_sound.play()
            score_value += 1
            objectDogY[i] = random.randint(0, 25)
            objectDogX[i] = random.randint(0, 736)
            objectDogY_change[i] = objectDogY_change[i] + 0.01

        object_Dog(objectDogX[i], objectDogY[i])

        ewwGross = collision(playerX, playerY, objectPoopX[i], objectPoopY[i])
        if ewwGross:
            splat_sound = mixer.Sound('slime_jump.wav')
            splat_sound.play()
            score_value -= 1
            objectPoopY[i] = random.randint(0, 25)
            objectPoopX[i] = random.randint(0, 736)
            speed = speed - 0.2

        object_Poop(objectPoopX[i], objectPoopY[i])

    show_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update()