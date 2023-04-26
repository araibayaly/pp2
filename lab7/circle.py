import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('my game')

ball_position = [400, 300]
speed = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                ball_position[1] -= speed
               elif event.key == pygame.K_DOWN:
                   ball_position[1] += speed
               elif event.key == pygame.K_LEFT:
                   ball_position[0] -= speed
               elif event.key == pygame.K_RIGHT:
                   ball_position[0] += speed

    if ball_position[0] - 25 < 0:
        ball_position[0] = 25
    elif ball_position[0] + 25 > 800:
        ball_position[0] = 800 - 25
    if ball_position[1] - 25 < 0:
        ball_position[1] = 25
    elif ball_position[1] + 25 > 600:
        ball_position[1] = 600 - 25

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', ball_position, 25)
    pygame.display.update()