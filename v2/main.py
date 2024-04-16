# Import necessary elements from the html_elements and v2.html_elements modules
from html_elements import *
from atexit import register
from Formatter import prettify
from Pytml.v2.css_creator.placeholder import *
# Create a complex HTML structure using div_element, h1_element, and p_element

div_element(
    Text='This is a div element' + h1_element(Text=f"Cool {h1_element(Child_Element=True)}", Child_Element=True),
    Class='my-class',
    ID='my-id',
    Lang='EN',
    Style=generateCSS(ElementSelectorType="*", color="red"),
    Title='My div element',
    Child_Element=False,
)
prettify()

