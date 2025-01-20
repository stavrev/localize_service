import pycountry

def recognizeLanguage(code):
    """
    Recognizes the language and optionally the region based on the provided code.

    :param code: The language code (e.g., "en", "bg", "de-rDE").
    :return: A string describing the language and region, if applicable.
    """
    try:
        # Split the code into language and region parts if applicable
        parts = code.split("-")
        language_code = parts[0]
        region_code = parts[1] if len(parts) > 1 else None

        # Get the language name
        language = pycountry.languages.get(alpha_2=language_code) or pycountry.languages.get(alpha_3=language_code)
        language_name = language.name if language else "Unknown Language"

        # Get the region name, if applicable
        region_name = None
        if region_code:
            region = pycountry.countries.get(alpha_2=region_code.upper())
            region_name = region.name if region else "Unknown Region"

        # Construct the result string
        if region_name:
            return f"{language_name} ({language_code}) in {region_name}"
        else:
            return f"{language_name} ({language_code})"
    except Exception as e:
        return f"Error recognizing language: {str(e)}"