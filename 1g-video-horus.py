import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_info(videoname, frames, framerate):
    print('----------------')
    print("Video:", videoname)
    print('----------------')
    print("Number of Frames:", len(frames))
    print("Frame Rate:", framerate)
    print('----------------')
    if len(frames) > 0:
        plot_info(videoname, frames)
    else:
        print("No frames to plot.")

def plot_info(videoname, frames):
    sTitle = 'Video Frames - ' + videoname
    plt.title(sTitle)
    sLegend = []
    for c in range(frames.shape[1]):
        sLabel = 'Frame' + str(c + 1)
        sLegend = sLegend + [str(c + 1)]
        plt.plot(frames[:, c], label=sLabel)
    plt.legend(sLegend)
    plt.show()

def video_to_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray_frame.flatten())
    cap.release()
    return np.array(frames)

# Example usage
sInputVideo = 'C:/Users/BHAVESH/Desktop/DS_PRACS/h.mp4'
print('=====================================================')
print('Processing Video:', sInputVideo)
print('=====================================================')
video_frames = video_to_frames(sInputVideo)
print("Size of video_frames:", video_frames.shape)  
show_info("Sample Video", video_frames, framerate=30) 

if video_frames.shape[0] > 0 and video_frames.shape[1] > 0:
    video_columns = [f'Pixel_{i+1}' for i in range(video_frames.shape[1])]
    video_df = pd.DataFrame(video_frames, columns=video_columns)
    video_output_file = 'D:/Nishant/Masters/pracexam/HORUS-Video.csv'
    video_df.to_csv(video_output_file, index=False)
    print('Video to HORUS - Done')
else:
    print('No frames to convert. Check the video file.')