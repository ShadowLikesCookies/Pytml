from write_to_file import write_to_file
import atexit
def create_element(tag, Text='', Class='', ID='', Lang='EN', Style='', Title=''):
    element = f"<{tag} class='{Class}' id='{ID}' lang='{Lang}' style='{Style}' title='{Title}'>{Text}</{tag}>"
    atexit.register(write_to_file, element)
    return element
