import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

from file_operations import get_sorted_files, get_image_paths

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

def display_image(image, window_name='Image'):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def main():
    base_options = python.BaseOptions(model_asset_path='helpers/face_landmarker_v2_with_blendshapes.task')
    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                            output_face_blendshapes=True,
                                            output_facial_transformation_matrixes=True,
                                            num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)

    data_path = "gen-data"
    image_files = get_sorted_files(data_path)

    annotated_images = []
    for file_name in image_files:
        image_path = get_image_paths(data_path, file_name)
        image = mp.Image.create_from_file(image_path)

        img_rgb = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

        # Detect face landmarks from the input image.
        detection_result = detector.detect(image)

        # Process the detection result. In this case, visualize it.
        annotated_image = draw_landmarks_on_image(img_rgb, detection_result)
        annotated_images.append(annotated_image)

    # Create a figure with annotated images
    figure = np.concatenate(annotated_images, axis=1)
    display_image(cv2.cvtColor(figure, cv2.COLOR_RGB2BGR))

if __name__ == "__main__":
    main()