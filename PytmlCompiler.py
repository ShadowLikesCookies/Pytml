def h1(text, class_name='', indent_level=0):
    if class_name:
        return f"<h1 class='{class_name}'>{text}</h1>"
    else:
        return f"<h1>{text}</h1>"


def button(text, class_name='', indent_level=0):
    if class_name:
        return f"<button class='{class_name}'>{text}</button>"
    else:
        return f"<button>{text}</button>"


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
    if class_name:
        return f"<p class='{class_name}'>{text}</p>"
    else:
        return f"<p>{text}</p>"



def ul(class_name='', children=None, indent_level=0):
    if children is None:
        children = []


    indentation = " " * 4 * indent_level


    opening_tag = f"{indentation}<ul class='{class_name}'>" if class_name else f"{indentation}<ul>"
    closing_tag = f"{indentation}</ul>"


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
            raise ValueError("Invalid child element for ul: only tuples are allowed")


    indented_children = '\n'.join(html_children)

    return f"{opening_tag}\n{indented_children}\n{closing_tag}"


def li(text, class_name='', indent_level=0):
    if class_name:
        return f"<li class='{class_name}'>{text}</li>"
    else:
        return f"<li>{text}</li>"




element_functions = {
    "h1": h1,
    "button": button,
    "div": div,
    "p": p,
    "ul": ul,
    "li": li,
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
                    ("li", "", "Item 1"),
                    ("li", "", "Item 2"),
                    ("li", "", "Item 3"),
                ]),
            ]),
        ]),
    )
