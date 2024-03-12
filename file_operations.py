import os

def get_sorted_files(path):
    return sorted([file for file in os.listdir(path) if not file.startswith('.')])

def get_image_paths(data_path, file_name):
    return os.path.join(data_path, file_name)
