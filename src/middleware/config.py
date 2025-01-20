import json

# Module-level variables to hold config values
app_name = None
source_strings_file = None
resources_dir = None

def load_config(json_file):
    """
    Reads a JSON file and sets module-level variables based on its contents.

    :param json_file: Path to the JSON configuration file.
    """
    global app_name, source_strings_file, resources_dir

    try:
        with open(json_file, "r") as file:
            config = json.load(file)

        # Extract variables from JSON
        app_name = config.get("app_name")
        source_strings_file = config.get("source_strings_file")
        resources_dir = config.get("resources_dir")

        if not app_name or not source_strings_file or not resources_dir:
            raise ValueError("Missing required fields in configuration file.")

    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {json_file}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {json_file}")
