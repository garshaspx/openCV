
import cv2
import os


def get_video_fps(video_path):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

fps = get_video_fps("C:\\Users\\amir2\\Videos\\h33.mp4")



def images_to_video(image_folder, output_path, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape

    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()



image_folder = "imgs_for_vid"
output_path = "videooo.mp4"

images_to_video(image_folder, output_path, int(fps))