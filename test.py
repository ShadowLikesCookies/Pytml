from PytmlCompiler import main
if __name__ == "__main__":
    html_output = main(
        ("div", "", [
            ("button", "", "Click me!"),
            ("h1", "", "Hello, World!"),
            ("div", "inner-div", [
                ("button", "nested-button", "Nested button"),
                ("p", "", "This is nested content."),
                ("ul", "", [  # Add a new nested element, an unordered list
                    ("li", "", "Item 1"),
                    ("li", "", "Item 2"),
                    ("li", "", "Item 3"),
                ]),
            ]),
        ]),
    )
