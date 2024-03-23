import os
import shutil
import random

def copy_random_images(source_dir, destination_dir, num_images=80):
    # Get a list of all files in the source directory
    all_images = os.listdir(source_dir)
    
    # Ensure the destination directory exists, create it if necessary
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Choose random images from the list
    selected_images = random.sample(all_images, min(num_images, len(all_images)))

    # Copy selected images to the destination directory with sequential names
    for i, image in enumerate(selected_images, start=1):
        source_path = os.path.join(source_dir, image)
        destination_path = os.path.join(destination_dir, f"{i:03d}.jpg")
        shutil.copy2(source_path, destination_path)
        print(f"Copied {image} to {destination_path}")

if __name__ == "__main__":
    # Replace these paths with your actual directory paths
    source_directory = "/Users/jakubmikysek/Documents/FIT_VUT/BP/anthropometric-evaluation/CelebA-HQ-img"
    destination_directory = "/Users/jakubmikysek/Documents/FIT_VUT/BP/anthropometric-evaluation/real-data"

    # Specify the number of random images to copy (default is 80)
    num_random_images = 15

    copy_random_images(source_directory, destination_directory, num_random_images)