import pygame
import random
import sys

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
rand_x = 0
rand_y = 0
# Set the width and height of each snake segment
segment_width = 10
segment_height = 10
# Margin between each segment
# segment_margin = 30

# Set initial speed
# x_change = segment_width + segment_margin
x_change = segment_width
y_change = 0
clocks = 10
snake_length = 20

global circ_check
circ_check = True

score = 0

display_width = 600
display_height = 800
counter = 0

class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """

    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def food(self):
        global rand_x, rand_y

        rand_x = random.randrange(20, 78) * 10
        rand_y = random.randrange(20, 58) * 10

        global circ_check
        circ_check = False

    def paused(self):

        print(score)

        while pause:
         for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        

pygame.init()

font = pygame.font.SysFont('Agency FB', 30) 

text = font.render(str(score),True,WHITE)
text_rect = text.get_rect()

text_rect.center = (10,10)


# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the windowcxf1
pygame.display.set_caption('Snake')

allspriteslist = pygame.sprite.Group()

# Create an initial snake
snake_segments = []
for i in range(snake_length):
    x = 250 - (segment_width) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
    

clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                x_change = (segment_width) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height)

    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)

    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)

     # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)

    allspriteslist.draw(screen)

    if segment.rect.x == rand_x and segment.rect.y == rand_y:
        
        segment = Segment(x, y)
        snake_segments.append(segment)
        allspriteslist.add(segment)
        circ_check = True
        snake_length += 1
        score += 10
        text = font.render(str(score),True,WHITE)
        counter+=1
        rands = random.randint(1,10)
        if counter == rands:
            score+=(rands*10)
            counter=0

    pygame.draw.rect(screen, (0, 0, 255), [rand_x, rand_y, 10, 10])

    if circ_check:
        segment.food()

    if segment.rect.x == -10 or segment.rect.x == 800 or segment.rect.y == -10 or segment.rect.y == 600:
        print (score)
        pause = True
        segment.paused()

    for i in range(1, snake_length - 1):

        if (segment.rect.x == snake_segments[i].rect.x) and (segment.rect.y == snake_segments[i].rect.y):
            print(score)
            pause=True
            segment.paused()
    

    screen.blit(text,text_rect)        
    # Flip screen
    pygame.display.flip()
   
    if score == 0:
        clock.tick(clocks)
    
    elif score % 100 != 0:
        clock.tick(clocks)

    elif score % 100 == 0:
        clocks = clocks + 10
        clock.tick(clocks)

pygame.quit()
