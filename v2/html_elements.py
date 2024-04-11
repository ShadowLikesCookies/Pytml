import atexit

from create_element import create_element
from write_to_file import write_to_file
from ClassNameGenerator import generate_class_name
class html:
    def h1_element(Text=None, Class='', ID='', Lang='EN', Style='', Title='', Is_Internal=False):



        attributes = []
        if Class == '':
            rand_class = generate_class_name(length=12)
            print(rand_class)
            attributes.append(f"class='{rand_class}'")
        elif Class:
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
            element = create_element('h1', Text, Class, ID, Lang, Style, Title)
            atexit.register(write_to_file, element)
        elif Is_Internal == True:
            element = create_element('h1', Text, Class, ID, Lang, Style, Title)
        return element

    def p_element(Text=None, Class='', ID='', Lang='EN', Style='', Title='', Is_Internal=False):

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
            element = create_element('p', Text, Class, ID, Lang, Style, Title)
            atexit.register(write_to_file, element)
        elif Is_Internal == True:
            element = create_element('p', Text, Class, ID, Lang, Style, Title)
        return element

    def div_element(Text=None, Class='', ID='', Lang='EN', Style='', Title='', Is_Internal=False):
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
            element = create_element('div', Text, Class, ID, Lang, Style, Title)
            atexit.register(write_to_file, element)
        elif Is_Internal == True:
            element = create_element('div', Text, Class, ID, Lang, Style, Title)
            element1 = create_element('div', element, Class, ID, Lang, Style, Title)

        return element