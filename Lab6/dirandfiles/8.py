import os

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
    else:
        print("File does not exist.")

# Пример использования
delete_file("test.txt")