import pygame
import time

pygame.init()
pygame.display.set_caption("Pong Game")

screen_width=700
screen_height=500
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()


#ball properties
ball_radius=10
ball_x_position=screen_width//2
ball_y_position=screen_height//2
ball_speed_x=4
ball_speed_y=4

#pad properties
pad_height=100
pad_width=20
pad_x_position=0
pad_y_position=0
pad_speed=0

white=(255,255,255)

score = 0
font = pygame.font.Font(None,50)

def displayScore():
    global score
    score+=1
    text=font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(text,(screen_width//2,10))

    

running = True
while running:

    play = True
    hit = False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                    pad_speed=-10

            elif event.key==pygame.K_s:
                    pad_speed=10
                    
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w or event.key==pygame.K_s:
                pad_speed=0
        
        if pad_x_position<0:
            pad_x_position=0 
    pad_x_position+=pad_speed
 
            
                            
    ball_x_position+=ball_speed_x
    ball_y_position+=ball_speed_y
    
    if(ball_x_position<=ball_radius or ball_x_position>=screen_width-ball_radius):
        ball_speed_x=-ball_speed_x
        

    if(ball_y_position<=ball_radius or ball_y_position>=screen_height-ball_radius):
        ball_speed_y=-ball_speed_y
        
    if (ball_x_position-ball_radius) <= pad_width and pad_x_position < ball_y_position < pad_x_position + pad_height:
        ball_speed_x = -ball_speed_x
        hit = True

    if(ball_x_position-ball_radius<=0):
         print("Game over, restarting...")
         pygame.time.delay(1000)
         ball_x_position=screen_width//2
         ball_y_position=screen_height//2
         print("hit")
         score =0

    screen.fill("black")
    pygame.draw.circle(screen,white,((ball_x_position),(ball_y_position)),ball_radius)
    pygame.draw.rect(screen,white,((pad_y_position),(pad_x_position),pad_width,pad_height))

    text=font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(text,(screen_width//2,10))
    if(hit==True):
        displayScore()

    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


