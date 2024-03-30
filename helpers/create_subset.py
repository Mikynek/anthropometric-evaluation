import os
import shutil
import random
import argparse
import zipfile
import tempfile

def extract_zip_to_temp(source_zip):
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(source_zip, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    return temp_dir

def copy_random_images(source, destination_dir, num_images):
    if source.endswith('.zip'):
        temp_dir = extract_zip_to_temp(source)
        source_dir = temp_dir
    else:
        source_dir = source

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

    # Clean up the temporary directory if created
    if source.endswith('.zip'):
        shutil.rmtree(temp_dir)

def parse_arguments_create_subset():
    parser = argparse.ArgumentParser(description='Copy random images from a source directory or zip file to a destination directory.')
    parser.add_argument('-s', '--source', required=True, help='Source directory or zip file path')
    parser.add_argument('-d', '--destination', required=True, help='Destination directory path')
    parser.add_argument('-n', '--num', type=int, default=75, help='Number of random images to copy (default: 75)')
    args = parser.parse_args()

    copy_random_images(args.source, args.destination, args.num)

if __name__ == "__main__":
    parse_arguments()