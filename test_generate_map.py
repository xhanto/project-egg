import pandas as pd
import cv2
import csv
import ast
import numpy as np

fname = raw_input("Enter csv file name (no extension): ")
res = np.zeros((128,160,3))

block = []
with open(fname + ".csv", 'rb') as f:
    reader = csv.reader(f,delimiter=';')
    raw_map = map(tuple, reader)

    for i in range(8):
        block_line = []
        for j in range(10):
            b = raw_map[i][j]
            b = b[1:-1].split(',')
            case = cv2.imread("elements\\" + b[0] + ".png")
            res[i*16:(1+i)*16,j*16:(j+1)*16]=case
            block_line.append(b[1])
        block.append(block_line)


cv2.imwrite(fname + ".png",res)
