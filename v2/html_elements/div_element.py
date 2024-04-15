from v2.build.write_to_file import *

# This list is sourced from https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes
ALLOWED_DIV_ATTRIBUTES = {
    "accesskey",
    "class",
    "contenteditable",
    "contextmenu",
    "dir",
    "draggable",
    "dropzone",
    "hidden",
    "id",
    "lang",
    "spellcheck",
    "style",
    "tabindex",
    "title",
    "translate",
    "accesskey",  # Duplicate for clarity

    # Data attributes
    "data-",
}

def div_element(Text='', Class='', ID='', Lang='EN', Style='', Title='', Child_Element=False, accesskey='',
                access_key='', contenteditable='', contextmenu='', dir='', draggable='', dropzone='',
                hidden='', spellcheck='', tabindex='', translate=''):
    """
    This function generates a div element in HTML using f-strings.

    Args:
        Text (str, optional): The text content of the div element. Defaults to ''.
        Class (str, optional): CSS class(es) for the div element. Defaults to ''.
        ID (str, optional): The ID of the div element. Defaults to ''.
        Lang (str, optional): The language of the div element content. Defaults to 'EN'.
        Style (str, optional): Inline CSS styles for the div element. Defaults to ''.
        Title (str, optional): The tooltip text displayed on hover. Defaults to ''.
        Child_Element (Bool, optional): Determines if element is nested within another. Defaults to False.
        accesskey (str, optional): The access key for the div element. Defaults to ''.
        access_key (str, optional): Deprecated alias for accesskey. Defaults to ''.
        contenteditable (str, optional): Whether the element is editable. Defaults to ''.
        contextmenu (str, optional): The context menu for the element. Defaults to ''.
        dir (str, optional): The text direction for the element. Defaults to ''.
        draggable (str, optional): Whether the element is draggable. Defaults to ''.
        dropzone (str, optional): The drop zone for the element. Defaults to ''.
        hidden (str, optional): Whether the element is hidden. Defaults to ''.
        spellcheck (str, optional): Whether the element's spelling is checked. Defaults to ''.
        tabindex (str, optional): The tab index for the element. Defaults to ''.
        translate (str, optional): Whether the element's content is translated. Defaults to ''.

    Returns:
        str: The complete HTML string for the div element.
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
    if accesskey or access_key:
        attributes += f" accesskey='{accesskey or access_key}'"
    if contenteditable:
        attributes += f" contenteditable='{contenteditable}'"
    if contextmenu:
        attributes += f" contextmenu='{contextmenu}'"
    if dir:
        attributes += f" dir='{dir}'"
    if draggable:
        attributes += f" draggable='{draggable}'"
    if dropzone:
        attributes += f" dropzone='{dropzone}'"
    if hidden:
        attributes += f" hidden='{hidden}'"
    if spellcheck:
        attributes += f" spellcheck='{spellcheck}'"
    if tabindex:
        attributes += f" tabindex='{tabindex}'"
    if translate:
        attributes += f" translate='{translate}'"

    if Child_Element != True:
        element = f"<div{attributes}>{Text}</div>"
        write_to_file(element)
    elif Child_Element == True:
        element = f"<div{attributes}>{Text}</div>"

    return element