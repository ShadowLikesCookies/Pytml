import os
import json

def read_increment_write(FileName, Directory, class_value=0, id_value=0):
    # Create or ensure the directory exists
    fetch_data_dir = Directory
    if not os.path.exists(fetch_data_dir):
        os.makedirs(fetch_data_dir)

    # Construct the file path
    file_path = os.path.join(fetch_data_dir, FileName)

    # If the file doesn't exist, create it with initial class and id values
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({"class": class_value, "id": id_value}, file)

    # Read the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
        value = data.get('id', 0)

    # Increment the id value
    value += 1

    # Update the id value and class value in the JSON data
    data['id'] = value
    data['class'] = class_value  # Update the class value separately

    # Write the updated JSON data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file)

    return value