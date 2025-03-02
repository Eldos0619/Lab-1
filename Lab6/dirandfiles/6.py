import string

def generate_text_files():
    for letter in string.ascii_uppercase:  
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt")

generate_text_files()