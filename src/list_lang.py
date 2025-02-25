import sys
from middleware import config
from middleware import input
from middleware.language import recognizeLanguage

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_config_file>")
        sys.exit(1)

    # Load configuration
    config_file = sys.argv[1]
    config.load_config(config_file)

    # Use config variables
    strings_files = input.collect_strings_files(config.resources_dir)

    for lang, item in strings_files.items():
        print(recognizeLanguage(lang))