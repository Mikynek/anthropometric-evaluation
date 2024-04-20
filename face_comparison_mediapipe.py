import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from experiments_statistics import print_analysis_statistics, print_tfi_statistics
from helpers.file_operations import get_sorted_files, get_image_paths
from helpers.landmark_info import FACE_PROPORTIONS, TFI, MaxDifference

def calculate_distances(landmark1, landmark2):
    """Calculate the Euclidean distance between two 3D points."""
    return math.sqrt((landmark2.x - landmark1.x) ** 2 +
                     (landmark2.y - landmark1.y) ** 2 +
                     (landmark2.z - landmark1.z) ** 2)

def calculate_TFI(height, width):
    """Calculate TFI (Total Facial Index) based on distances."""
    return ( height * 100 ) / width

def max_absolute_proportion_difference(proportions):
    """Find the maximum absolute difference in proportions."""
    max_value = 0
    max_key = None
    for key, value in proportions.items():
        if abs(value) > max_value:
            max_value = abs(value)
            max_key = key

    return max_key, max_value

def compare_proportions(proportions1, proportions2):
    """Compare proportions between two sets."""
    results = {}
    for key in proportions1:
        results[key] = proportions1[key] - proportions2[key]

    return results

def measure_face_proportions(landmarks, proportions=FACE_PROPORTIONS):
    """Measure face proportions based on landmarks."""
    distances = {}
    for landmark in proportions:
        distance = calculate_distances(landmarks[landmark.start], landmarks[landmark.end])
        distances[landmark.name] = distance

    return distances

def compare_faces_mediapipe(real_data_path, gen_data_path):
    print("\nComparing faces using MediaPipe...")
    base_options = python.BaseOptions(model_asset_path='helpers/face_landmarker_v2_with_blendshapes.task')
    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                            output_face_blendshapes=True,
                                            output_facial_transformation_matrixes=True,
                                            num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)

    real_data_files = get_sorted_files(real_data_path)
    gen_data_files = get_sorted_files(gen_data_path)

    max_differences = {}

    real_facial_height = []
    real_facial_width = []
    real_tfi = []

    gen_facial_height = []
    gen_facial_width = []
    gen_tfi = []

    # Ensure both folders have an equal number of images
    if len(real_data_files) != len(gen_data_files):
        raise ValueError("Number of images in 'real-data' and 'gen-data' folders must be the same.")

    for real_file, gen_file in zip(real_data_files, gen_data_files):
        # Process real image
        real_image_path = get_image_paths(real_data_path, real_file)
        image_real = mp.Image.create_from_file(real_image_path)
        detection_result_real = detector.detect(image_real)
        real_landmarks = detection_result_real.face_landmarks[0]
        real_proportions = measure_face_proportions(real_landmarks)

        real_proportions_tfi = measure_face_proportions(real_landmarks, TFI)
        real_facial_height.append(real_proportions_tfi[TFI[0].name])
        real_facial_width.append(real_proportions_tfi[TFI[1].name])
        real_facial_index = calculate_TFI(real_facial_height[-1], real_facial_width[-1])
        real_tfi.append(real_facial_index)

        # Process generated image
        gen_image_path = get_image_paths(gen_data_path, gen_file)
        image_gen = mp.Image.create_from_file(gen_image_path)
        detection_result_gen = detector.detect(image_gen)
        gen_landmarks = detection_result_gen.face_landmarks[0]
        gen_proportions = measure_face_proportions(gen_landmarks)

        gen_proportions_tfi = measure_face_proportions(gen_landmarks, TFI)
        gen_facial_height.append(gen_proportions_tfi[TFI[0].name])
        gen_facial_width.append(gen_proportions_tfi[TFI[1].name])
        gen_facial_index = calculate_TFI(gen_facial_height[-1], gen_facial_width[-1])
        gen_tfi.append(gen_facial_index)

        print(f"Comparison between {real_file} and {gen_file}")

        comparison_result = compare_proportions(real_proportions, gen_proportions)

        max_key, max_value = max_absolute_proportion_difference(comparison_result)

        if max_key in max_differences:
            max_differences[max_key].count += 1
            max_differences[max_key].value += max_value
        else:
            max_differences[max_key] = MaxDifference(value=max_value, count=1)

    print_analysis_statistics(max_differences)
    print_tfi_statistics(real_facial_height, real_facial_width, real_tfi, gen_facial_height, gen_facial_width, gen_tfi)

if __name__ == "__main__":
    real_data_path = "real-data"
    gen_data_path = "gen-data"
    compare_faces_mediapipe(real_data_path, gen_data_path)