from deepface import DeepFace
from helpers.file_operations import get_sorted_files, get_image_paths
from plot_view import plot_verification_results

def compare_faces_deepface(real_data_path, gen_data_path, save_locally=False):
    real_data_files = get_sorted_files(real_data_path)
    gen_data_files = get_sorted_files(gen_data_path)

    # Ensure both folders have an equal number of images
    if len(real_data_files) != len(gen_data_files):
        raise ValueError("Number of images in 'real-data' and 'gen-data' folders must be the same.")

    verification_results = []
    distances = []
    distance_threshold = 0.68

    for real_file, gen_file in zip(real_data_files, gen_data_files):
        real_image_path = get_image_paths(real_data_path, real_file)
        gen_image_path = get_image_paths(gen_data_path, gen_file)

        result = DeepFace.verify(real_image_path, gen_image_path,
                                 model_name="ArcFace",
                                 detector_backend='retinaface')

        verification_results.append(result["verified"])
        distances.append(result["distance"])
        distance_threshold = result["threshold"]

        print(f"Comparison between {real_file} and {gen_file}: {result['verified']} with distance {result['distance']}")

    # plot_verification_results(verification_results, distances, distance_threshold, save_locally)
    return verification_results, distances
