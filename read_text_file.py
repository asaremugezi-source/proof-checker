def read_text_file(file_name):
    x = open(file_name, "r")
    s = x.read()
    x.close()
    return s
