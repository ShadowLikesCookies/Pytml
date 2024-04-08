from create_element import create_element
from write_to_file import write_to_file
class html:
    def h1_element(self, Text='', Class='', ID='', Lang='EN', Style='', Title=''):
        return create_element('h1', Text, Class, ID, Lang, Style, Title)

    def p_element(self, Text='', Class='', ID='', Lang='EN', Style='', Title=''):
        return create_element('p', Text, Class, ID, Lang, Style, Title)

    def div_element(self, Text=None, Class='', ID='', Lang='EN', Style='', Title='', element=None):
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

        if Text:
            element = create_element('div', Text, Class, ID, Lang, Style, Title)
        elif element:
            element = f"    {element}\n"
            element = f"<div {" ".join(attributes)}>\n{element}</div>"
        else:
            element = f"<div {" ".join(attributes)}>\n</div>"

        atexit.register(write_to_file, element)
        return element
