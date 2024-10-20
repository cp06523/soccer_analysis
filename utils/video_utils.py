import cv2

###### THIS IS THE ORIGINAL FUNCTION ######################
# def read_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     frames = []
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frames.append(frame)
#     return frames
#############################################################
###### REPLACING WITH generate_frames() FROM football player object tracking nb  BUT KEEPING NAME AS read_video() #######

def read_video(video_file: str) -> Generator[np.ndarray, None, None]:
    video = cv2.VideoCapture(video_file)
    # print(video.isOpened())
    while video.isOpened():
        success, frame = video.read()
        # print(f"Success: {success}, Frame shape: {frame.shape if frame is not None else None}")  # Add this line
        if not success:
          # print('no success')
          break
        yield frame
def save_video(ouput_video_frames,output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (ouput_video_frames[0].shape[1], ouput_video_frames[0].shape[0]))
    for frame in ouput_video_frames:
        out.write(frame)
    out.release()
