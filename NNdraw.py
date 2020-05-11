import pygame as py
from config_variables import *
from car import decodeCommand
from vect2d import vect2d
from node import *

py.font.init()

class NN:

    def __init__(self, config, genome, pos):
        self.input_nodes = []
        self.output_nodes = []
        self.nodes = []
        self.genome = genome
        self.pos = (int(pos[0]+NODE_RADIUS), int(pos[1]))
        input_names = ["Sensor T", "Sensor TR", "Sensor R", "Sensor BR", "Sensor B", "Sensor BL", "Sensor L", "Sensor TL", "Speed"]
        output_names = ["Accelerate", "Brake", "Turn Left", "Turn Right"]
        middle_nodes = [n for n in genome.nodes.keys()]
        nodeIdList = []

        #nodes
        h = (INPUT_NEURONS-1)*(NODE_RADIUS*2 + NODE_SPACING)
        for i, input in enumerate(config.genome_config.input_keys):
            n = Node(input, pos[0], pos[1]+int(-h/2 + i*(NODE_RADIUS*2 + NODE_SPACING)), INPUT, [GREEN_PALE, GREEN, DARK_GREEN_PALE, DARK_GREEN], input_names[i], i)
            self.nodes.append(n)
            nodeIdList.append(input)

        h = (OUTPUT_NEURONS-1)*(NODE_RADIUS*2 + NODE_SPACING)
        for i,out in enumerate(config.genome_config.output_keys):
            n = Node(out+INPUT_NEURONS, pos[0] + 2*(LAYER_SPACING+2*NODE_RADIUS), pos[1]+int(-h/2 + i*(NODE_RADIUS*2 + NODE_SPACING)), OUTPUT, [RED_PALE, RED, DARK_RED_PALE, DARK_RED], output_names[i], i)
            self.nodes.append(n)
            middle_nodes.remove(out)
            nodeIdList.append(out)

        h = (len(middle_nodes)-1)*(NODE_RADIUS*2 + NODE_SPACING)
        for i, m in enumerate(middle_nodes):
            n = Node(m, self.pos[0] + (LAYER_SPACING+2*NODE_RADIUS), self.pos[1]+int(-h/2 + i*(NODE_RADIUS*2 + NODE_SPACING)), MIDDLE, [BLUE_PALE, DARK_BLUE, BLUE_PALE, DARK_BLUE])
            self.nodes.append(n)
            nodeIdList.append(m)

        #connections
        self.connections = []
        for c in genome.connections.values():
            if c.enabled:
                input, output = c.key
                self.connections.append(Connection(self.nodes[nodeIdList.index(input)],self.nodes[nodeIdList.index(output)], c.weight))

    def draw(self, world):
        for c in self.connections:
            c.drawConnection(world)
        for node in self.nodes:
            node.draw_node(world)































#----
