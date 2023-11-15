import cv2

# Load the input image (resized_img) and watermark image (resized_wm)
resized_wm = cv2.imread(r"C:\\Users\91628\OneDrive\Pictures\images.jpeg")
resized_img = cv2.imread(r"C:\\Users\91628\OneDrive\Pictures\images.jpeg")

h_img, w_img, _ = resized_img.shape
center_y = int(h_img/2)
center_x = int(w_img/2)
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
roi = resized_img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(resized_wm, 0.3, roi, 1, 0)
resized_img[top_y:bottom_y, left_x:right_x] = result
filename = "C:/Users/Merwin S/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/32508F53F24C46F685870A075EAAA29C/WhatsApp Image 2023-10-16 at 13.54.13_3e6dfcb5.jpg"
cv2.imwrite(filename, resized_img)
cv2.imshow("Resized Input Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
