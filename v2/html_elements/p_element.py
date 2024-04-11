import atexit
import os

from v2.ClassNameGenerator import generate_class_name
from create_element import create_element
from v2.write_to_file import write_to_file




def p_element(Text=None, Class=None, ID='', Lang='EN', Style='', Title='', Is_Internal=False):
    if not Is_Internal:
        if callable(Text):
            raise ValueError("Error: Text input cannot be a function.")
    attributes = []
    if Class is not None:
        attributes.append(f"class='{Class}'")
    elif Class is None:
        Class = generate_class_name(12)
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
        element = create_element('p', Text, Class, ID, Lang, Style, Title)
        atexit.register(write_to_file, element)
    elif Is_Internal == True:
        element = create_element('p', Text, Class, ID, Lang, Style, Title)
    return element
