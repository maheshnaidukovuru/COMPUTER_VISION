import cv2

# Open the video file
cap = cv2.VideoCapture(r"C:\\Users\91628\Downloads\Tu Hi To - Sameer Khan_HD-(PagalWorld.video).mp4")

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Start from the last frame
current_frame = total_frames - 1

while current_frame >= 0:
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow('Video in Reverse', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    current_frame -= 1

cap.release()
cv2.destroyAllWindows()
