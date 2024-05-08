import cv2
import numpy as np
from deepface import DeepFace
img=cv2.imread("criminals/nabih.jpg")
results= DeepFace.analyze(img, actions=("gender","age","race","emotion"))
print (results)
