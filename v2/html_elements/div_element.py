import atexit
import os

from create_element import create_element
from write_to_file import write_to_file





print(Div_Value)

def div_element(Text=None, Class=None, ID='', Lang='EN', Style='', Title='', Is_Internal=False):
    if Is_Internal == False:
        if callable(Text):
            raise ValueError("Error: Text input cannot be a function.")
    attributes = []
    if Class is not None:
        attributes.append(f"class='{Class}'")
    elif Class is None:
        attributes.append(f"class='Class-{x}'")
    if ID:
        attributes.append(f"id='{ID}'")
    if Lang:
        attributes.append(f"lang='{Lang}'")
    if Style:
        attributes.append(f"style='{Style}'")
    if Title:
        attributes.append(f"title='{Title}'")

    if Is_Internal != True:
        element = create_element('div', Text, Class, ID, Lang, Style, Title)
        atexit.register(write_to_file, element)
    elif Is_Internal == True:
        element = create_element('div', Text, Class, ID, Lang, Style, Title)

    return element
