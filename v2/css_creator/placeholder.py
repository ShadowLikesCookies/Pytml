import json

def generateCSS(ElementSelectorType, Decorators="", **kwargs):
    with open('css_properties.json') as f:
        css_properties = json.load(f)

    css_dictionary = set(css_properties.keys())

    cssStruct = []
    CssStartStructure = f"{ElementSelectorType}"
    if Decorators:
        CssStartStructure += f":{Decorators}"
    CssEndStructure = "}"

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

    return cssStruct


# Example usage:
css = generateCSS(ElementSelectorType="*", Decorators="hover", color="blue", background="orange", invalid_property="value")
print("\n".join(css))