import json
import input

def missing_items(source_data, strings_files):
    """
    Identifies missing keys from source data in the given strings files.

    :param source_data: List of dictionaries with "data" (stringified JSON dict) and "meta" fields.
    :param strings_files: Dictionary mapping <lang-code> to <strings-file-location>.
    :return: Dictionary mapping <lang-code> to a dictionary with "file_path" and "data_to_translate".
    """
    result = {}

    # Read files and process
    for lang, file_path in strings_files.items():
        # Parse the language-specific data
        file_data = input.get_lang_data(file_path)
        try:
            file_dict = json.loads(file_data)  # Convert stringified JSON to dict
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {file_path}")

        # Initialize result for this language
        result[lang] = {
            "file_path": file_path,
            "data_to_translate": []
        }

        # Iterate over source data
        for item in source_data:
            try:
                source_dict = json.loads(item["data"])  # Convert stringified JSON to dict
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON in source data: {item}")

            # Check each key in the source dictionary
            missing_keys = {key: value for key, value in source_dict.items() if key not in file_dict}

            # If there are missing keys, add them to the result
            if missing_keys:
                result[lang]["data_to_translate"].append({
                    "data": json.dumps(missing_keys),  # Stringify the missing keys
                    "meta": item["meta"],
                })
    return result

