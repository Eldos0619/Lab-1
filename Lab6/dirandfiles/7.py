import shutil

def copy_file(source, destination):
    #shutil.copyfile(source, destination)
    shutil.move("copy_test.txt", "test.txt") 
    #print(f"Copied {source} to {destination}")

copy_file("B.txt", "A.txt")