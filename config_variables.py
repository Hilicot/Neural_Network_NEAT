import pygame as py
py.font.init()


#=================== General constants ==================================
FPS = 30
WIN_WIDTH = 1800
WIN_HEIGHT = 1000
STARTING_POS = (WIN_WIDTH/2, WIN_HEIGHT-100)
SCORE_VEL_MULTIPLIER = 0.00                     #bonus for faster cars
BAD_GENOME_TRESHOLD = 200                       #if a car is too far behind it is removed

INPUT_NEURONS = 9
OUTPUT_NEURONS = 4

#=================== Car Specs ==================================

CAR_DBG = False
FRICTION  = -0.1
MAX_VEL = 10
MAX_VEL_REDUCTION = 1              #at the start reduce maximum speed
ACC_STRENGHT = 0.2
BRAKE_STREGHT = 1
TURN_VEL = 2
SENSOR_DISTANCE = 200
ACTIVATION_TRESHOLD = 0.5

#=================== Road Specs ==================================

ROAD_DBG = False
MAX_ANGLE = 1
MAX_DEVIATION = 300
SPACING = 200
NUM_POINTS  = 15                #number of points for each segment
SAFE_SPACE = SPACING + 50       #buffer space above the screen
ROAD_WIDTH = 200

#=================== Display and Colors ==================================

NODE_RADIUS = 20
NODE_SPACING = 5
LAYER_SPACING = 100
CONNECTION_WIDTH = 1

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
DARK_RED = (100, 0, 0)
RED_PALE = (250, 200, 200)
DARK_RED_PALE = (150, 100, 100)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 100, 0)
GREEN_PALE = (200, 250, 200)
DARK_GREEN_PALE = (100, 150, 100)
BLUE = (0,0,255)
BLUE_PALE = (200, 200, 255)
DARK_BLUE = (100, 100, 150)

NODE_FONT = py.font.SysFont("comicsans", 15)
STAT_FONT = py.font.SysFont("comicsans", 50)


#=================== Constants for internal use ==================================
GEN = 0

#enumerations
ACC = 0
BRAKE = 1
TURN_LEFT = 2
TURN_RIGHT = 3

INPUT = 0
MIDDLE = 1
OUTPUT = 2
