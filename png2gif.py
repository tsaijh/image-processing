from os import listdir
from os .path import basename
from imageio.v2 import mimsave, imread
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("txtpath", type = str)    #1_XXX, 2_XXX, 3_XXX
txtpath = parser.parse_args().txtpath

f = open(txtpath, 'r')
for path in f.readlines():
    if '\n' == path[-1]:
        path = path[:-1]
    if '' == path:
        continue
    directions = listdir(path)    #front, bottom
    for direction in tqdm(directions):
        images = listdir(path + '/' + direction)    #images 0001 to 0441
        frames = []
        for image in images:
            frame = imread(path + '/' + direction + '/' + image)
            frames.append(frame)
        namefolder = basename(path)
        name = namefolder[:namefolder.find('_')]
        savepath =  path + '/' + str(name) + '_' + str(direction) + '.gif'
        mimsave(savepath, frames, 'GIF', duration = 0.1)
f.close