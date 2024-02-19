def h1(text, cls=''):
    if cls:
        return f"<h1 class='{cls}'>{text}</h1>"
    else:
        return f"<h1>{text}</h1>"

def button(text, cls=''):
    if cls:
        return f"<button class='{cls}'>{text}</button>"
    else:
        return f"<button>{text}</button>"
def div(text, cls=''):
    if cls:
        return f"<div class='{cls}'>{text}</div>"
    else:
        return f"<div>{text}</div>"

# HTML "compiler"
element_functions = {
    "h1": h1,
    "button": button,
    "div": div,
}

def compile_to_html(func, *args, **kwargs):
    html_output = func(*args, **kwargs)
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
    main(("h1", "Hello, World!",),
         ("h1", "Hello, World!", "my-class"),
         ("button", "Click me!",),
         ("button", "Click me with class", "my-button-class"),
         ("div", "This is a div")
         )