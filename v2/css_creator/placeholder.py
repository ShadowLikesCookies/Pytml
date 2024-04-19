import os
import json

def custom_write_to_file(content, filename):
    with open(filename, 'a') as file:  # Use 'a' for append mode instead of 'w' for write mode
        file.write(content + '\n')

def generateCSS(ElementSelectorType, Decorators="", file_path='css_properties.json', **kwargs):
    file_path = os.path.join(os.path.dirname(__file__), file_path)  # Get the absolute path to css_properties.json
    directory = 'v2'
    file_name = 'style.css'
    file_path2 = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), file_name)
    print(f"File path2: {file_path2}")

    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create the style.css file

    print(f"File path: {file_path}")
    try:
        with open(file_path, 'r') as f:
            css_properties = json.load(f)
            print(f"Loaded {len(css_properties)} CSS properties from {file_path}")
    except Exception as e:
        print(f"\033[91mError loading CSS properties from {file_path}: {e}\033[0m")
        return

    css_dictionary = set(css_properties.keys())

    cssStruct = []
    CssStartStructure = f"{ElementSelectorType}" + " {"
    if Decorators:
        CssStartStructure += f":{Decorators}"
    CssEndStructure = "}"

    print(f"CssStartStructure: {CssStartStructure}")
    print(f"CssEndStructure: {CssEndStructure}")

    for key, value in kwargs.items():
        try:
            if key in css_dictionary:
                CssMidStructure = f"    {key}: {value};"
                cssStruct.append(CssMidStructure)
            else:
                raise KeyError(f"Css Invalid_Property Error: '{key}' is not a valid CSS property.")
        except KeyError as e:
            print(f"\033[91m{e}\033[0m")

    cssStruct.insert(0, CssStartStructure)
    cssStruct.append(CssEndStructure)

    # Print the contents of cssStruct
    print(f"CSS Struct:     {cssStruct}")

    # Write cssStruct to the style.css file
    for css in cssStruct:
        custom_write_to_file(css, filename=file_path2)
        print(css)

generateCSS(ElementSelectorType="*", color="blue")
