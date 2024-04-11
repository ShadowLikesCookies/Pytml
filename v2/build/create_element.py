# Import necessary functions from the write_to_file module
from v2.build.write_to_file import *
import atexit

# Function to create an HTML element with specified attributes
def create_element(tag, Text='', Class='', ID='', Lang='EN', Style='', Title='', Is_Internal=False):
    attributes = []

    # Check if Class is provided and append it to the attributes list
    if Class:
        attributes.append(f"class='{Class}'")
        print(f"Class Values Appended To Attributes for {tag}: {Class}")

    # Check if ID is provided and append it to the attributes list
    if ID:
        attributes.append(f"id='{ID}'")
        print(f"ID Values Appended To Attributes for {tag}: {ID}")

    # Check if Lang is provided and append it to the attributes list
    if Lang:
        attributes.append(f"lang='{Lang}'")
        print(f"Lang Values Appended To Attributes for {tag}: {Lang}")

    # Check if Style is provided and append it to the attributes list
    if Style:
        attributes.append(f"style='{Style}'")
        print(f"Style Values Appended To Attributes for {tag}: {Style}")

    # Check if Title is provided and append it to the attributes list
    if Title:
        attributes.append(f"title='{Title}'")
        print(f"Title Values Appended To Attributes for {tag}: {Title}")

    # Construct the HTML element string with the specified attributes and text
    if Is_Internal is False:
        element = f"<{tag} {' '.join(attributes)}>\n{Text}\n</{tag}>"
    elif Is_Internal is True:
        element = f"<{tag} {' '.join(attributes)}>\n{Text}\n</{tag}>"


    # Register write_to_file function if element is not a string instance
    if not isinstance(element, str):
        print(f"Element String Instance: True; {element}")
        atexit.register(write_to_file, element)

    return element