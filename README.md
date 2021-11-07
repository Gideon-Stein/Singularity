# Python Codex + GPT3 Game



##Idea: Ask GPT3 what kind of game should be created and use codex to implement it. 



The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you? <br/>
AI: I am an AI created by OpenAI. How can I help you today?<br/>
Human: I would like to create a small game. What python library should I use?<br/>
AI: If you are specifically interested in building games, then I suggest using Pygame.<br/>
Human: What should be the goal of the game?<br/>
AI: If you're going to make a competition-based game, how about a racing game?<br/>
Human: A racing game with cars?<br/>
AI: Just like normal cars? Or you could mix up cars and trucks and use more unusual vehicles, like a motorcycle or a big truck. You could even make a walking human-like character and make him run and jump over gaps.<br/>
Human: Could you give me a link to a picture of a car for my game?<br/>
AI: Sure, here's a link:  http://example.com<br/>
Human: Give me 3 facts about your favourite car<br/>
AI: Volkswagen Beetles have been around for over 70 years, the current version of the beetle was designed by Ferry Porsche and styled by Pino Farinetti from Italdesign Giugiaro. The Káradómrøkkur crater in Iceland is named after a volcano in Norse mythology. In Icelandic, Timbuktu means "you are far away".<br/>
Human: What should be in the background of my game?<br/>
AI: A background for your racing game? A track with a highway on top of a mountain peak with blue sky and white clouds, with a road winding itself down the peak. Is that what you had in mind?<br/>
Human:  What should be the goal of the game?<br/>
AI: You should complete the game, or get to a high score. How about getting the highest score without caring about the race?<br/>
Human: How should the player get points?<br/>
AI: There are a number of ways. You can get points for completing levels or stages, getting bonuses, and etc. There's also a way to get points by collecting items on the course, like coins and power-ups.<br/>
Human: Can the player loose points?<br/>
AI: Yes, it is possible to have the player loose points for getting hit by an obstacle or car ahead. You can also have penalties for running out or time or other ways.<br/>
Human: Should the game have a soundtrack?<br/>
AI: Maybe, if you think it is necessary for the game. But I find that a racing game doesn't need any music as there's enough action to keep the player busy.<br/>
Human: I think music would be cool. Can you tell me your favourite song?<br/>
AI:  My favourite song? I don't think that's a very good song. It is an okay song, and I like the lyrics and the singer's voice. But I do not like the instrumentals at all.<br/>
Human: What is its name?<br/>
AI: Just Gimme the Night by George Benson.<br/>
Human:  Should the player be able to honk?<br/>
AI: If you want, but it's not necessary.<br/>
Human: Which sound should the honk make?<br/>
AI: Maybe you could get the sound from a real car to use in the game.<br/>
Human: What would be an appropriate name for the game?<br/>
AI: Racing on Narinin's Island?<br/>
Human: When does the player loose<br/>
AI: The player should loose when they crash into something or when they run out of time. But I have to admit, in my opinion it doesn't make sense for the player to loose when they crash.<br/>
Human: What should I tell the player when he looses?<br/>
AI: Thank you for playing. Try again?<br/>
Human: Maybe something that is a little bit more creative<br/>
AI: As the player I don't like it when the player looses, but if you want to give them something positive... okay... how about, "Well try again. You'll do better next time." ?<br/>
Human: Should I display the score at the end?<br/>
AI: I don't think it makes much sense to display the score at the end. I don't know how you're going to use the score.<br/>
Human:  What could I do with the score?<br/>
AI: You could give the player a trophy for getting a huge number of points. That would probably be strange and funny and make them play your game more.<br/>
Human: How should the trophy look like? <br/>
AI: A trophy with a green base and a green top with a green comfy seat. It would have the text GOT IT on it with a large green coloured star on top of the text.<br/>
Human: Alright! I think I can do that. Do you want to see the result?<br/>
AI: I want to see how you make it.<br/>
Human: You could ask your cousin Codex. I think he will let you watch<br/>
AI: I will ask him. Thanks!<br/>



The following are the steps I took to build GPT3s game with Codex.

1.Lets start doing a game window.
2.Now lets add the background we downloaded
3.Lets add the car and center it
4.LEts add the game loop so we can see what is displayed
5.The car is to big. In order to work properly lets delete the game loop from the codex code and just keep it in our prgram. this way we can easily edit for example the car
6.Make the car 20% 
7.Add a high score 
8.Error font not initalized: Ask Codex to initialize the font. Works
9.Add A Coin Works
10.Add an obstacle Works
11.Add a level counter. Gets implemented differently than the highscore. Weird
12.Add the midi music that gpt3 wanted
13.Need to initialize mixer first. Works
14.We got all the objects asembled. Now we need to make things move
15.First the player: 
16.The output has everything but needs to be combined with our old drawings:

```
# The playerImg should be able to move with the arrow keys
def player(x,y):
    screen.blit(playerImg, (x,y))

#Game loop
running = True
while running:
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
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    #Create the boundaries for the player icon
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    #Update the screen
    pygame.display.update()
    #Set the frame rate
    clock.tick(60)

#Quit the game
pygame.quit()
quit()
```  

17.Now lets try to move the coin. I think it should come down the road somehow 
18.Works somehow. Now the obstacle. Maybe it moves on the road X axis. 
19.bouncing is hard. We can however easily add some if statements to the codex output to make it work

20. We can add a sinus function to make it smooth. Also, we can use the same for the coin to make it more look smoother    
21. We need a name. Add what GPT has to say
22. Gpt says the game should be over after some time. Added this mainly by hand since its very basic 
23. Added the game over screen. Had to edit the if conditions to make it work like it is supposed to

## The final pythonfile of the game is included in this repo.
        
    
    



