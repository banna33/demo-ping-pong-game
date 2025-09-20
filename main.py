from pygame import *
from sprites_module import GameSprite, Player

window = display.set_mode((600,500))
background = transform.scale(image.load('tennis_court.png'),(600,500))

clock = time.Clock()

ball = GameSprite('tennisball.png', 50, 50, 60, 60, 2)
racket1 = Player('racket_1.png', 5, 240, 30, 150, 4)
racket2 = Player('racket_2.png', 560, 240, 30, 150, 4)


font.init()
font1 = font.SysFont('Arial', 35)
player1_lose = font1.render('Player 1 Lost!', True, (255,255,0))
font2 = font.SysFont('Arial', 35)
player2_lose = font2.render('Player 2 Lost!', True, (255,255,0))

speed_x = 2
speed_y = 2

run = True
finish = True

while run: 
  for e in event.get():
    if e.type == QUIT:
      run = False
    
  if finish:
    window.blit(background, (0,0))
    ball.reset(window)

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y >= 440 or ball.rect.y <=0 :
      speed_y *= -1
    
    if sprite.collide_rect(racket2, ball) or sprite.collide_rect(racket1, ball):
      speed_x *= -1

    if ball.rect.x <= 0:
      window.blit(player1_lose, (200,200))
      finish = False
    
    if ball.rect.x >= 600:
      window.blit(player2_lose, (200,200))
      finish = False

    racket1.reset(window)
    racket2.reset(window)

    racket1.update_1()
    racket2.update_2()

  display.update()
  clock.tick(60)