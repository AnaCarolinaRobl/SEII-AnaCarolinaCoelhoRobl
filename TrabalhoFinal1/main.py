import pygame
import math
import pend_sim
from time import sleep

#VARIABLES
width, height = 800, 400   
                           
Out = False                
length = 150                 
angle = 0               
user_input = 0 
k = 0            
 
#COLORS
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
rose = (135, 4, 72)
color = pygame.Color('aquamarine4')
 
#BEFORE START
pygame.init()
pygame.display.set_caption("Aeropêndulo")
fonte = pygame.font.SysFont('arial', 20, True, True)
background = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#INPUT
text = fonte.render('Simulação Aeropêndulo', True, black, color)
text2 = fonte.render('Digite o Ângulo desejado:', True, black, color)
user_text = ''
input_rect = pygame.Rect(350,300,140,32)


img1 = pygame.image.load('sprites/Layer1.png')
img2 = pygame.image.load('sprites/Layer2.png')
img3 = pygame.image.load('sprites/Layer3.png')

textRect = text.get_rect()
textRect.center = (400, 50)

textRect2 = text2.get_rect()
textRect2.center = (200, 315)


def rect_input(bg): 
        pygame.draw.rect(background, color, input_rect, 0)
        text = fonte.render(user_text, True, black)
        background.blit(text,(input_rect.x+5,input_rect.y+5))
        input_rect.w = max(100, text.get_width()+10)

def angle_Length(angle): 
    vetor=pend_sim.main(user_input,angle)
    #print(vetor)
    j=0
    i = len(vetor)
    #print(i)
    while (i>0):
        angle = vetor[j]
        #print(angle)
        img_rotate, img_rectcenterx, img_rectcentery = get_path(angle, j)  
        redraw(img_rotate, img_rectcenterx, img_rectcentery)
        clock.tick(60)
        j+=1
        i-=1
    return (angle)
 
def get_path(first_angle, cont): 
    
    img1_rotate = pygame.transform.rotate(img1, first_angle)
    img2_rotate = pygame.transform.rotate(img2, first_angle)
    img3_rotate = pygame.transform.rotate(img3, first_angle)
    img1_rect = img1_rotate.get_rect()
    img2_rect = img2_rotate.get_rect()
    img3_rect = img3_rotate.get_rect()

    if cont % 3 == 0:
        return (img2_rotate, img2_rect.centerx, img2_rect.centery)
    elif cont % 2 == 0:
        return (img3_rotate, img3_rect.centerx, img3_rect.centery)
    else:
        return (img1_rotate, img1_rect.centerx, img1_rect.centery)


 
def redraw(img_rotate, img_rectcenterx, img_rectcentery): 
    background.fill(rose)
    background.blit(text, textRect)
    background.blit(text2, textRect2) 
    background.blit(img_rotate, (width/2 - img_rectcenterx, 100 - img_rectcentery))
    rect_input(background)
    pygame.display.update()
 
 


while not Out:
    clock.tick(50)              
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            Out = True 
        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            if  44 < ord(event.unicode) < 58 :
                user_text += event.unicode

            if event.key == pygame.K_RETURN:
                #print(user_text)
                user_input = float(user_text)
                user_text = ''
                #print(user_input)
                angle = angle_Length(angle)
                #print(angle)
              
    k += 1
    if user_input == 0:
        k = 0
    img_rotate, img_rectcenterx, img_rectcentery = get_path(angle, k)  
    redraw(img_rotate, img_rectcenterx, img_rectcentery)
 
pygame.quit()