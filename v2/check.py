def check_and_add_head_content(file_path="index.html"):
    required_content = [
        "<head>",
        "  <link rel=\"stylesheet\" href=\"style.css\">",
        "</head>"
    ]

    with open(file_path, 'r') as file:
        content = file.readlines()

    if content[:3] != required_content:
        content = required_content + content

    with open(file_path, 'w') as file:
        file.writelines(content)

check_and_add_head_content()