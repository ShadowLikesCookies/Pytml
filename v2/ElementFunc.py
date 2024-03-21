class Element:
    def __init__(self, tag, content='', **attributes):
        self.tag = tag
        self.content = content
        self.attributes = attributes
        self.children = []

    def add_child(self, child_tag, child_content='', **child_attributes):
        child = Element(child_tag, child_content, **child_attributes)
        self.children.append(child)
        return child

    def __str__(self, indent=0):
        element_str = " " * 4 * indent + f"<{self.tag}"
        for key, value in self.attributes.items():
            element_str += f" {key}='{value}'"
        element_str += ">\n"

        if self.content:
            element_str += " " * 4 * (indent + 1) + self.content + "\n"

        for child in self.children:
            element_str += child.__str__(indent + 1)

        element_str += " " * 4 * indent + f"</{self.tag}>\n"
        return element_str

# Example of chaining nested elements
parent = Element('div', Class='container', ID="apple sauce")
(parent.add_child('h1', 'Heading 1', Class='heading')
 .add_child('p', 'Paragraph 1', Class='paragraph')
 .add_child('h2','text', Class="class"))

# Print the nested elements with proper indentation and line separation
print(parent.__str__())