from write_to_file import write_to_file
import atexit

def create_element(tag, Text='', Class='', ID='', Lang='EN', Style='', Title=''):
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

    element = f"<{tag} {" ".join(attributes)}>\n"
    if Text:
        element += f"    {Text}\n"
    element += f"</{tag}>"
    atexit.register(write_to_file, element)
    return element

