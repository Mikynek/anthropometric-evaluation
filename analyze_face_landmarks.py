import argparse
from face_comparison_deepface import compare_faces_deepface
from face_comparison_mediapipe import compare_faces_mediapipe
from experiments_statistics import print_verification_statistics_deepface

parser = argparse.ArgumentParser(description="Compare faces using DeepFace and MediaPipe.")
parser.add_argument('-r', '--real', required=True, help='Directory or zip file name for real images')
parser.add_argument('-g', '--generated', required=True, help='Directory or zip file name for generated images')
parser.add_argument("-l", "--locally", action="store_true", help="Save plots locally.")

args = parser.parse_args()

verification_results, distances = compare_faces_deepface(args.real, args.generated, save_locally=args.locally)
compare_faces_mediapipe(args.real, args.generated)
print_verification_statistics_deepface(verification_results, distances)
