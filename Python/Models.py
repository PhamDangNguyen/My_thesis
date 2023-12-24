import sys
import cv2
import numpy as np
import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu' #khong co cad thi chay cpu
model = torch.hub.load('ultralytics/yolov5','custom',path='C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Models/Detect_Droplet.pt',force_reload=True)
model.to(device)
path_img = 'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Data_vinhua/Paper/2.png'
img = cv2.imread(path_img)
detections = model(img)