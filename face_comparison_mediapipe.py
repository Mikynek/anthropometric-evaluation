import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from file_operations import get_sorted_files, get_image_paths
    
def main():
    base_options = python.BaseOptions(model_asset_path='helpers/face_landmarker_v2_with_blendshapes.task')
    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                            output_face_blendshapes=True,
                                            output_facial_transformation_matrixes=True,
                                            num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)

    data_path = "test02"
    image_files = get_sorted_files(data_path)

    face_landmarks = []
    for file_name in image_files:
        image_path = get_image_paths(data_path, file_name)
        image = mp.Image.create_from_file(image_path)

        detection_result = detector.detect(image)

        print(f"Detected landmarks: {detection_result.face_landmarks}")
        face_landmarks.append(detection_result.face_landmarks)
        print(f"Detected face blendshapes: {detection_result.face_blendshapes}")
        print(f"Detected facial transformation matrixes: {detection_result.facial_transformation_matrixes}")

if __name__ == "__main__":
    main()