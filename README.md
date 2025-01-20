
# Localize Service with LLM (for Android)

## Overview

This project provides a Python-based solution to **translate `strings.xml` files** from a default language into localized `strings.xml` files for other languages or regions. 

The script:
- Fills empty `strings.xml` files in localization directories.
- Adds missing translations incrementally to existing files.
- Uses **meta instructions** provided in comments for accurate and context-aware translations.
- Supports **only flat `strings.xml` files** (no nested structures).

This is **version 1.0**, and while it might lack some features, it is practical and actively used. Contributions are highly encouraged to improve its functionality.

---

## Features

1. **Incremental Localization**:
   - Translates only missing items in existing `strings.xml` files.
   - Writes each translated chunk to the corresponding file immediately, ensuring changes are traceable.

2. **Context-Aware Translation**:
   - Leverages meta instructions provided in comments for localization accuracy, ensuring natural and meaningful translations.

3. **Easy Language Addition**:
   - To add a new language or region, create a `values-<language_code>` directory and include an empty `strings.xml` file. The script will handle the rest.

4. **Flat `strings.xml` Support**:
   - Current support is limited to flat `strings.xml` files.

5. **Configurable for Multiple Apps**:
   - Manage multiple apps by creating separate JSON config files for each one.

---

## Requirements

- **Python 3.10 or higher**
- An **OpenAI API Key** set as an environment variable:
  ```bash
  export OPENAI_API_KEY=<your_openai_api_key>
  ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Set up the environment and install dependencies:
   ```bash
   ./setup.sh
   ```

3. Create a JSON config file for your app in the `config/` directory. Example:
   ```json
   {
     "app_name": "Your App Name",
     "source_strings_file": "/path/to/res/values/strings.xml",
     "resources_dir": "/path/to/res/"
   }
   ```

   - A sample config file (`ffa_app.json`) is provided for reference.

---

## Usage

To translate your strings:
```bash
./run.sh config/<config-file>.json
```

### Adding New Languages
1. Create a `values-<language_code>` directory in your `res/` folder.
2. Add an empty `strings.xml` file inside the directory.
3. Run the script, and it will populate the file with translations.

---

## Source `strings.xml` Format

The source `strings.xml` should:
1. Have **empty lines** between different items.
2. Include **comments** with meta instructions for context.

### Example
```xml
<!--
    Role: Company name, translate it as literally as possible, it is not important the meaning but its naming.
-->
<string name="company_name">FUSION AI EOOD</string>

<!--
    Role: Displayed in a drop-down menu to show nutrition information for the current day.
    Character Limit: ~10
-->
<string name="today">Today</string>

<!--
    Role Nutrients name shown to the user in a normal and short form.
    main title Maximum characters: 20
    short title maximum characters: 7 (any way of shortening and abbreviation of words)
    info part: make it informative and insightful.
-->
<string name="calories">Calories</string>
<string name="calories_short">Cal</string>
<string name="calories_info">You need energy for your body to work properly.</string>
```

---

## How It Works

1. **Step 1**: Reads the default `strings.xml` file and all `values-<language_code>/strings.xml` files.
2. **Step 2**: Parses the meta instructions and strings for translation context.
3. **Step 3**: Translates missing strings incrementally and writes results to the corresponding `strings.xml` files.

---

## Contribution

Contributions are welcome to enhance this tool. Feel free to:
- Submit issues for bugs or feature requests.
- Fork the repository and open pull requests.

### Current Limitations
- Supports only flat `strings.xml` files.
- May require additional features for nested structures or advanced use cases.

---

## Notes

- The script modifies files in place, so ensure you **stash or commit all changes** before running it.
- Changes are incremental, making them easy to trace or revert using version control (e.g., Git).
- Meta instructions in comments are **crucial** for accurate and meaningful translations.

---

## License

This project is licensed under the MIT License.
