from Pytml.v2.build.write_to_file import *


def li_element(Child_Element=False, Text='', Class='', ID='', Lang='EN', Style='', Title='', accesskey='',
               Contenteditable='', Contextmenu='', Dir='', Draggable='', Dropzone='', Hidden='', Spellcheck='',
               Tabindex='', Translate=''):
    """
    This function generates a li element in HTML using f-strings.

    Args:
        Text (str, optional): The text content of the li element.
        Class (str, optional): CSS class(es) for the li element.
        ID (str, optional): The ID of the li element.
        Lang (str, optional): The language of the li element content. Defaults to 'EN'.
        Style (str, optional): Inline CSS styles for the li element.
        Title (str, optional): The tooltip text displayed on hover.
        Accesskey (str, optional): The access key for the li element.
        Contenteditable (str, optional): Whether the li element is editable.
        Contextmenu (str, optional): The context menu for the li element.
        Dir (str, optional): The text direction for the li element.
        Draggable (str, optional): Whether the li element is draggable.
        Dropzone (str, optional): The drop zone for the li element.
        Hidden (str, optional): Whether the li element is hidden.
        Spellcheck (str, optional): Whether the li element is spellchecked.
        Tabindex (str, optional): The tab index for the li element.
        Translate (str, optional): Whether the li element is translated.

    Returns:
        str: The complete HTML string for the li element.
    """
    attributes = ""

    # Add common attributes based on provided arguments
    if Class:
        attributes += f" class='{Class}'"
    if ID:
        attributes += f" id='{ID}'"
    if Lang:
        attributes += f" lang='{Lang}'"
    if Style:
        attributes += f" style='{Style}'"
    if Title:
        attributes += f" title='{Title}'"
    if accesskey:
        attributes += f" accesskey='{accesskey}'"
    if Contenteditable:
        attributes += f" contenteditable='{Contenteditable}'"
    if Contextmenu:
        attributes += f" contextmenu='{Contextmenu}'"
    if Dir:
        attributes += f" dir='{Dir}'"
    if Draggable:
        attributes += f" draggable='{Draggable}'"
    if Dropzone:
        attributes += f" dropzone='{Dropzone}'"
    if Hidden:
        attributes += f" hidden='{Hidden}'"
    if Spellcheck:
        attributes += f" spellcheck='{Spellcheck}'"
    if Tabindex:
        attributes += f" tabindex='{Tabindex}'"
    if Translate:
        attributes += f" translate='{Translate}'"

    if Child_Element != False:
        element = f"<li{attributes}>{Text}</li>"
        write_to_file(element)
    if Child_Element == False:
        element = f"<li{attributes}>{Text}</li>"

    return element
