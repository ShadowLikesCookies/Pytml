from Pytml.v2.build.write_to_file import *


def p_element(Child_Element=False, Text='', Class='', ID='', Lang='EN', Style='', Title='', Accesskey='',
              Contenteditable='', Contextmenu='', Dir='', Draggable='', Dropzone='', Hidden='', Spellcheck='',
              Tabindex='', Translate=''):
    """
    This function generates a p element in HTML using f-strings.

    Args:
        Text (str, optional): The text content of the p element.
        Class (str, optional): CSS class(es) for the p element.
        ID (str, optional): The ID of the p element.
        Lang (str, optional): The language of the p element content. Defaults to 'EN'.
        Style (str, optional): Inline CSS styles for the p element.
        Title (str, optional): The tooltip text displayed on hover.
        Accesskey (str, optional): The access key for the p element.
        Contenteditable (str, optional): Whether the p element is editable.
        Contextmenu (str, optional): The context menu for the p element.
        Dir (str, optional): The text direction for the p element.
        Draggable (str, optional): Whether the p element is draggable.
        Dropzone (str, optional): The drop zone for the p element.
        Hidden (str, optional): Whether the p element is hidden.
        Spellcheck (str, optional): Whether the p element is spellchecked.
        Tabindex (str, optional): The tab index for the p element.
        Translate (str, optional): Whether the p element is translated.

    Returns:
        str: The complete HTML string for the p element.
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
        element = f"<p{attributes}>{Text}</p>"
        write_to_file(element)
    if Child_Element == False:
        element = f"<p{attributes}>{Text}</p>"

    return element
