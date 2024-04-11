
def write_to_file(content, filename='index.html'):
    # Open the file in append mode
    with open(filename, 'a') as file:
        # Write the content to the file followed by a newline character
        file.write(content + '\n')

