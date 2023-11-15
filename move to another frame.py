import cv2

# Load the source and destination frames
source_frame = cv2.imread("source_frame.png")
destination_frame = cv2.imread("destination_frame.png")

# Define the coordinates where you want to move the image
x_offset, y_offset = 100, 100  # Change these values to move the image to a different location

# Get the dimensions of the source image
image_height, image_width, _ = source_frame.shape

# Copy the source image to the specified coordinates on the destination frame
destination_frame[y_offset:y_offset + image_height, x_offset:x_offset + image_width] = source_frame

# Display or save the destination frame with the moved image
cv2.imshow("Moved Image", destination_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
