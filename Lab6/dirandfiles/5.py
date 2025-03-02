def write_list_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines("\n".join(data))

data = ["Python", "Java", "C++", "JavaScript"]
write_list_to_file("languages.txt", data)