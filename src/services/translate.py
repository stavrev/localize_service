import openai
import os


MODEL = "gpt-4-turbo"

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

openai.api_key = openai_api_key


def translateAgent(language):
    return (
        f"You are an expert Translator in {language} language and Localization Specialist.\n"
        f"Your goal is to translate input data into {language} language while preserving meaning, intent, and cultural alignment.\n"
        "The output must maintain usability, naturalness, and fit within any specified constraints.\n"
        "Ensure the translation aligns with provided guidelines and adapts seamlessly to the target audience's expectations.\n\n"
        "You are a highly skilled translator with expertise in linguistic accuracy, cultural adaptation,"
        " and localization for digital applications. You excel at creating translations that feel natural and"
        " intuitive while respecting the provided context and constraints. Your translations ensure usability and"
        f" cultural resonance, delivering seamless integration into {language} language."
        "\n"
        "Rules: Output only JSON data dictionary of the translated text, using the keys provided by input data.\n"
        "Do not output any additional text. Only output the translated item into json dictionary."
    )

def taskPrompt(data, meta):
    return (
        "Extract keys and translate values from the provided JSON `data`."
        "\n"
        f"Data to translate: \"\"\"\n{data}\n\"\"\"\n"
        "Important, do not translate literally, but rethink of its purpose and recreate it to be fluent"
        " and natural to the target language.\n"
        "\n"
        "Additional context and important guidance:\n"
        f"{meta}\n"
        "Generate only the translated output JSON.\n"
        "Do not change the json keys, keep them intact. Only translate values.\n"
    )


def sendMessage(system, message):
    response = openai.chat.completions.create(model=MODEL,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": message}
    ])
    return response.choices[0].message.content


def runOne(data: str, meta: str, language: str):
    system = translateAgent(language)
    message = taskPrompt(data, meta)
    return sendMessage(system, message)