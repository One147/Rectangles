import pygame
from sys import exit
import time
import random 
pygame.init()

#screen init
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))               
clock = pygame.time.Clock()            
camera_width = 100
camera_height = 100 





class Rectangle(pygame.sprite.Sprite):
    def __init__(self, xpos , ypos , width , height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.random_value = (random.randint(0,255) , random.randint(0,255) , random.randint(0,255))
        self.image.fill(self.random_value)
        self.rect = self.image.get_rect()
        self.rect.left = xpos
        self.rect.bottom = ypos  
        
    def change_rectangle(self, xpos, ypos , width , height):
        self.image = pygame.Surface([100,100])
        self.image.fill(self.random_value)
        self.rect = pygame.Rect( xpos , (ypos - height) , width , height )
        


class Camera(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill("Black")
        self.rect = self.image.get_rect()
        
        #initial triangle 
        
    
    def update(self):
        self.image.fill("Black") #background
        for rects in rect_group:
            self.image.blit(rects.image , rects.rect)
        
        
        




#making rectangle group 
rect_group = pygame.sprite.Group()

#making camera object
camera = Camera(camera_width,camera_height)


def display_camera():
    camera.update()
    screen.blit((pygame.transform.scale(camera.image, (screen_width, screen_height))) , (pygame.transform.scale(camera.image, (screen_width, screen_height))).get_rect())
    pygame.display.update()
    
def rect_creation():
    rect_group.add(Rectangle( ((camera_width / (len(rect_group)+1))*(len(rect_group))) , (camera_height) , ((camera_width) / (len(rect_group) + 1)) , (camera_height )))

def transform_rectangles():
    #set sprite index to 0
    sprite_index = 0
    
    for rects in rect_group:
        #transform the rectangle by 
        #  changing the width to the total width of the camera screen divided by the amount of sprites
        # changing the height to the (total height of the camera screen divided by the number of sprites) + (total height of the camera screen divided by the number of sprites) * (the index of the rect)
        # changing xpos position to (camera width divided by total number of sprites) * the index of the sprite 
        # ypos remains the same
        rects.change_rectangle( (camera_width / len(rect_group))*(sprite_index) , camera_height , (camera_width)/(len(rect_group)) , (camera_height / len(rect_group)) + (camera_height / len(rect_group))*(sprite_index) ) 

        #move sprite index to next value
        
        sprite_index += 1    

while True:                                                         
    start_time = time.time()
    #create rect and display rect onto surface (created in the camera class)
    try:
        rect_creation()
    except:
        print("Error another rect could not be created. total rects: " , len(rect_group))
    
    #transform rectangles
    try:
        transform_rectangles()
        
    except:
        print("Error, rects couldnt be transformed to smaller value. Max Rects: " , len(rect_group))
    
    #display camera
    try:
        display_camera()
    except:
        print("Error rects couldnt be drawn onto camera. Max Rects: " , len(rect_group))  

    #time tracking
    end_time = time.time()
    print(f'Loop completed in: {end_time - start_time}                    Loop total {len(rect_group)}                     Width {camera_width / len(rect_group)}')
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    clock.tick(5)        
                      