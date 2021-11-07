import pygame
import random
import numpy as np
import math

#Create a pygame window
screen = pygame.display.set_mode((800,600))

#Set the title of the window
pygame.display.set_caption("Racing on Narinin's Island")

#Set the game's clock
clock = pygame.time.Clock()

##Added this 
direction = 1
gameSpeed = 1

#Put the picture src/background.jpg as the background of the window
background = pygame.image.load('src/background.jpg')

#Put the picture "src/eth.png" as coin icon in the middle of the screen
coinImg = pygame.image.load('src/eth.png')
coinX = 450
coinY = 300

#Put the picture "src/obstacle.png" at the top of the screen
obstacleImg = pygame.image.load('src/obstacle.png')
obstacleX = 200 #changed from 0 
obstacleY = 300 # changed from -600


#Define the score and display it in the top left corner
score = 0
scoreX = 10
scoreY = 10

# Draw the score value on the screen
def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))
    
#Initialize the pygame font
pygame.font.init()

# Define the font
font = pygame.font.Font('src/freesansbold.ttf', 32)
    
#Put the picture "src/player.png" as player icon in the center of the screen
playerImg = pygame.image.load('src/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Load the picture "src/trophy.png"
trophy = pygame.image.load("src/trophy.png")


#Define the time and display it in the top right corner
time = 60
timeX = 500 # changed from 700
timeY = 10   # changed from 50

#Make the car 20% of its size
playerImg = pygame.transform.scale(playerImg, (int(playerImg.get_width()/5), int(playerImg.get_height()/5)))
#Make the obstacle 10% of its size
obstacleImg = pygame.transform.scale(obstacleImg, (int(obstacleImg.get_width()/10), int(obstacleImg.get_height()/10)))
#Make the coin 10% of its size
coinImg = pygame.transform.scale(coinImg, (int(coinImg.get_width()/10), int(coinImg.get_height()/10)))


# initialize the pygame mixer
pygame.mixer.init()

# load the song "src/sountrack.mid" and play it in the background
pygame.mixer.music.load('src/soundtrack.mid')
pygame.mixer.music.play(-1)

#load the sound "src/effect.wav"
effect = pygame.mixer.Sound('src/effect.wav')


# Create a function that randomly changes the coinX according to a sinus function and adds one to coinY
def coin_movement():
    global coinX, coinY, gameSpeed
    coinX = 450 + math.sin(coinY/10)*100
    coinY += gameSpeed
    
# Create a function that checks if the Yposition of coinImg is over 500. If yes set the Y position to 300
def coin_reset():
    global coinY
    global coinX
    if coinY > 600: #changed from 500
        coinY = 300
        coinX = 450
        
        
        
# a function that returns the value of sinus at x with a period of 800 and a mean of 1 
## had to edit here a little
def sinus(x):
    return 1 +  np.sin(x / 400 * 2 * np.pi)

        
## Add that the center is used rather than the top right corner
# Create a function that checks if the player icon and the coin icon collide
def is_collision(playerX, playerY, coinX, coinY):
    distance = math.sqrt((math.pow(playerX - coinX, 2)) + (math.pow(playerY - coinY, 2)))
    if distance < 40: # changed from 27
        return True
    else:
        return False
    
    

# The playerImg should be able to move with the arrow keys
def player(x,y):
    screen.blit(playerImg, (x,y))

def obstacle_movement():
    global direction
    global obstacleX
    global obstacleY
    obstacleX += 2 * direction * gameSpeed ##Added here a scaling
    if obstacleX > 736:
        direction = -1
    if obstacleX < 0:
        direction = 1
    ## Add the obstacleY here had to do that myself
    obstacleY = sinus(obstacleX) * 100 + 400

# Get the current time
current_time = pygame.time.get_ticks()

#check how many seconds have passed between current_time and now
def time_check(current_time):
    return pygame.time.get_ticks() - current_time

#if time is 0, the screen should be black
    #if time is 0, the game should be over
def game_over():
    # Added the BG to make it look better
    screen.blit(background, (0,0))
    font = pygame.font.Font('src/freesansbold.ttf', 24)
    ## Added a condition with win
    if score < 100:
        text = font.render("Well try again. You'll do better next time. - GPT3", True, (0,0,0)) #Added the text here from GPT3
    else:
        text = font.render("YOU WIN. Here is the trophy GPT3 wanted you to have", True, (0,0,0)) #Added the text here from GPT3
        screen.blit(trophy, (400, 300))

    screen.blit(text, (100, 150))

# check if the player pressed spacebar
def check_space(event):
    if event.type == pygame.KEYDOWN:
        print(event.key)
        if event.key == pygame.K_SPACE:
            print("here")
            return True
    return False

    
#Game loop
running = True
while running:
    ## added the condition here
    if time > 0: 
        #Set the background color of the window
        screen.fill((0,0,0))
        #Set the background image
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #If the keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -2.5   # changed this here from -0.3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2.5
                ## Lets add some up and down movement aswell
                if event.key == pygame.K_UP:
                    playerY_change = -2.5
                if event.key == pygame.K_DOWN:
                    playerY_change = 2.5
                ## Added this part from a codex function
                if event.key == pygame.K_SPACE:
                    print("Honk!")
                    effect.play()

                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                # Add again  
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0
        playerX += playerX_change
        # Add here again
        playerY += playerY_change
        
        ##  Ive build that in here
        timer = time_check(current_time)
        time = 60 - int(timer / 1000)
        
            
            
        #Create the boundaries for the player icon
        if playerX <= 0:
            playerX = 0
        elif playerX >= 700:  # changed this here from 736
            playerX = 700
        ##Add the same again foor the up down
        if playerY <= 425:
            playerY = 425
        elif playerY >= 500:  # changed this here from 736
            playerY = 500
        player(playerX, playerY)
        
        # Get the coordinates of the center of playerImg
        playerX_center = playerX + (playerImg.get_width()/2)
        playerY_center = playerY + (playerImg.get_height()/2)
        
        ## Do the same for the obstacle and the coin
        coinX_center = coinX + (playerImg.get_width()/2)
        coinY_center = coinY + (playerImg.get_height()/2)        
        obstacleX_center = obstacleX + (playerImg.get_width()/2)
        obstacleY_center = obstacleY + (playerImg.get_height()/2)
        
        ##Aded to check with codex collision function
        if is_collision(playerX_center, playerY_center, coinX_center, coinY_center):
            score +=1
        ## We can copy the function for the obstacle

        if is_collision(playerX_center, playerY_center, obstacleX_center, obstacleY_center):
            score -=1
        
        ## Added the function from Codex here
        coin_movement()
        coin_reset()
        obstacle_movement()
        ##Added this part from earlier
        #Draw the current timer on the screen
        timer_text = font.render("Seconds left: " + str(time), True, (255,255,255))
        ##Added by hand based on the highscore function
        screen.blit(timer_text, (timeX, timeY))
        ## added by hand
        screen.blit(coinImg, (coinX, coinY))
        screen.blit(obstacleImg, (obstacleX, obstacleY))
        show_score(scoreX, scoreY)

    else:
        game_over()


    #Update the screen
    pygame.display.update()
    #Set the frame rate
    clock.tick(60)
