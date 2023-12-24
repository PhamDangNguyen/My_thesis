import cv2


# Đường dẫn đến video
video_path = 'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/video_data/2.mp4'

# Mở video để đọc
cap = cv2.VideoCapture(video_path)

# Kiểm tra xem video đã mở thành công hay chưa
if not cap.isOpened():
    print("Không thể mở video.")
else:
    frame_count = 0  # Biến đếm số frame đã đọc

    while True:
        # Đọc frame từ video
        ret, frame = cap.read()
        frame_crop = frame[250:900,525:1265]
        print(frame.shape)
        # Kiểm tra xem đã đọc hết video hay chưa
        if not ret:
            break
        # Vẽ hình chữ nhật bằng vùng frame_crop trên frame gốc
        x1, y1, x2, y2 = 525, 250, 1265, 900
        cv2.imwrite(f'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/upload/{frame_count}_2.png',frame_crop)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Xử lý frame ở đây (ví dụ: hiển thị frame)
        cv2.imshow('Frame', frame)

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