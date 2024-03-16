import os

def get_sorted_files(path):
    """
    Returns a sorted list of files in the given directory path, excluding hidden files.
    """
    files = [file for file in os.listdir(path) if not file.startswith('.')]
    return sorted(files)

def get_image_paths(data_path, file_name):
    """
    Returns the absolute path of an image file given its directory path and file name.
    """
    return os.path.join(data_path, file_name)
