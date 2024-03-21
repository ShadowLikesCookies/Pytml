def write_to_file(content, filename='index.html'):
    with open(filename, 'a') as file:
        file.write(content + '\n')
