import atexit
import os

from v2.build.create_element import *
from v2.build.read_increment_write import read_increment_write
from v2.build.write_to_file import *

def p_element(Text=None, Class=None, ID=None, Lang='EN', Style='', Title='', Is_Internal=False):
    # If Is_Internal is False, raise an error if Text is a function
    if not Is_Internal:
        if callable(Text):
            raise ValueError("Error: Text input cannot be a function.")

    attributes = []

    # If Class is provided, add it to the attributes list
    if Class is not None:
        attributes.append(f"class='{Class}'")
    # If Class is not provided, read and increment the class value from the P_Data.json file
    elif Class is None:
        P_Class_Num = read_increment_write("P_Data.json", "Fetch_data")
        Class = f"p-Class-{P_Class_Num}"
        attributes.append(f"class='{Class}'")

    # If ID is provided, add it to the attributes list
    if ID is not None:
        attributes.append(f"id='{ID}'")
    # If ID is not provided, read and increment the ID value from the p_Data.json file
    elif ID is None:
        p_ID_Num = read_increment_write("p_Data.json", "Fetch_data")
        ID = f"p-ID-{p_ID_Num}"
        attributes.append(f"class='{ID}'")

    # Add Lang, Style, and Title to the attributes list if they are provided
    if Lang:
        attributes.append(f"lang='{Lang}'")
    if Style:
        attributes.append(f"style='{Style}'")
    if Title:
        attributes.append(f"title='{Title}'")

    # If Is_Internal is not True, create the p element, write it to the file, and return it
    if Is_Internal != True:
        element = create_element('p', Text, Class, ID, Lang, Style, Title)
        write_to_file(element)
    # If Is_Internal is True, create the p element and return it without writing to the file
    elif Is_Internal == True:
        element = create_element('p', Text, Class, ID, Lang, Style, Title)

    return element