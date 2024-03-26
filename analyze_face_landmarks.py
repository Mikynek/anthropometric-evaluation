import argparse
from face_comparison_deepface import compare_faces_deepface

# Example usage
real_data_path = 'real-data'
gen_data_path = 'gen-data'

# Check command-line arguments for saving plots locally
parser = argparse.ArgumentParser(description="Compare faces using DeepFace.")
parser.add_argument("-l", "--locally", action="store_true", help="Save plots locally.")

args = parser.parse_args()

compare_faces_deepface(real_data_path, gen_data_path, save_locally=args.locally)
