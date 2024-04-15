from v2.build.write_to_file import *
def img_element(Child_Element=False, Src='', Alt='', Width='', Height='', Usemap='', Ismap='', Crossorigin='', Sizes='', Srcset='',
                Loading='', Referrerpolicy='', Naturalheight='', Naturalwidth='', Hspace='', Vspace=''):
    """
    This function generates an img element in HTML using f-strings.

    Args:
        Src (str, optional): The URL of the image.
        Alt (str, optional): The alternative text for the image.
        Width (str, optional): The width of the image.
        Height (str, optional): The height of the image.
        Usemap (str, optional): The partial URL of an image map associated with the element.
        Ismap (str, optional): Specifies an image as a server-side image map.
        Crossorigin (str, optional): CORS settings of an image.
        Sizes (str, optional): Image sizes for different page layouts.
        Srcset (str, optional): A list of image files to use in different situations.
        Loading (str, optional): Specifies whether a browser should defer loading of images.
        Referrerpolicy (str, optional): Specifies which referrer information to use when fetching an image.
        Naturalheight (str, optional): Returns the original height of an image.
        Naturalwidth (str, optional): Returns the original width of an image.
        Hspace (str, optional): The number of pixels of white space on the left and right of the image.
        Vspace (str, optional): The number of pixels of white space above and below the image.

    Returns:
        str: The complete HTML string for the img element.
    """
    attributes = ""

    # Add common attributes based on provided arguments
    if Src:
        attributes += f" src='{Src}'"
    if Alt:
        attributes += f" alt='{Alt}'"
    if Width:
        attributes += f" width='{Width}'"
    if Height:
        attributes += f" height='{Height}'"
    if Usemap:
        attributes += f" usemap='{Usemap}'"
    if Ismap:
        attributes += f" ismap='{Ismap}'"
    if Crossorigin:
        attributes += f" crossorigin='{Crossorigin}'"
    if Sizes:
        attributes += f" sizes='{Sizes}'"
    if Srcset:
        attributes += f" srcset='{Srcset}'"
    if Loading:
        attributes += f" loading='{Loading}'"
    if Referrerpolicy:
        attributes += f" referrerpolicy='{Referrerpolicy}'"
    if Naturalheight:
        attributes += f" naturalheight='{Naturalheight}'"
    if Naturalwidth:
        attributes += f" naturalwidth='{Naturalwidth}'"
    if Hspace:
        attributes += f" hspace='{Hspace}'"
    if Vspace:
        attributes += f" vspace='{Vspace}'"
    if Child_Element != False:
        element = f"<img{attributes}>"
        write_to_file(element)
    if Child_Element == False:
        element = f"<img{attributes}>"

    return element