from v2.build.write_to_file import *
import atexit


def create_element(tag, Text='', Class='', ID='', Lang='EN', Style='', Title='', Is_Internal=False):
    attributes = []
    if Class:
        attributes.append(f"class='{Class}'")
        print(f"Class Values Appended To Attributes for {tag}: {Class}")
    if ID:
        attributes.append(f"id='{ID}'")
        print(f"ID Values Appended To Attributes for {tag}: {ID}")
    if Lang:
        attributes.append(f"lang='{Lang}'")
        print(f"Lang Values Appended To Attributes for {tag}: {Lang}")
    if Style:
        attributes.append(f"style='{Style}'")
        print(f"Style Values Appended To Attributes for {tag}: {Style}")
    if Title:
        attributes.append(f"title='{Title}'")
        print(f"Title Values Appended To Attributes for {tag}: {Title}")

    element = f"<{tag} {' '.join(attributes)}>\n{Text}\n</{tag}>"
    if not isinstance(element, str):
        print(f"Element String Instance: True; {element}")
        atexit.register(write_to_file, element)
    return element