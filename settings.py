import math

#game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH //2
HALF_HEIGHT = HEIGHT //2
FPS = 0

PLAYER_POS = 1.5, 5 #mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAER_ROT_SPEED = 0.002

'''define feild of veiw of player and the number of rays used in view 
the number of rays for the whole game it is enough to take half of the resolution width value
Based on the number of rays we will define the angle between the rays delta angle and
define the max depth defined as draw distance '''

FOV = math.pi / 3
HALF_FOV = FOV / 2 
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

#3d projection calculating the correct distance for the screen location 
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
#determin scaling factor
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2