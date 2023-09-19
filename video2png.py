# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:27:05 2022

@author: TSAI
"""

import cv2
from os import makedirs
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("videopath", type = str)
parser.add_argument("outputdirpath", type = str)
videopath = parser.parse_args().videopath
outputdirpath = parser.parse_args().outputdirpath

makedirs(outputdirpath, exist_ok=True)

vc = cv2.VideoCapture(videopath)
length = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))

for number in tqdm(range(1,length+1)):
    rval, frame = vc.read()
    cv2.imwrite(outputdirpath + '/' + str(number) + '.png', frame)

vc.release()