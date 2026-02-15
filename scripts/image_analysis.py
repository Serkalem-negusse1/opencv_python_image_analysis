import cv2
import os

# Paths
image_path = r"E:/AASTU PhD/Presentations/Year 1 Semester 2/ComputerVision/opencv_python_image_analysis/dataset/butterfly.jpg"
save_dir = r"E:/AASTU PhD/Presentations/Year 1 Semester 2/ComputerVision/opencv_python_image_analysis/results/"

# Make sure image exists
if not os.path.exists(image_path):
    print("Error: Image not found at", image_path)
    exit()

# Create results folder if it doesn't exist.
os.makedirs(save_dir, exist_ok=True)

# Load image
image = cv2.imread(image_path)
print("Image loaded successfully! Shape:", image.shape)

# Save original image
original_save_path = os.path.join(save_dir, "butterfly_original.jpg")
cv2.imwrite(original_save_path, image)
print("Original image saved as:", original_save_path)

# Convert to grayscale and save
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_save_path = os.path.join(save_dir, "butterfly_gray.jpg")
cv2.imwrite(gray_save_path, gray)
print("Grayscale image saved as:", gray_save_path)

# Apply Canny edge detection and save
edges = cv2.Canny(gray, 100, 200)
edges_save_path = os.path.join(save_dir, "butterfly_edges.jpg")
cv2.imwrite(edges_save_path, edges)
print("Edge-detected image saved as:", edges_save_path)

print("All processing done!")
