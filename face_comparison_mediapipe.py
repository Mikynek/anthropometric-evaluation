import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from file_operations import get_sorted_files, get_image_paths

def compare_landmarks(landmarks1, landmarks2):
    pass


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
        gen_image_path = get_image_paths(gen_data_path, gen_file)

        image_real = mp.Image.create_from_file(real_image_path)
        detection_result_real = detector.detect(image_real)

        image_gen = mp.Image.create_from_file(gen_image_path)
        detection_result_gen = detector.detect(image_gen)

        print(f"Comparison between {real_file} and {gen_file}")
        comparison_result = compare_landmarks(detection_result_real.face_landmarks[0], detection_result_gen.face_landmarks[0])

if __name__ == "__main__":
    real_data_path = "real-data"
    gen_data_path = "gen-data"
    compare_faces_mediapipe(real_data_path, gen_data_path)