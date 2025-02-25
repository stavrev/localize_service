import json


def convertToXML(partial_data):
    xml_output = []
    for key, value in partial_data.items():
        curated_value = replaceUnwantedCharacters(value)
        xml_output.append(f'    <string name="{key}">{curated_value}</string>')

    if len(xml_output) > 0:
        return "\n".join(xml_output)
    else:
        return ""


def replaceUnwantedCharacters(input: str):
    return (input
            .replace("'", "’")
            .replace("&", "&amp;")
            .replace("—", ", ")  # Seems a marker from chatGPT
    )


def update_resource_file(file_path, new_data):
    """
    Opens a file, removes the bottom "</resources>" (including trailing empty lines),
    appends new data, re-adds "</resources>", and writes the updated content back to the file.

    :param file_path: Path to the file to update.
    :param new_data: The data to append before "</resources>".
    """
    try:
        # Read the file content
        with open(file_path, "r") as file:
            content = file.read()

        # Remove the last "</resources>" using str.replace and keep one trailing line
        content = content.replace("</resources>", "").rstrip() + "\n"

        # Add the new data and re-add "</resources>"
        updated_content = content + new_data + "\n</resources>\n"

        # Write the updated content back to the file
        with open(file_path, "w") as file:
            file.write(updated_content)
    except Exception as e:
        print(f"Error updating file {file_path}: {e}")