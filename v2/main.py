# Import necessary elements from the html_elements and v2.html_elements modules
from html_elements import *
from v2.html_elements import *

# Create a complex HTML structure using div_element, h1_element, and p_element
a = div_element(Text=h1_element(Text=p_element(Is_Internal=True), Is_Internal=True))