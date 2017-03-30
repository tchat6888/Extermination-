from gamelib import *

game = Game(800,600,"Extermination", 60)
bk = Image("images//CityBG.gif",game)
game.setBackground(bk)
bk.resizeTo(game.width,game.height)

land = Image("images//land.png",game)
land.moveTo(400,550)
land.resizeBy(80)

crosshair = Image("images//crosshair1.png",game)
crosshair.resizeBy(-80)

abdulstand = Image("images//abdulstand.gif",game)
abdulstand.resizeBy(50)
abdulstand.moveTo(400,450)
abdulshoot = Animation("images//shooting.gif",2,game,148/2,43)
abdulwalk = Animation("images//abdulrun1.png",12,game,478/12,52,frate=4)
abdulwalk.resizeBy(50)

abdulx = 400
abduly = 450

abdulstatus = "stand"

zombie = []



for num in range(300):
    zombie.append(Animation("images//zomb_full.png",18,game,185/5,225/5) )

for z in zombie:
    z.resizeBy(30)
    x = randint(-300,100)
    y = randint(460,460)
    z.moveTo(x,y)
    z.setSpeed(2,270)
    
bullet = Image("images\\gcirc.png",game)
bullet.visible = False
bullet.resizeBy(-96)

game.drawBackground()
game.drawText("Extermination",game.width/2 -50,game.height/2)
game.drawText("Press [Space] To Start",game.width/2 - 72,game.height/2 + 100) 
game.update(30)
game.wait(K_SPACE)

game.score = 0
game.drawText

shoot = Sound("sound//gun2.wav",1)

while not game.over:
    game.processInput()
    bk.draw()
    land.draw()
    bullet.moveTowards(mouse,10)

    for z in zombie:
        z.move()
        if z.collidedWith(bullet):
            z.visible = False
            game.score += 1
        if z.collidedWith(abdulstand):
            game.over = True
    if bullet.collidedWith(crosshair):
        bullet.visible = False
                    
    if keys.Pressed[K_LEFT]:
        abdulstatus = "walkleft"
        abdulx -= 2
    elif keys.Pressed[K_RIGHT]:
        abdulstatus = "walkright"
        abdulx += 2
    if not keys.Pressed[K_LEFT] and not keys.Pressed[K_RIGHT]:
        abdulstatus = "stand"

    if abdulstatus == "walkleft":
        abdulwalk.x = abdulx
        abdulwalk.y = abduly
        abdulwalk.nextFrame()
    elif abdulstatus == "walkright":
        abdulwalk.x = abdulx
        abdulwalk.y = abduly
        abdulwalk.prevFrame()
    else:
        abdulstand.moveTo(abdulx,abduly)
        abdulstand.draw()

    if keys.Pressed[K_SPACE]:
        bullet.visible = True
        bullet.moveTo(abdulx,abduly)
        bullet.setSpeed(10 , crosshair.getAngle())
        shoot.play()

    crosshair.moveTo(mouse.x,mouse.y)
    game.displayScore()

    game.update(60)
game.drawBackground()
game.drawText("Game Over",game.width/2 -50,game.height/2)
game.drawText("Press [Space] To End",game.width/2 - 72,game.height/2 + 100) 
game.update(30)
game.wait(K_SPACE)
game.wait(K_SPACE)


