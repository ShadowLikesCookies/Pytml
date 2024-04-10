from write_to_file import write_to_file
import atexit

def create_element(tag, Text='', Class='', ID='', Lang='EN', Style='', Title='', Is_Internal=False):
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

    element = f"<{tag} {" ".join(attributes)}>\n{Text}\n</{tag}>"
    if not isinstance(element, str):
        atexit.register(write_to_file, element)
    return element

