
import bs4
import sys
from Pytml.v2.build.override_to_file import *

def format_html(input_file):
    try:
        with open(input_file, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print("File not found:", input_file)
        return None

    formatter = bs4.formatter.HTMLFormatter(indent=4)
    # Parse HTML using BeautifulSoup
    soup = bs4.BeautifulSoup(data, 'html.parser')

    # Prettify the HTML
    prettyHTML = soup.prettify(formatter=formatter)
    print(prettyHTML)
    return prettyHTML



def prettify(filename="index.html"):
    formatted_html = format_html(filename)
    override_to_file(formatted_html)

prettify()

