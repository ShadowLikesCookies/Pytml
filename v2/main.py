# Import necessary elements from the html_elements and v2.html_elements modules
from html_elements import *
from v2.html_elements import *
from atexit import register
from Formatter import prettify

# Create a complex HTML structure using div_element, h1_element, and p_element

div_element(
    Text='This is a div element',
    Class='my-class',
    ID='my-id',
    Lang='EN',
    Style='color: red;',
    Title='My div element',
    Child_Element=False,
)
prettify()
