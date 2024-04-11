import atexit
import os

from v2.build.create_element import *
from v2.build.read_increment_write import read_increment_write
from v2.build.write_to_file import *





def p_element(Text=None, Class=None, ID=None, Lang='EN', Style='', Title='', Is_Internal=False):
    if not Is_Internal:
        if callable(Text):
            raise ValueError("Error: Text input cannot be a function.")
    attributes = []
    if Class is not None:
        attributes.append(f"class='{Class}'")
    elif Class is None:
        P_Class_Num = read_increment_write("P_Data.json", "Fetch_data")
        Class = f"p-Class-{P_Class_Num}"
        attributes.append(f"class='{Class}'")
    if ID is not None:
        attributes.append(f"id='{ID}'")
    elif ID is None:
        p_ID_Num = read_increment_write("p_Data.json", "Fetch_data")
        ID = f"p-ID-{p_ID_Num}"
        attributes.append(f"class='{ID}'")
    if Lang:
        attributes.append(f"lang='{Lang}'")
    if Style:
        attributes.append(f"style='{Style}'")
    if Title:
        attributes.append(f"title='{Title}'")

    if Is_Internal != True:
        element = create_element('p', Text, Class, ID, Lang, Style, Title)
        write_to_file(element)
    elif Is_Internal == True:
        element = create_element('p', Text, Class, ID, Lang, Style, Title)
    return element
