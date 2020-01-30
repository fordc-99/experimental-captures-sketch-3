import json
import pygame
import math
import sys

##### START CONSTANTS #####
# some jank IO handling, for ease of demo
args = sys.argv
if (len(args) < 2):
    IS_LINE = False
else:
    IS_LINE = args[1] == 'line'

# set constants based on video
if (IS_LINE):
    WIDTH = 960
    HEIGHT = 540
    FILE_NAME = 'dog_doline.json'
else:
    WIDTH = 1920
    HEIGHT = 1080
    FILE_NAME = 'light_circles.json'
FPS = 30 
BLACK = (0, 0, 0)
#####  END CONSTANTS  #####

# convert file to be readable as json by python
with open(FILE_NAME) as edit_json:
    unformatted_data = edit_json.read()

unformatted_data = "[" + unformatted_data.replace("}\n", "},", unformatted_data.count("}\n")-1) + "]"
data = json.loads(unformatted_data)

# start visualization
pygame.init()

# clock for redrawing
fpsClock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
gameDisplay.fill(BLACK)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # go through each frame
    for i in range(len(data)):
        # clear the screen
        gameDisplay.fill(BLACK)

        # set the line color to the avg frame color, cast to int
        r = int(data[i]['mean_red'])
        g = int(data[i]['mean_green'])
        b = int(data[i]['mean_blue'])
        frame_color = (r, g, b)

        # get thickness from frame count
        thickness = max(10, min(abs(int(math.cos(data[i]['frame']) * 50)), 50))

        # iterate over all the shapes in the frame
        if (IS_LINE):
            shape_data = data[i]['lines']
        else:
            shape_data = data[i]['circles']
        for j in range(len(shape_data)):
            if (IS_LINE):
                # get first point, as an array
                start_point = shape_data[j][0]
                # multiply to get proper coordinates, cast to int
                start_tuple = (int(start_point[0]*WIDTH), int(start_point[1]*HEIGHT))

                # get second point, as an array
                end_point = shape_data[j][1]
                # multiply to get proper coordinates, cast to int
                end_tuple = (int(end_point[0]*WIDTH), int(end_point[1]*HEIGHT))

                # draw the line
                pygame.draw.line(gameDisplay, frame_color, start_tuple, end_tuple, thickness)
            else:
                # get circle data
                circle = shape_data[j]
                
                # get center as tuple, cast to int
                center = (int(circle['cx']), int(circle['cy']))
                # get radius as int
                radius = int(circle['r'])

                # draw the circle
                pygame.draw.circle(gameDisplay, frame_color, center, radius, min(thickness, radius))
                
        # animate the shapes
        pygame.display.flip()
        fpsClock.tick(FPS)
        pygame.display.update()
            