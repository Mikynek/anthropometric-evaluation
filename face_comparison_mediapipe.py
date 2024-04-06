import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from helpers.file_operations import get_sorted_files, get_image_paths
from helpers.landmark_info import FACE_PROPORTIONS

def max_absolute_proportion(proportions):
    max_value = 0
    max_key = None
    for key, value in proportions.items():
        if abs(value) > max_value:
            max_value = abs(value)
            max_key = key

    return max_key, max_value

def compare_proportions(proportions1, proportions2):
    results = {}
    for key in proportions1:
        results[key] = proportions1[key] - proportions2[key]

    return results

def measure_face_proportions(landmarks):
    distances = {}
    for landmark in FACE_PROPORTIONS:
        distance = calculate_distances(landmarks[landmark.start], landmarks[landmark.end])
        distances[landmark.name] = distance

    return distances

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
        real_landmarks = detection_result_real.face_landmarks[0]
        real_proportions = measure_face_proportions(real_landmarks)

        gen_image_path = get_image_paths(gen_data_path, gen_file)
        image_gen = mp.Image.create_from_file(gen_image_path)
        detection_result_gen = detector.detect(image_gen)
        gen_landmarks = detection_result_gen.face_landmarks[0]
        gen_proportions = measure_face_proportions(gen_landmarks)

        print(f"Comparison between {real_file} and {gen_file}")

        print(f"Real proportions: {real_proportions}")
        print(f"Gen proportions: {gen_proportions}")

        comparison_result = compare_proportions(real_proportions, gen_proportions)
        print()
        print(f"Comparison result: {comparison_result}")

        max_key, max_value = max_absolute_proportion(comparison_result)
        print(f"Max difference: {max_key} with value {max_value}")
        print("--------------------------------------------------------------------------------")

if __name__ == "__main__":
    real_data_path = "real-data"
    gen_data_path = "gen-data"
    compare_faces_mediapipe(real_data_path, gen_data_path)