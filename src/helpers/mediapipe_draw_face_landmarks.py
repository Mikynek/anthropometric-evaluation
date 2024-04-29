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

LANDMARK_INDEXES = {
    'G': 9,
    'TR': 10,
    'GN': 152,
    'ZY_L': 127,
    'ZY_R': 356,
    'GO_L': 58,
    'GO_R': 288,
    'EX_L': 33,
    'EN_L': 133,
    'EX_R': 263,
    'EN_R': 362,
    'SN': 2,
    'N': 8,
    'AL_L': 49,
    'AL_R': 279,
    'CH_L': 61,
    'CH_R': 308,
    'LS': 0,
    'STO_LS': 13,
    'LI': 17,
    'STO_LI': 14
}

def draw_landmark(landmark, label, image):
    """Draws a single landmark and its label on the image."""
    x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
    # Draw the point as a green circle
    cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    # Overlay the index label next to the point
    cv2.putText(image, str(label), (x + 5, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1, cv2.LINE_AA)

def draw_specific_landmarks_on_image(rgb_image, detection_result):
    face_landmarks_list = detection_result.face_landmarks
    annotated_image = np.copy(rgb_image)
    
    for face_landmarks in face_landmarks_list:
        for label, idx in LANDMARK_INDEXES.items():
            if idx < len(face_landmarks):
                draw_landmark(face_landmarks[idx], label, annotated_image)
                
    return annotated_image

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
    annotated_image_points = draw_specific_landmarks_on_image(img_rgb, detection_result)

    output_path = image_path.replace(".jpg", "_landmarks.png")
    cv2.imwrite(output_path, cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
    print(f"Annotated image saved at: {output_path}")

    output_path = image_path.replace(".jpg", "_landmarks_specific.png")
    cv2.imwrite(output_path, cv2.cvtColor(annotated_image_points, cv2.COLOR_RGB2BGR))
    print(f"Annotated specific image saved at: {output_path}")

def parse_arguments_landmarks():
  parser = argparse.ArgumentParser(description='Create image with landmarks.')
  parser.add_argument('-s', '--source', required=True, help='Source image path')
  args = parser.parse_args()

  get_image_with_landmarks(image_path=args.source)

if __name__ == "__main__":
    parse_arguments_landmarks()