from middleware import input
import json
from services import translate
from middleware.language import recognizeLanguage
from middleware import output
from middleware import scan_files
from middleware import config
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_config_file>")
        sys.exit(1)

    # Load configuration
    config_file = sys.argv[1]
    config.load_config(config_file)

    # Use config variables
    strings_files = input.collect_strings_files(config.resources_dir)
    source_strings = input.get_source_data(config.source_strings_file)
    data_to_translate = scan_files.missing_items(source_strings, strings_files)

    # Check if no translation is required
    has_translation = False

    for key, value in data_to_translate.items():
        if len(value["data_to_translate"]) > 0:
            has_translation = True
            print(f"Language: {key} has {len(value['data_to_translate'])} parts")

    if has_translation:
        print(f"Running for app {config.app_name}")
    else:
        print(f"All up to date with {config.app_name}")

    for key, value in data_to_translate.items():
        parts_amount = len(value["data_to_translate"])
        if parts_amount > 0:
            langName = recognizeLanguage(key)
            itemCount = 1
            print(langName)

            for item in value["data_to_translate"]:
                partial_result = translate.runOne(item["data"], item["meta"], langName)
                json_partial = {}
                try:
                    json_partial = json.loads(partial_result)
                except json.JSONDecodeError:
                    # make a second attempt if the LLM gets the first wrongfully
                    try:
                        json_partial = json.loads(partial_result)
                    except json.JSONDecodeError:
                        raise ValueError("Could not convert to json, partial_result: ", partial_result)

                xml_partial = output.convertToXML(json_partial)
                if xml_partial:
                    output.update_resource_file(value["file_path"], xml_partial)
                    print(f"\rPart {itemCount} of {parts_amount} written.", end="")

                itemCount += 1

            print("\n")


