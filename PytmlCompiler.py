def h1(text, class_name='', indent_level=0):
    indentation = " " * 4 * indent_level
    if class_name:
        return f"{indentation}<h1 class='{class_name}'>{text}</h1>"
    else:
        return f"{indentation}<h1>{text}</h1>"


def a(href='', text='', class_name='', indent_level=0):
    indentation = " " * 4 * indent_level
    if class_name:
        return f"{indentation}<a href='{href}' class='{class_name}'>{text}</a>"
    else:
        return f"{indentation}<a href='{href}'>{text}</a>"


def button(text, class_name='', indent_level=0):
    indentation = " " * 4 * indent_level
    if class_name:
        return f"{indentation}<button class='{class_name}'>{text}</button>"
    else:
        return f"{indentation}<button>{text}</button>"


def img(src, alt='', cls='', indent_level=0, children=None):
    indentation = " " * 4 * indent_level
    class_attribute = f" class='{cls}'" if cls else ''
    alt_attribute = f" alt='{alt}'" if alt else ''

    if children:
        raise ValueError("img tag cannot have nested elements.")

    return f"{indentation}<img src='{src}'{class_attribute}{alt_attribute}>"


def div(class_name='', children=None, indent_level=0):
    if children is None:
        children = []

    indentation = " " * 4 * indent_level

    opening_tag = f"{indentation}<div class='{class_name}'>\n" if class_name else f"{indentation}<div>\n"
    closing_tag = f"{indentation}</div>"

    html_children = []
    for child in children:
        if isinstance(child, tuple):
            element_type, *element_args = child
            if element_type in element_functions:
                html_child = compile_to_html(element_functions[element_type], *element_args,
                                             indent_level=indent_level + 1)
                html_children.append(html_child)
            else:
                raise ValueError(f"Invalid element type: {element_type}")
        else:
            html_children.append(f"{indentation}    {child}")

    indented_children = '\n'.join(html_children)

    return f"{opening_tag}{indented_children}\n{closing_tag}"


def p(text, class_name='', indent_level=0):
    indentation = " " * 4 * indent_level
    if class_name:
        return f"{indentation}<p class='{class_name}'>{text}</p>"
    else:
        return f"{indentation}<p>{text}</p>"


def ul(class_name='', children=None, indent_level=0):
    if children is None:
        children = []

    indentation = " " * 4 * indent_level

    opening_tag = f"{indentation}<ul class='{class_name}'>\n" if class_name else f"{indentation}<ul>\n"
    closing_tag = f"{indentation}</ul>"

    html_children = []
    for child in children:
        if isinstance(child, tuple):
            element_type, *element_args = child
            if element_type in element_functions:
                if element_type == 'img':  # Check if the element type is img
                    html_child = compile_to_html(element_functions[element_type], *element_args,
                                                 indent_level=indent_level, children=None)  # Pass None for children
                else:
                    html_child = compile_to_html(element_functions[element_type], *element_args,
                                                 indent_level=indent_level + 1)  # Adjust indent level for other elements
                html_children.append(html_child)
            else:
                raise ValueError(f"Invalid element type: {element_type}")
        else:
            html_children.append(f"{indentation}    <li>{child}</li>")

    indented_children = '\n'.join(html_children)

    return f"{opening_tag}{indented_children}\n{closing_tag}"



def li(text, class_name='', indent_level=0):
    indentation = " " * 4 * indent_level
    if class_name:
        return f"{indentation}<li class='{class_name}'>{text}</li>"
    else:
        return f"{indentation}<li>{text}</li>"


def span(text='', class_name='', indent_level=0):
    indentation = " " * 4 * indent_level
    if class_name:
        return f"{indentation}<span class='{class_name}'>{text}</span>"
    else:
        return f"{indentation}<span>{text}</span>"


def form(action='', method='post', class_name='', children=None, indent_level=0):
    if children is None:
        children = []

    indentation = " " * 4 * indent_level

    opening_tag = f"{indentation}<form action='{action}' method='{method}' class='{class_name}'>\n" if class_name else f"{indentation}<form action='{action}' method='{method}'>\n"
    closing_tag = f"{indentation}</form>"

    html_children = []
    for child in children:
        if isinstance(child, tuple):
            element_type, *element_args = child
            if element_type in element_functions:
                html_child = compile_to_html(element_functions[element_type], *element_args,
                                             indent_level=indent_level + 1)
                html_children.append(html_child)
            else:
                raise ValueError(f"Invalid element type: {element_type}")
        else:
            html_children.append(f"{indentation}    {child}")

    indented_children = '\n'.join(html_children)

    return f"{opening_tag}{indented_children}\n{closing_tag}"


def input(type_='text', id_='', class_name='', attributes=None, indent_level=0):
    indentation = " " * 4 * indent_level
    attributes_str = ''

    # Constructing attributes string
    if id_:
        attributes_str += f" id='{id_}'"
    if class_name:
        attributes_str += f" class='{class_name}'"
    if attributes:
        for key, value in attributes.items():
            attributes_str += f" {key}='{value}'"

    # Constructing input tag with attributes
    return f"{indentation}<input type='{type_}'{attributes_str}>"


def label(text='', for_id='', class_name='', indent_level=0):
    indentation = " " * 4 * indent_level
    attributes = ''
    if for_id:
        attributes += f" for='{for_id}'"
    if class_name:
        attributes += f" class='{class_name}'"

    return f"{indentation}<label{attributes}>{text}</label>"


element_functions = {
    "h1": h1,
    "button": button,
    "div": div,
    "p": p,
    "ul": ul,
    "li": li,
    "img": img,
    "a": a,
    "span": span,
    "form": form,
    "label": label,
    "input": input,
}



def compile_to_html(func, *args, **kwargs):
    indent_level = kwargs.pop('indent_level', 0)

    if args:
        children = []
        for arg in args:
            if isinstance(arg, tuple):
                element_type = arg[0]
                if element_type in element_functions:
                    element_function = element_functions[element_type]
                    html_output = compile_to_html(element_function, *arg[1:], indent_level=indent_level + 1)
                    children.append(html_output)
                else:
                        raise ValueError(f"Invalid element type: {element_type}")
            else:
                children.append(arg)

        html_output = func(*children, indent_level=indent_level, **kwargs)
    else:
        html_output = func(indent_level=indent_level, **kwargs)

    return html_output


def write_to_file(html_output, filename):
    with open(filename, "w") as file:
        file.write(html_output)


def compile_and_append_to_list(args, filename):
    html_outputs = []
    for arg in args:
        element_type = arg[0]
        if element_type in element_functions:
            element_function = element_functions[element_type]
            html_output = compile_to_html(element_function, *arg[1:])
            html_outputs.append(html_output)
        else:
            raise ValueError(f"Invalid element type: {element_type}")
    with open(filename, "w") as file:
        for html_output in html_outputs:
            file.write(html_output + "\n")


def main(*args):
    compile_and_append_to_list(args, "output.html")


if __name__ == "__main__":
    main(
        ("div", "", [
            ("button", "", "Click me!"),
            ("h1", "", "Hello, World!"),
            ("div", "inner-div", [
                ("button", "nested-button", "Nested button"),
                ("p", "", "This is nested content."),
                ("ul", "", [
                    ("li", "e", "Item 1"),
                    ("li", "e", "Item 2"),
                    ("li", "e", "Item 3")
                ]),
                ("ul", "", [
                    ("ul", "", [
                        ("li", "e", "Item 1"),
                        ("li", "e", "Item 2"),
                        ("li", "e", "Item 3")
                    ])
                ]),
                ("div", "class_name", [
                    ("div", "class_name", [
                        ("div", "class_name", [
                            ("p", "", "This is nested content."),
                        ])
                    ])
                ])
            ])
        ])
    )

