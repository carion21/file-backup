import json
from shutil import copyfile

def get_json_from_file(file_path):
    """
    Read a JSON file and return a dictionary.
    """
    with open(file_path, 'r') as f:
        return json.load(f)
    
def set_json_to_file(file_path, data):
    """
    Write a dictionary to a JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
        
def move_file(source, destination):
    """
    Move a file from source to destination.
    """
    print('Moving ' + source + ' to ' + destination + '...')
    copyfile(source, destination)