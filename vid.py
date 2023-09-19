import cv2
import os


def get_video_fps(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) of the video
    fps = video.get(cv2.CAP_PROP_FPS)

    # Release the video file
    video.release()

    return fps

# Example usage
video_path = "path/to/your/video.mp4"
fps = get_video_fps("C:\\Users\\amir2\\Videos\\videoblocks-nested-sequence-09_s21fiifbq__1f2f6ac2a90dff7ec723cdb84d3daa75__P360.mp4")
print(f"The video has a frame rate of {fps} fps.")





def images_to_video(image_folder, output_path, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape

    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

# Example usage
image_folder = "imgs_for_vid"
output_path = "videooo.mp4"

images_to_video(image_folder, output_path, int(fps))