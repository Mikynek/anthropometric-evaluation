from deepface import DeepFace
import matplotlib.pyplot as plt
from file_operations import get_sorted_files, get_image_paths

def compare_faces(real_data_path, gen_data_path):
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

        result = DeepFace.verify(real_image_path, gen_image_path, model_name="ArcFace", detector_backend='retinaface')

        verification_results.append(result["verified"])
        distances.append(result["distance"])
        distance_threshold = result["threshold"]

        print(f"Comparison between {real_file} and {gen_file}: {result['verified']} with distance {result['distance']}")

    plot_verification_results(verification_results, distances, distance_threshold)
    print_verification_statistics(verification_results)

def plot_verification_results(verification_results, distances, distance_threshold):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plot_pie_chart(verification_results)
    plt.title('Verification Results')

    plt.subplot(1, 2, 2)
    plot_distance_scatter(distances, distance_threshold)
    plt.title('Face Distance for Each Pair')
    plt.xlabel('Pair Number')
    plt.ylabel('Face Distance')

    plt.tight_layout()
    plt.show()

def plot_pie_chart(verification_results):
    success_count = verification_results.count(True)
    failure_count = verification_results.count(False)

    plt.pie([success_count, failure_count], labels=['Success', 'Failure'], explode=(0, 0.1),
            colors=['green', 'red'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), pctdistance=0.4)
    plt.gca().add_artist(plt.Circle((0, 0), 0.3, color='white'))

def plot_distance_scatter(distances, distance_threshold):
    plt.scatter(range(1, len(distances)+1), distances, color='blue')
    plt.axhline(y=distance_threshold, color='r', linestyle='--', label=f'Threshold ({distance_threshold})')

def print_verification_statistics(verification_results):
    success_count = verification_results.count(True)
    failure_count = verification_results.count(False)

    print("\nVerification Statistics:")
    print(f"Total Pairs: {len(verification_results)}")
    print(f"Successful Verifications: {success_count}")
    print(f"Failed Verifications: {failure_count}")

    if len(verification_results) > 0:
        success_rate = success_count / len(verification_results) * 100
        print(f"Success Rate: {success_rate:.2f}%")
    else:
        print("No pairs to verify.")