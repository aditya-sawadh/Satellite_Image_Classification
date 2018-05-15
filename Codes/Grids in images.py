# coding: utf-8
from __future__ import division
import tifffile as tiff
import numpy as np
import math

def createMask(image_shape):

	## Image Dimensions
	refXLength = 834
	refYLength = 830

	## Grid dimensions
	gridXLen = round(30 * image_shape[0]/refXLength)
	gridYLen = round(30 * image_shape[1]/refYLength)

	# print("CreateMask() :")
	# print(gridXLen)
	# print(gridYLen)
	# print("-----------------")

	gridMask = np.zeros((image_shape[0], image_shape[1]))

	numGridsX = math.ceil(image_shape[0]/gridXLen)
	for x in range(0, image_shape[0]):
		for y in range(0, image_shape[1]):
			gridMask[x][y] = (x//gridXLen+1) + numGridsX*(y//gridYLen) 

	return gridMask
