import cv2
from ultralytics import YOLO
import os
import cv2
import math
import torch
model_path = 'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Models/Detect_Droplet.pt'
model_segv8 = YOLO(model_path)
# Đường dẫn đến video
video_path = 'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/video_data/1.mp4'

# Mở video để đọc
cap = cv2.VideoCapture(video_path)

# Kiểm tra xem video đã mở thành công hay chưa
if not cap.isOpened():
    print("Không thể mở video.")
else:
    frame_count = 0  # Biến đếm số frame đã đọc
    count = 0
    while True:
        # Đọc frame từ video
        ret, frame = cap.read()
        frame_crop = frame[250:900,525:1265]

        img = cv2.resize(frame_crop,(640,640))
        # image = cv2.resize(frame_crop, (640, 640))
        results = model_segv8(img,hide_labels=True,line_thickness=1,conf=0.25,imgsz = 640)
        boxes = results[0].boxes
        cls = boxes.cls.cpu().numpy().astype("uint8")
        bbox = boxes.data.cpu().numpy()
        for i in range(0,len(cls)):
            x1_bb,y1_bb,x2_bb,y2_bb,_,_= bbox[i]
            center = (int((x1_bb + x2_bb)/2),int((y1_bb + y2_bb)/2))
            about = y2_bb - y1_bb
            # # cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
            x1_ct = int(center[0] - about/2)
            y1_ct = int(center[1] - about/2)

            # Tính toạ độ góc dưới bên phải của hình chữ nhật
            x2_ct = int(center[0] + about/2)
            y2_ct = int(center[1] + about/2)
        

            print( x1_ct,y1_ct,x2_ct,y2_ct)
            if y1_ct <= 0:
                cv2.rectangle(img, (int(x1_ct),int(y1_ct)), (int(x2_ct),int(y2_ct)), (255,255,255), 2)
            elif y2_ct >= 638:
                cv2.rectangle(img, (int(x1_ct),int(y1_ct)), (int(x2_ct),int(y2_ct)), (255,255,255), 2)
            else:
                crop_1 = img[y1_ct:y2_ct,x1_ct:x2_ct]
                crop = cv2.resize(crop_1,(640,640))
                cv2.imwrite(f'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Data_vinhua/Crop_by_model/{count}_dif.png',crop)
                count = count + 1
                cv2.rectangle(img, (int(x1_ct),int(y1_ct)), (int(x2_ct),int(y2_ct)), (255, 0, 0), 2)
            # cropped_image = img[y1r:y2r, x1r:x2r]
            # cropped_image = cv2.resize(cropped_image, (640, 640))




        # Kiểm tra xem đã đọc hết video hay chưa
        if not ret:
            break
        # Vẽ hình chữ nhật bằng vùng frame_crop trên frame gốc
        # x1, y1, x2, y2 = 525, 250, 1265, 900
        # cv2.rectangle(frame_crop, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Xử lý frame ở đây (ví dụ: hiển thị frame)
        cv2.imshow('Frame', img)

        # Tăng biến đếm số frame đã đọc
        frame_count += 1

        # Để thoát vòng lặp, bạn có thể nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên khi xong
    cap.release()
    cv2.destroyAllWindows()

# In tổng số frame đã đọc
print(f'Tổng số frame: {frame_count}')