import matplotlib.pyplot as plt
from matplotlib import rcParams

# Thiết lập font chữ toàn cục
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = 'Times New Roman'

# Tạo dữ liệu
x = [3, 4, 5, 6, 7, 8]
y1 = [0.72, 0.83, 0.84, 0.87, 0.91, 0.93]
y2 = [0.81, 0.82, 0.86, 0.86, 0.9, 0.91]
y3 = [0.77, 0.72, 0.87, 0.87, 0.94, 0.96]

# Vẽ đồ thị
plt.plot(x, y1, label="YOLOv5", color="red", linewidth=2.0, marker="*", markersize=10)
plt.plot(x, y2, label="YOLOv7", color="green", linewidth=2.0, marker="x", markersize=10, markeredgewidth=2)
plt.plot(x, y3, label="YOLOv8", color="blue", linewidth=2.0, marker="p", markersize=10)

# Thêm tiêu đề và chú thích
plt.title("Accuracy of testset droplets", fontsize=20)
plt.xlabel("Number of counting frames", fontsize=16)
plt.ylabel("Accuracy(%)", fontsize=16)
plt.legend(fontsize=14)

# Tùy chỉnh trục x và y
plt.xticks(x, fontsize=14)
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=14)
plt.ylim(0, 1)

# Xuất ảnh đồ thị
plt.savefig("3Version.png", dpi=1300)

# Hiển thị đồ thị
plt.show()
