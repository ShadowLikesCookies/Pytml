from v2.build.create_element import create_element
from v2.build.write_to_file import write_to_file


def li_element(Text=None, Class=None, ID=None, Lang='EN', Style='', Title='', Is_Internal=False):
    if Is_Internal == False:
        if callable(Text):
            raise ValueError("Error: Text input cannot be a function.")

    attributes = []

    if Class:
        attributes.append(f"class='{Class}'")
    if ID:
        attributes.append(f"id='{ID}'")
    if Lang:
        attributes.append(f"lang='{Lang}'")
    if Style:
        attributes.append(f"style='{Style}'")
    if Title:
        attributes.append(f"title='{Title}'")

    if Is_Internal != True:
        element = create_element('li', Text, Class, ID, Lang, Style, Title, Is_Internal)
        write_to_file(element)
    elif Is_Internal == True:
        element = create_element('li', Text, Class, ID, Lang, Style, Title, Is_Internal)

    return element