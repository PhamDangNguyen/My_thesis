import cv2

def find_cnts(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.GaussianBlur(gray,(11,11),0)
    canny_cv = cv2.Canny(gray1,650,1150,apertureSize=5,L2gradient= True)
    canny_cv_ = cv2.dilate(canny_cv, None, iterations=4)
    canny_cv_1 = cv2.erode(canny_cv_, None, iterations=3)
    cnts, hierarchy = cv2.findContours(canny_cv_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return gray,gray1,canny_cv,canny_cv_1,cnts

def draw_square_around_objects(img, cnts):
    # Make a copy of the original image to draw on
    img_copy = img.copy()

    for cnt in cnts:
        # Get the coordinates of the bounding rectangle
        x, y, w, h = cv2.boundingRect(cnt)

        # Draw a green square around the object
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img_copy

def read_video(video_path):
    # Mở video để đọc
    cap = cv2.VideoCapture(video_path)

    # Kiểm tra xem video đã mở thành công hay chưa
    if not cap.isOpened():
        print("Không thể mở video.")
        return
    i = 0
    while True:
        # Đọc frame từ videoq
        ret, frame = cap.read()
        print(frame.shape)
        frame_sub = frame[200:900,800:980]
        # Kiểm tra xem đã đọc hết video hay chưa
        if not ret:
            break

        # cnts = find_cnts(frame_sub)
        # cv2.drawContours(frame_sub, cnts, -1, (0, 255, 0), 2)

        # Xử lý frame ở đây (ví dụ: hiển thị frame)
        cv2.imshow('Frame', frame_sub)
        cv2.imwrite(f'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Data_vinhua/Paper/{i}.png',frame_sub)
        i=i+1
        
        # cv2.imshow("cnt",cnts)

        # Để thoát vòng lặp, bạn có thể nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên khi xong
    cap.release()
    cv2.destroyAllWindows()


def read_img(img_path):
    img = cv2.imread(img_path)
    gray,blur,canny_cv,dilate_img,cnts = find_cnts(img)
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
    cv2.imwrite(f'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Data_vinhua/Paper/2_cnts.png',img)
    cv2.imshow('test',img)
    cv2.waitKey(0)
if __name__ == '__main__':
    video_path = 'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/video_data/1.mp4'
    img_path = 'C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Data_vinhua/Paper/2.png'
    # read_video(video_path=video_path)
    read_img(img_path=img_path)
