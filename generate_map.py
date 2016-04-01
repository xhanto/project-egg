import pandas as pd
import cv2
import csv
import ast
import numpy as np
class Map_part:

    def __init__(self,fname):
        self.res = np.zeros((128,160,3))
        self.filename = fname

    def generate(self):
        self.block = []
        with open(fichier, 'rb') as f:
            reader = csv.reader(f,delimiter=';')
            raw_map = map(tuple, reader)

            for i in range(8):
                block_line = []
                for j in range(10):
                    b = raw_map[i][j]
                    b = b[1:-1].split(',')
                    case = cv2.imread("elements\\" + b[0] + ".png")
                    self.res[i*16:(1+i)*16,j*16:(j+1)*16]=case
                    block_line.append(b[1])
                self.block.append(block_line)

    def display(self):

#    cv2.imwrite("map1.png",res)
