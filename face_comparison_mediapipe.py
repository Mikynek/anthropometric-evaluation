import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from helpers.file_operations import get_sorted_files, get_image_paths

def compare_landmarks(landmarks1, landmarks2):
    pass

def calculate_distances(landmark1, landmark2):
    # Calculate the Euclidean distance between two 3D points
    distance = math.sqrt((landmark2.x - landmark1.x) ** 2 +
                         (landmark2.y - landmark1.y) ** 2 +
                         (landmark2.z - landmark1.z) ** 2)
    return distance


def compare_faces_mediapipe(real_data_path, gen_data_path):
    base_options = python.BaseOptions(model_asset_path='helpers/face_landmarker_v2_with_blendshapes.task')
    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                            output_face_blendshapes=True,
                                            output_facial_transformation_matrixes=True,
                                            num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)

    real_data_files = get_sorted_files(real_data_path)
    gen_data_files = get_sorted_files(gen_data_path)

    # Ensure both folders have an equal number of images
    if len(real_data_files) != len(gen_data_files):
        raise ValueError("Number of images in 'real-data' and 'gen-data' folders must be the same.")

    for real_file, gen_file in zip(real_data_files, gen_data_files):
        real_image_path = get_image_paths(real_data_path, real_file)
        image_real = mp.Image.create_from_file(real_image_path)
        detection_result_real = detector.detect(image_real)

        gen_image_path = get_image_paths(gen_data_path, gen_file)
        image_gen = mp.Image.create_from_file(gen_image_path)
        detection_result_gen = detector.detect(image_gen)

        print(f"Comparison between {real_file} and {gen_file}")
        real_landmarks = detection_result_real.face_landmarks[0]
        gen_landmarks = detection_result_gen.face_landmarks[0]

        print("Real landmarks sn:", real_landmarks[2].x, real_landmarks[2].y, real_landmarks[2].z)
        print("Real landmarks n:", real_landmarks[8].x, real_landmarks[8].y, real_landmarks[8].z)
        print("Gen landmarks sn:", gen_landmarks[2].x, gen_landmarks[2].y, gen_landmarks[2].z)
        print("Gen landmarks n:", gen_landmarks[8].x, gen_landmarks[8].y, gen_landmarks[8].z)

        real_distance = calculate_distances(real_landmarks[2], real_landmarks[8])
        gen_distance = calculate_distances(gen_landmarks[2], gen_landmarks[8])

        print(f"Real distance: {real_distance}")
        print(f"Gen distance: {gen_distance}")
        print("--------------------------------------------------------------------------------")

        # comparison_result = compare_landmarks(real_landmarks, gen_landmarks)

if __name__ == "__main__":
    real_data_path = "real-data"
    gen_data_path = "gen-data"
    compare_faces_mediapipe(real_data_path, gen_data_path)