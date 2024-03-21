from create_element import create_element
from write_to_file import write_to_file

def h1_element(Text='', Class='', ID='', Lang='EN', Style='', Title=''):
    return create_element('h1', Text, Class, ID, Lang, Style, Title)

def p_element(Text='', Class='', ID='', Lang='EN', Style='', Title=''):
    return create_element('p', Text, Class, ID, Lang, Style, Title)

def div_element(Text='', Class='', ID='', Lang='EN', Style='', Title=''):
    return create_element('div', Text, Class, ID, Lang, Style, Title)
