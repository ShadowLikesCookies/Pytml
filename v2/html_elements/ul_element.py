from v2.build.create_element import *
from v2.build.write_to_file import *
def ul_element(Class=None, ID=None, Lang='EN', Style='', Title='', Is_Internal=False):
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
        element = create_element('ul', None, Class, ID, Lang, Style, Title, Is_Internal)
        write_to_file(element)
    elif Is_Internal == True:
        element = create_element('ul', None, Class, ID, Lang, Style, Title, Is_Internal)

    return element