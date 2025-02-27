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
left_pad_x_position=0
left_pad_y_position=0
right_pad_x_position=screen_height//2
right_pad_y_position=680

left_pad_speed=0
right_pad_speed=0

white=(255,255,255)

score = 0
font = pygame.font.Font(None,50)

def displayScore():
    global score
    text=font.render(f"Score: {score}",True,(255,255,255))
    text_rect=text.get_rect(center=(screen_width//2,20))
    screen.blit(text,text_rect)

    

running = True
while running:

    play = True
    hit = False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                    left_pad_speed=-10

            elif event.key==pygame.K_s:
                    left_pad_speed=10
            
            elif event.key==pygame.K_DOWN:
                 right_pad_speed=10
            
            elif event.key==pygame.K_UP:
                 right_pad_speed=-10
            
            elif event.key==pygame.K_q:
                 running=False
                    
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w or event.key==pygame.K_s: 
                left_pad_speed=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                 right_pad_speed=0
        
        
    left_pad_x_position+=left_pad_speed
    left_pad_x_position=max(0,min(screen_height-pad_height,left_pad_x_position))

    right_pad_x_position+=right_pad_speed
    right_pad_x_position=max(0,min(screen_height-pad_height,right_pad_x_position))
            
    #Move the ball
    ball_x_position+=ball_speed_x
    ball_y_position+=ball_speed_y
    
    #Ball collision with the left and right boundaries
    # if(ball_x_position<ball_radius or ball_x_position>=screen_width-ball_radius   ):
    #     ball_speed_x=-ball_speed_x

    
    #Balll collision with the bottom and top boundaries
    if(ball_y_position<=ball_radius or ball_y_position>=screen_height-ball_radius):
        ball_speed_y=-ball_speed_y
        
    #Ball collision with the paddel
    if (ball_x_position-ball_radius) <= pad_width and left_pad_x_position < ball_y_position < left_pad_x_position + pad_height:
        ball_speed_x = -ball_speed_x
        hit = True

    if (ball_x_position-ball_radius) <= pad_width and right_pad_x_position < ball_y_position < right_pad_x_position + pad_height:
        ball_speed_x=-ball_speed_x
        hit = True

    #Paddle missing and game restarting
    if(ball_x_position-ball_radius<=0 or ball_x_position-ball_radius >=screen_width):
         print("Game over, restarting...")
         pygame.time.delay(1000)
         ball_x_position=screen_width//2
         ball_y_position=screen_height//2
         print("hit")
         score =0
        
    if(hit):
         score+=1

    screen.fill("black")
    pygame.draw.circle(screen,white,((ball_x_position),(ball_y_position)),ball_radius)
    pygame.draw.rect(screen,white,((left_pad_y_position),(left_pad_x_position),pad_width,pad_height))
    pygame.draw.rect(screen,white,((right_pad_y_position),(right_pad_x_position),pad_width,pad_height))

    text=font.render(f"Score: {score}",True,(255,255,255))
    text_rect=text.get_rect(center=(screen_width//2,20))
    screen.blit(text,text_rect)
    

    displayScore()
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()


