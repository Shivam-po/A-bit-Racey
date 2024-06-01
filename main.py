import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (160,0,0)
green = (0,160,0)
bright_red= (255,0,0)
bright_green=(0,255,0)

block_color = (92,47,194)

car_width = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.transform.scale(pygame.image.load('carpic-transformed.png'), (100,100))

pygame.display.set_icon(carImg)



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+ str(count), True , black)
    gameDisplay.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])



def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')


def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse [0] > x and y + h > mouse [1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()


    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)


def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)


        button("GO!",150,500,120,70,green,bright_green,"play")
        button("QUIT?!",750,500,120,70,red,bright_red,"quit")

        mouse = pygame.mouse.get_pos()

        
        smallText = pygame.font.Font("freesansbold.ttf",20)
        TextSurf, TextRect = text_objects("GO!", smallText)
        TextRect.center = ((150+(120/2)), (500+(70/2)))
        gameDisplay.blit(TextSurf, TextRect)


        pygame.display.update()
        clock.tick(15)



   
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100


    dodged = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change

        
        
        gameDisplay.fill(white)
        

     
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed

        
        car(x,y)
        things_dodged(dodged)
     
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed +=0.3
            thing_width += (dodged * 1.02)
            thing_height += (dodged * 1.02)
            if thing_width and thing_height >= 200:
                thing_width = 200
                thing_height = 200
            if thing_speed >= 18:
                thing_speed=18
                


        if y < thing_starty + thing_height :
            print("y crossover")
            if x > thing_startx and x + 20 < thing_startx + thing_width or x+ car_width - 20 > thing_startx and x + car_width < thing_startx + thing_width -20 :
                print("X crossover")
                crash()

            
        
        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()