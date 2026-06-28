import cv2
import sys
import os

vid_path = "site/assets/videos/oqueridinhodacidade_1782217218_3925843339656031279_77703762734.mp4"
out_path = "site/assets/images/ale_frame.jpg"

print(f"Reading {vid_path}")
cap = cv2.VideoCapture(vid_path)
if not cap.isOpened():
    print("Error opening video")
    sys.exit(1)

fps = cap.get(cv2.CAP_PROP_FPS)
target_frame = int(fps * 3.5) # 3.5 seconds, likely where he speaks "E o clima"
cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)

ret, frame = cap.read()
if ret:
    cv2.imwrite(out_path, frame)
    print("Frame saved successfully to", out_path)
else:
    print("Could not read frame")

cap.release()
