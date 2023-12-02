# This is the main file for the Image Processing Project, which will be used to run the program.

from skimage import io, color, filters, feature, morphology, measure, draw
from processing import processing
from preprocessing import pre_processing
from post_processing import post_processing
import matplotlib.pyplot as plt
import numpy as np
import os
import math
import random
import cv2
import sys



# Function: main

def main():
    # File path
    path = ''
    
    # Read in the image
    image = io.imread(path)

    # Pre-processing
    image = pre_processing(image)
    
    # Processing
    image = processing(image)

    # Post-processing
    image = post_processing(image)
    
    return 0
    
    
    
    