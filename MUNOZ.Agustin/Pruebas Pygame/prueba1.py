import sys, pygame
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("probando")
width, height = 800, 600
speed = [1, 1]
white = 255, 255, 255
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(400, 260)
run=True
while run:
	pygame.time.delay(0)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: run = False
        
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		baterect=baterect.move(0, -1)
	if keys[pygame.K_DOWN]:
		baterect=baterect.move(0, 1)
	if baterect.colliderect(ballrect):
		speed[0] = - speed[0]
		# Muevo la pelota
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[1] = -speed[1]
	screen.fill(white)
	screen.blit(ball, ballrect)
	pygame.display.flip()
pygame.quit()