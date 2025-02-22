import pygame
import time

pygame.init()

scree_width=700
screen_height=500
screen = pygame.display.set_mode((scree_width,screen_height))
clock = pygame.time.Clock()


#ball properties
ball_radius=10
ball_x_position=scree_width//2
ball_y_position=screen_height//2
ball_speed_x=2
ball_speed_y=2

#pad properties
pad_height=100
pad_width=20
pad_x_position=screen_height//2
pad_y_position=0
move =True

white=(255,255,255)

runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runnig = False
        
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                if(pad_x_position<400):
                    pad_x_position+=20
            elif event.key==pygame.K_w:
                if(pad_x_position>0):
                    pad_x_position-=20
        
    ball_x_position+=ball_speed_x
    ball_y_position+=ball_speed_y
    
    if(ball_x_position<=ball_radius or ball_x_position>=scree_width-ball_radius):
        ball_speed_x=-ball_speed_x
        
            
    if(ball_y_position<=ball_radius or ball_y_position>=screen_height-ball_radius):
        ball_speed_y=-ball_speed_y
    
            
    screen.fill("black")
    pygame.draw.circle(screen,white,((ball_x_position),(ball_y_position)),ball_radius)
    pygame.draw.rect(screen,white,((pad_y_position),(pad_x_position),pad_width,pad_height))
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()