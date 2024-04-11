import atexit
import os

# Import necessary functions for creating elements, writing to file, and reading/incrementing values
from v2.build.create_element import *
from v2.build.write_to_file import *
from v2.build.read_increment_write import *

def div_element(Text=None, Class=None, ID=None, Lang='EN', Style='', Title='', Is_Internal=False):
    # If Is_Internal is False, raise an error if Text is a function
    if Is_Internal == False:
        if callable(Text):
            raise ValueError("Error: Text input cannot be a function.")

    attributes = []

    # If Class is provided, add it to the attributes list
    if Class:
        attributes.append(f"class='{Class}'")
    # If ID is provided, add it to the attributes list
    if ID:
        attributes.append(f"id='{ID}'")
    # Add Lang, Style, and Title to the attributes list if they are provided
    if Lang:
        attributes.append(f"lang='{Lang}'")
    if Style:
        attributes.append(f"style='{Style}'")
    if Title:
        attributes.append(f"title='{Title}'")

    # If Is_Internal is not True, create the div element, write it to the file, and return it
    if Is_Internal != True:
        element = create_element('div', Text, Class, ID, Lang, Style, Title, Is_Internal)
        write_to_file(element)
    # If Is_Internal is True, create the div element and return it without writing to the file
    elif Is_Internal == True:
        element = create_element('div', Text, Class, ID, Lang, Style, Title, Is_Internal)

    return element