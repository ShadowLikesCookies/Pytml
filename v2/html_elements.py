import atexit

from v2.html_elements.create_element import create_element
from write_to_file import write_to_file
from ClassNameGenerator import generate_class_name
class html:
    def h1_element(self=None, Class=None, ID='', Lang='EN', Style='', Title='', Is_Internal=False):
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
            element = create_element('h1', self, Class, ID, Lang, Style, Title)
            atexit.register(write_to_file, element)
        elif Is_Internal == True:
            element = create_element('h1', self, Class, ID, Lang, Style, Title)
        return element

    def p_element(self=None, Class=None, ID='', Lang='EN', Style='', Title='', Is_Internal=False):

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
            element = create_element('p', self, Class, ID, Lang, Style, Title)
            atexit.register(write_to_file, element)
        elif Is_Internal == True:
            element = create_element('p', self, Class, ID, Lang, Style, Title)
        return element

    def div_element(self=None, Class=None, ID='', Lang='EN', Style='', Title='', Is_Internal=False):
        if Is_Internal == False:
            if callable(self):
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
            element = create_element('div', self, Class, ID, Lang, Style, Title)
            atexit.register(write_to_file, element)
        elif Is_Internal == True:
            element = create_element('div', self, Class, ID, Lang, Style, Title)

        return element