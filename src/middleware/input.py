import sys
import os
import json

# Add the current directory to the Python module search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parse

def read_file(filename):
    """
    Reads the contents of a file and returns it as a string.

    :param filename: Path to the file to be read.
    :return: Contents of the file as a string.
    :raises FileNotFoundError: If the file does not exist.
    :raises IOError: If there is an error reading the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")


def extract_data(array_data):
    """
    Processes an array of strings and returns an array of dictionaries
    with `text_data` and `meta_data` fields, excluding items with empty "data".

    :param array_data: List of strings to process.
    :return: List of dictionaries with `text_data` and `meta_data`.
    """

    # Process each string in the input array and construct the result
    result = [
        {
            "data": data,
            "meta": parse.get_meta(item),
        }
        for item in array_data
        if (data := parse.get_data(item)) and json.loads(data)  # Ensure "data" is not empty JSON
    ]

    return result


def collect_strings_files(res_dir):
    """
    Scans a directory for subdirectories named "values-<lang_code_str>",
    checks for the presence of "strings.xml" inside them, and collects their paths.

    :param res_dir: The base resource directory to scan.
    :return: A dictionary mapping <lang_code_str> to the file path of "strings.xml".
    """
    result = {}

    # Iterate over the subdirectories in the given directory
    for subdir in os.listdir(res_dir):
        subdir_path = os.path.join(res_dir, subdir)

        # Check if it's a directory and matches the "values-<lang_code_str>" pattern
        if os.path.isdir(subdir_path) and subdir.startswith("values-"):
            lang_code = subdir.split("values-")[1]
            strings_file_path = os.path.join(subdir_path, "strings.xml")

            # Check if "strings.xml" exists in this directory
            if os.path.isfile(strings_file_path):
                result[lang_code] = strings_file_path

    return result


def get_source_data(file_path):
    raw_data = read_file(file_path)
    raw_data = parse.remove_heading_tags(raw_data)
    array_data = parse.split_strings_file(raw_data)
    parsed_data = extract_data(array_data)
    return parsed_data


def get_lang_data(file_path):
    raw_data = read_file(file_path)
    raw_data = parse.remove_heading_tags(raw_data)
    parsed_data = parse.get_data(raw_data)
    return parsed_data

