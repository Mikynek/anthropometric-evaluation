"""
This script is used to draw landmarks on an image using MediaPipe FaceLandmarker.
The script takes an image as input and outputs an image with landmarks drawn on it.
The output image is saved in the same directory as the input image with "_landmarks" appended to the filename.

This script was partly retrieved from The MediaPipe Authors.
  Title: Face Landmarks Detection with MediaPipe Tasks
  Authors: Lugaresi, Camillo and Tang, Jiuqiang and Nash, Hadon and McClanahan, Chris and Uboweja, Esha and Hays, Michael and Zhang, Fan and Chang, Chuo-Ling and Yong, Ming and Lee, Juhyun and others
  Date: 2023
  Availability: https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/face_landmarker/python/%5BMediaPipe_Python_Tasks%5D_Face_Landmarker.ipynb
  License: Apache License 2.0
"""

import cv2
import numpy as np
import argparse
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

def draw_landmarks_on_image(rgb_image, detection_result):
  face_landmarks_list = detection_result.face_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected faces to visualize.
  for idx in range(len(face_landmarks_list)):
    face_landmarks = face_landmarks_list[idx]

    # Draw the face landmarks.
    face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    face_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
    ])

    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_tesselation_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_contours_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_IRISES,
          landmark_drawing_spec=None,
          connection_drawing_spec=mp.solutions.drawing_styles
          .get_default_face_mesh_iris_connections_style())

  return annotated_image

def get_image_with_landmarks(image_path):
    base_options = python.BaseOptions(model_asset_path='helpers/face_landmarker_v2_with_blendshapes.task')
    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                            output_face_blendshapes=True,
                                            output_facial_transformation_matrixes=True,
                                            num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)

    image = mp.Image.create_from_file(image_path)
    img_rgb = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

    detection_result = detector.detect(image)
    annotated_image = draw_landmarks_on_image(img_rgb, detection_result)

    # Save the annotated image
    output_path = image_path.replace(".jpg", "_landmarks.jpg")
    cv2.imwrite(output_path, cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
    print(f"Annotated image saved at: {output_path}")

def parse_arguments_landmarks():
  parser = argparse.ArgumentParser(description='Create image with landmarks.')
  parser.add_argument('-s', '--source', required=True, help='Source image path')
  args = parser.parse_args()

  get_image_with_landmarks(image_path=args.source)

if __name__ == "__main__":
    parse_arguments_landmarks()