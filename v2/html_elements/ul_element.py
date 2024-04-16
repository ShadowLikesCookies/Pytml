from Pytml.v2.build.write_to_file import *


def ul_element(Child_Element=False, Class='', ID='', Lang='EN', Style='', Title='', Accesskey='',
               Contenteditable='', Contextmenu='', Dir='', Draggable='', Dropzone='', Hidden='', Spellcheck='',
               Tabindex='', Translate=''):
    """
    This function generates a ul element in HTML using f-strings.

    Args:
        Class (str, optional): CSS class(es) for the ul element.
        ID (str, optional): The ID of the ul element.
        Lang (str, optional): The language of the ul element content. Defaults to 'EN'.
        Style (str, optional): Inline CSS styles for the ul element.
        Title (str, optional): The tooltip text displayed on hover.
        Accesskey (str, optional): The access key for the ul element.
        Contenteditable (str, optional): Whether the ul element is editable.
        Contextmenu (str, optional): The context menu for the ul element.
        Dir (str, optional): The text direction for the ul element.
        Draggable (str, optional): Whether the ul element is draggable.
        Dropzone (str, optional): The drop zone for the ul element.
        Hidden (str, optional): Whether the ul element is hidden.
        Spellcheck (str, optional): Whether the ul element is spellchecked.
        Tabindex (str, optional): The tab index for the ul element.
        Translate (str, optional): Whether the ul element is translated.

    Returns:
        str: The complete HTML string for the ul element.
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
    if Accesskey:
        attributes += f" accesskey='{Accesskey}'"
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
        element = f"<ul{attributes}></ul>"
        write_to_file(element)
    if Child_Element == False:
        element = f"<ul{attributes}></ul>"

    return element
