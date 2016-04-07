import pandas as pd
import cv2
import csv
import ast
import numpy as np

fname = raw_input("Enter csv file name (no extension): ")
res = np.zeros((128,160,3))


with open("maps/" + fname + ".csv", 'rb') as f:
    reader = csv.reader(f,delimiter=',')
    raw_map = map(tuple, reader)

    for i in range(8):

        for j in range(10):
            b = raw_map[i][j]
            case = cv2.imread("elements\\" + b + ".png")
            res[i*16:(1+i)*16,j*16:(j+1)*16]=case

cv2.imwrite("maps/" + fname + ".png",res)
