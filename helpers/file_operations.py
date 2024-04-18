import os

def get_sorted_files(path):
    """
    Returns a sorted list of files in the given directory path, excluding hidden files.
    If the path is a file, it returns a list containing the file name.
    """
    if os.path.isfile(path):
        return [path]
    else:
        files = [file for file in os.listdir(path) if not file.startswith('.')]
        return sorted(files)

def get_image_paths(data_path, file_name):
    """
    Returns the absolute path of an image file given its directory path and file name.
    """
    if os.path.isfile(data_path):
        return data_path
    return os.path.join(data_path, file_name)
