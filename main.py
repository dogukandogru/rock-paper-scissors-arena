import pygame
import random
from enum import Enum
 
class DIRECTION(Enum):
    UP_LEFT = 1
    UP = 2
    UP_RIGHT = 3
    LEFT = 4
    RIGHT = 5
    DOWN_LEFT = 6
    DOWN = 7
    DOWN_RIGHT = 8

class TYPE(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2
    
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 600
IMAGE_WIDTH = 30
IMAGE_HEIGHT = 30
CLOCK_TICK = 60
NUM_OF_ELEMENTS = 30


def getRandomLocation():
    x = random.randint(0,DISPLAY_HEIGHT)
    y = random.randint(0,DISPLAY_WIDTH)
    return x, y

def getRandomDirection():
    directions = [e for e in DIRECTION]
    direction = random.choice(directions)
    return direction

def initializeArray(NUM_OF_ELEMENTS, type):
    tempArray = []
    for i in range(NUM_OF_ELEMENTS):
        x, y = getRandomLocation()
        obj = {
            "type" : type,
            "x" : x,
            "y" : y,
            "direction" : getRandomDirection()
        }
        tempArray.append(obj)

    return tempArray

def updateCoordinates(array):
    boundryControl(array)

    for obj in array:
        direction = obj['direction']
        
        if direction == DIRECTION.UP_LEFT:
            obj['x'] = obj['x'] - 1
            obj['y'] = obj['y'] - 1
        elif direction == DIRECTION.UP:
            obj['y'] = obj['y'] - 1
        elif direction == DIRECTION.UP_RIGHT:
            obj['x'] = obj['x'] + 1
            obj['y'] = obj['y'] - 1
        elif direction == DIRECTION.LEFT:
            obj['x'] = obj['x'] - 1
        elif direction == DIRECTION.RIGHT:
            obj['x'] = obj['x'] + 1
        elif direction == DIRECTION.DOWN_LEFT:
            obj['x'] = obj['x'] - 1
            obj['y'] = obj['y'] + 1
        elif direction == DIRECTION.DOWN:
            obj['y'] = obj['y'] + 1
        elif direction == DIRECTION.DOWN_RIGHT:
            obj['x'] = obj['x'] + 1
            obj['y'] = obj['y'] + 1

def changeRotation(obj):
    if obj['direction'] == DIRECTION.UP_LEFT:
        return DIRECTION.DOWN_RIGHT

    elif obj['direction'] == DIRECTION.UP:
        return DIRECTION.DOWN

    elif obj['direction'] == DIRECTION.UP_RIGHT:
        return DIRECTION.DOWN_LEFT
    
    elif obj['direction'] == DIRECTION.LEFT:
        return DIRECTION.RIGHT
    
    elif obj['direction'] == DIRECTION.RIGHT:
        return DIRECTION.LEFT
    
    elif obj['direction'] == DIRECTION.DOWN_LEFT:
        return DIRECTION.UP_RIGHT

    elif obj['direction'] == DIRECTION.DOWN:
        return DIRECTION.UP

    elif obj['direction'] == DIRECTION.DOWN_RIGHT:
        return DIRECTION.UP_LEFT
    

def boundryControl(array):
    for obj in array:

        if obj['x'] <= 0:
            if obj['direction'] == DIRECTION.LEFT:
                obj['direction'] = DIRECTION.RIGHT

            elif obj['direction'] == DIRECTION.UP_LEFT:
                obj['direction'] = DIRECTION.UP_RIGHT

            elif obj['direction'] == DIRECTION.DOWN_LEFT:
                obj['direction'] = DIRECTION.DOWN_RIGHT

        elif obj['x'] >= DISPLAY_WIDTH - IMAGE_WIDTH:
            if obj['direction'] == DIRECTION.RIGHT:
                obj['direction'] = DIRECTION.LEFT

            elif obj['direction'] == DIRECTION.UP_RIGHT:
                obj['direction'] = DIRECTION.UP_LEFT

            elif obj['direction'] == DIRECTION.DOWN_RIGHT:
                obj['direction'] = DIRECTION.DOWN_LEFT
        
        if obj['y'] <= 0:
            if obj['direction'] == DIRECTION.UP:
                obj['direction'] = DIRECTION.DOWN

            elif obj['direction'] == DIRECTION.UP_LEFT:
                obj['direction'] = DIRECTION.DOWN_LEFT

            elif obj['direction'] == DIRECTION.UP_RIGHT:
                obj['direction'] = DIRECTION.DOWN_RIGHT
        elif obj['y'] >= DISPLAY_HEIGHT - IMAGE_HEIGHT:
            if obj['direction'] == DIRECTION.DOWN:
                obj['direction'] = DIRECTION.UP

            elif obj['direction'] == DIRECTION.DOWN_LEFT:
                obj['direction'] = DIRECTION.UP_LEFT

            elif obj['direction'] == DIRECTION.DOWN_RIGHT:
                obj['direction'] = DIRECTION.UP_RIGHT


def isPointInsideRectangle(x1, y1, x2,
              y2, x, y) :
    if (x > x1 and x < x2 and
        y > y1 and y < y2) :
        return True
    else :
        return False

def calculateBattle(type1, type2):
    if type1 == TYPE.ROCK and type2 == TYPE.ROCK:
        return TYPE.ROCK

    elif type1 == TYPE.ROCK and type2 == TYPE.PAPER:
        return TYPE.PAPER

    elif type1 == TYPE.ROCK and type2 == TYPE.SCISSOR:
        return TYPE.ROCK

    elif type1 == TYPE.PAPER and type2 == TYPE.ROCK:
        return TYPE.PAPER

    elif type1 == TYPE.PAPER and type2 == TYPE.PAPER:
        return TYPE.PAPER

    elif type1 == TYPE.PAPER and type2 == TYPE.SCISSOR:
        return TYPE.SCISSOR
   
    elif type1 == TYPE.SCISSOR and type2 == TYPE.ROCK:
        return TYPE.ROCK

    elif type1 == TYPE.SCISSOR and type2 == TYPE.PAPER:
        return TYPE.SCISSOR

    elif type1 == TYPE.SCISSOR and type2 == TYPE.SCISSOR:
        return TYPE.SCISSOR


def detectCollision(elementArray):
    for obj1 in elementArray:
        leftBoundry = obj1['x'] - IMAGE_WIDTH
        rightBoundry = obj1['x'] + IMAGE_WIDTH
        topBoundry = obj1['y'] - IMAGE_HEIGHT
        bottomBoundry = obj1['y'] + IMAGE_HEIGHT
        for obj2 in elementArray:
            if isPointInsideRectangle(leftBoundry,topBoundry,rightBoundry,bottomBoundry,obj2['x'],obj2['y']):
                obj1['type'] = calculateBattle(obj1['type'], obj2['type'])
                obj2['type'] = calculateBattle(obj1['type'], obj2['type'])
                obj1['direction'] = changeRotation(obj1)
                obj2['direction'] = changeRotation(obj2)

def isGameOver():
    pass

def changeRotationWhenCollisionOccur():
    pass

def main():
    pygame.init()

    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
    pygame.display.set_caption('Rock Paper Scissors Simulator')

    black = (0,0,0)
    white = (255,255,255)

    clock = pygame.time.Clock()
    crashed = False

    rockImg = pygame.transform.scale(pygame.image.load('img/rock.png'), (IMAGE_WIDTH, IMAGE_HEIGHT))
    paperImg = pygame.transform.scale(pygame.image.load('img/paper.png'), (IMAGE_WIDTH, IMAGE_HEIGHT))
    scissorImg = pygame.transform.scale(pygame.image.load('img/scissor.png'), (IMAGE_WIDTH, IMAGE_HEIGHT))


    elementArray = initializeArray(NUM_OF_ELEMENTS, TYPE.ROCK) + initializeArray(NUM_OF_ELEMENTS, TYPE.PAPER) + initializeArray(NUM_OF_ELEMENTS, TYPE.SCISSOR)

    imgArray = [rockImg, paperImg, scissorImg]

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill(white)

        detectCollision(elementArray)

        updateCoordinates(elementArray)

        for obj in elementArray:
            gameDisplay.blit(imgArray[obj['type'].value], (obj['x'],obj['y']))

            
        pygame.display.update()
        clock.tick(CLOCK_TICK)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()