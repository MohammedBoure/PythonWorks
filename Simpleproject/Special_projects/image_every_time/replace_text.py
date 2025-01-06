def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print("Error:", e)


