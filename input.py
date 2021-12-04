def input_file(file):
    file_list = []
    with open(file, 'r') as fn:
        for line in fn:
            file_list.append(line.strip('\n'))
    return file_list