import atexit
import os
from v2.build.create_element import *
from v2.build.read_increment_write import read_increment_write
from v2.build.write_to_file import *








def h1_element(Text=None, Class=None, ID=None, Lang='EN', Style='', Title='', Is_Internal=False):
    if Is_Internal == False:
        if callable(Text):
            raise ValueError("Error: Text input cannot be a function.")
    attributes = []
    if Class is not None:
        attributes.append(f"class='{Class}'")
    elif Class is None:
        h1_Class_Num = read_increment_write("H1_Data.json", "Fetch_data")
        Class = f"h1-Class-{h1_Class_Num}"
        attributes.append(f"class='{Class}'")
    if ID is not None:
        attributes.append(f"id='{ID}'")
    elif ID is None:
        h1_ID_Num = read_increment_write("h1_Data.json", "Fetch_data")
        ID = f"h1-ID-{h1_ID_Num}"
        attributes.append(f"class='{ID}'")
    if Lang:
        attributes.append(f"lang='{Lang}'")
    if Style:
        attributes.append(f"style='{Style}'")
    if Title:
        attributes.append(f"title='{Title}'")
    if Is_Internal != True:
        element = create_element('h1', Text, Class, ID, Lang, Style, Title)
        write_to_file(element)
    elif Is_Internal == True:
        element = create_element('h1', Text, Class, ID, Lang, Style, Title)
    return element