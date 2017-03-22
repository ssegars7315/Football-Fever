from gamelib import *

game = Game(800,600,"Football Fever",60)
game.setMusic("sounds\\Football Crowd.wav")
bk = Image("images\\footballfield.jpg",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

startscreen = Image("images\\instructions.png",game)
startscreen.resizeTo(game.width, game.height)



player2 = []

for times in range(50):
    player2.append( Image("images\\player2.gif",game))
    

for p in player2:
    x = randint(1000,10000)
    y = randint(100,500)
    s = randint(1,3)
    p.moveTo(x,y)
    p.setSpeed(s,90)
    p.resizeBy(-50)

Powerup = []

for times in range(30):
    Powerup.append( Image("images\\gatorade.png", game))

for power in Powerup:
    x = randint(1000,10000)
    y = randint(150,500)
    s = randint(1,3)
    power.moveTo(x,y)
    power.setSpeed(s,90)
    power.resizeBy(-70)

Coin = []

for times in range(30):
    Coin.append(  Image("images\\coin.gif", game))

for c in Coin:
    x = randint(1000,10000)
    y = randint(200,550)
    s = randint(1,3)
    c.moveTo(x,y)
    c.setSpeed(s,90)
    c.resizeBy(-70)


Player1 = Image("images\\player1.gif",game)
Player1.resizeBy(-50)
Player1.moveTo(game.width/2, game.height - 100)



drink = Sound("sounds\\slurping.wav",1)
punch = Sound("sounds\\punching.wav",2)
tone = Sound("sounds\\tone.wav",3)

#Instructions Screen
while not game.over:
    game.processInput()
    startscreen.draw()
    game.update()
    game.wait(K_SPACE)
    
    game.drawText("Football Fever",game.width/4,game.height/4,Font(green,90,yellow))
    game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(60)


game.over = False

#Start Screen
while not game.over:
    game.processInput()
    game.drawBackground()
    game.drawText("Football Fever",game.width/4,game.height/4,Font(green,90,yellow))
    game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
    game.update()
    game.wait(K_SPACE) 
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(60)


game.over = False

#Main Game
while not game.over:
    game.processInput()

    bk.draw()
    Player1.move()
   

    for p in player2:
        p.move()
        if p.collidedWith(Player1):
            Player1.health-= 20
            punch.play()
            p.visible = False
            
            

    for power in Powerup:
        power.move()
        if Player1.collidedWith(power):
            Player1.health+= 10
            power.visible = False
            drink.play()

    for c in Coin:
        c.move()
        if Player1.collidedWith(c):
            game.score+=10
            c.visible = False
            tone.play()


    if Player1.x>=350 and Player1.x <=450 and Player1.y>=100 and Player1.y<=200:
        game.score+=20
        Player1.moveTo(game.width/2, game.height - 100)
        
        
        
        
            
            
    if keys.Pressed[K_UP]:
        Player1.y-= 3

    if keys.Pressed[K_DOWN]:
        Player1.y += 3

    if keys.Pressed[K_LEFT]:
        Player1.x-= 3

    if keys.Pressed[K_RIGHT]:
        Player1.x+= 3

    if game.time <= 0:
        game.over = True

    if Player1.health<0:
        game.over = True

        

        
    game.displayTime(300,5)
    game.drawText("Health: " + str(Player1.health),155,5)            
    game.displayScore()
    game.update(60)
game.drawText("Game Over",game.width/4,game.height/4,Font(green,90,yellow))
game.playMusic()
game.drawText("Press [SPACE] to Exit",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_SPACE)
game.quit()
