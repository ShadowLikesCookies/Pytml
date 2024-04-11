
def override_to_file(content, filename='index.html'):
    # Open the file in append mode
    with open(filename, 'w') as file:
        # Write the content to the file followed by a newline character
        file.write(content + '\n')

