import re
import json


def get_data(xml_string):
    """
    Converts XML-like elements in a string to a JSON dictionary string,
    ignoring elements with translatable="false".

    :param xml_string: A string containing XML-like elements.
    :return: A JSON string representing the elements as key-value pairs.
    """
    # Use regex to extract 'name' attribute and the inner text of <string> elements,
    # while capturing optional 'translatable="false"'
    pattern = r'<string name="(.*?)"(?:\s+translatable="false")?>(.*?)</string>'
    matches = re.findall(pattern, xml_string)

    # Convert matches to a dictionary, excluding items that have translatable="false"
    result_dict = {name: value for name, value in matches if f'name="{name}" translatable="false"' not in xml_string}

    # Convert the dictionary to a JSON string
    return json.dumps(result_dict, ensure_ascii=False, indent=4)


def get_meta(input_string):
    """
    Removes all <string name="...">...</string> elements from the input string.

    :param input_string: The input string containing XML-like elements.
    :return: The remaining string after removing the matched elements.
    """
    # Regex pattern to match <string name="...">...</string>
    pattern = r'<string name=".*?">.*?</string>'
    # Use re.sub to remove all matches
    result = re.sub(pattern, '', input_string)
    # Return the cleaned string, stripping unnecessary whitespace
    result = result.replace("<!--", "").replace("-->", "")
    return result.strip()


def split_strings_file(file_data):
    """
    Splits the input file data into an array of strings based on the pattern
    '\n<any-whitespace-characters>\n'.

    :param file_data: The string content of the file.
    :return: List of strings split by the specified pattern.
    """
    # Use regex to split on the pattern: newline, optional whitespace, newline
    return re.split(r'\n\s*\n', file_data)


def remove_heading_tags(file_data):
    return (file_data
        .replace("</resources>", "")
        .replace("<resources>", "")
        .replace('<?xml version="1.0" encoding="utf-8"?>', "")
    ).strip()