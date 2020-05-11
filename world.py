import pygame as py

class World:

    initialPos = (0,0)
    bestCarPos = (0,0)

    def __init__(self, starting_pos, world_width, world_height):
        self.initialPos = starting_pos
        self.bestCarPos = (0, 0)
        self.win  = py.display.set_mode((world_width, world_height))
        self.win_width = world_width
        self.win_height = world_height
        self.score = 0
        self.bestGenome = None

    def updateBestCarPos(self, pos):
        self.bestCarPos = pos

    def getScreenCoords(self, x, y):
        return (int(x + self.initialPos[0] - self.bestCarPos[0]), int(y + self.initialPos[1] - self.bestCarPos[1]))

    def getBestCarPos(self):
        return self.bestCarPos

    def updateScore(self, new_score):
        self.score = new_score

    def getScore(self):
        return self.score
