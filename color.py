import pygame
pygame.init()
Background = pygame.display.set_mode((1000 ,1000))
for i in range(0, 1000, 30):
    pygame.draw.line(Background, (255, 255, 255), (0, i), (1000, i))
    pygame.draw.line(Background, (255, 255, 255), (i, 0), (i, 1000))
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    #pygame.draw.rect(Background,(255,255,255), (0,0,1000,1000))
    pygame.draw.rect(Background,(255,255,255),(360,30,90,30))
    pygame.draw.rect(Background,(255,255,255),(330,60,30,30))
    pygame.draw.rect(Background,(255,255,255),(450,60,30,30))
    pygame.draw.rect(Background,(255,255,255),(240,90,120,30))
    pygame.draw.rect(Background,(255,255,255),(240,90,120,30))
    pygame.draw.rect(Background,(255,255,255),(210,210,30,30))
    pygame.draw.rect(Background,(255,255,255),(210,120,30,60))
    pygame.draw.rect(Background,(255,255,255),(240,180,90,30))
    pygame.draw.rect(Background,(255,255,255),(180,240,30,60))
    pygame.draw.rect(Background,(255,255,255),(150,300,30,60))
    pygame.draw.rect(Background,(255,255,255),(120,360,30,210))

    #doing right part now
    pygame.draw.rect(Background,(255,255,255),(510,120,30,30))
    pygame.draw.rect(Background,(255,255,255),(480,90,30,30))
    pygame.draw.rect(Background,(255,255,255),(540,150,30,30))
    pygame.draw.rect(Background,(255,255,255),(570,180,30,30))
    pygame.draw.rect(Background,(255,255,255),(600,210,30,30))
    pygame.draw.rect(Background,(255,255,255),(630,240,30,30))
    pygame.draw.rect(Background,(255,255,255),(660,270,30,30))
    pygame.draw.rect(Background,(255,255,255),(690,300,30,90))
    pygame.draw.rect(Background,(255,255,255),(720,360,30,240))
    
    #making outline lower
    pygame.draw.rect(Background,(255,255,255),(690,600,30,30))
    pygame.draw.rect(Background,(255,255,255),(660,630,30,30))
    pygame.draw.rect(Background,(255,255,255),(630,660,30,30))
    pygame.draw.rect(Background,(255,255,255),(630,600,30,30))
    pygame.draw.rect(Background,(255,255,255),(300,690,330,30))
    pygame.draw.rect(Background,(255,255,255),(240,660,60,30))
    pygame.draw.rect(Background,(255,255,255),(210,630,30,30))
    pygame.draw.rect(Background,(255,255,255),(180,600,30,30))
    pygame.draw.rect(Background,(255,255,255),(150,570,30,30))

    #making outline left
    pygame.draw.rect(Background,(255,255,255),(90,390,30,120))
    pygame.draw.rect(Background,(255,255,255),(60,420,30,60))
    pygame.draw.rect(Background,(255,255,255),(30,420,30,60))
    pygame.draw.rect(Background,(255,255,255),(0,360,60,60))
    pygame.draw.rect(Background,(255,255,255),(60,360,30,30))
    pygame.draw.rect(Background,(255,255,255),(30,510,60,30))
    #making inner lower
    pygame.draw.rect(Background,(255,255,255),(540,600,90,30))
    pygame.draw.rect(Background,(255,255,255),(480,630,90,30))
    pygame.draw.rect(Background,(255,255,255),(480,570,60,30))
    pygame.draw.rect(Background,(255,255,255),(450,600,30,30))
    pygame.draw.rect(Background,(255,255,255),(420,510,30,90))
    pygame.draw.rect(Background,(255,255,255),(450,510,30,30))
    pygame.draw.rect(Background,(255,255,255),(390,480,30,30))
    pygame.draw.rect(Background,(255,255,255),(360,390,30,90))
    pygame.draw.rect(Background,(255,255,255),(330,360,120,30))
    pygame.draw.rect(Background,(255,255,255),(390,390,120,30))
    pygame.draw.rect(Background,(255,255,255),(450,420,210,30))
    pygame.draw.rect(Background,(255,255,255),(570,390,150,30))
    pygame.draw.rect(Background,(255,255,255),(630,360,60,30))
    pygame.draw.rect(Background,(255,255,255),(660,420,30,90))
    pygame.draw.rect(Background,(255,255,255),(570,450,30,30))
    pygame.draw.rect(Background,(255,255,255),(480,450,30,30))
    pygame.draw.rect(Background,(255,255,255),(510,480,60,30))



    

    pygame.display.flip()