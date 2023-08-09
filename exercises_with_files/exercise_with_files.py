"""
file = open("test.txt", "w")
file.write("sample")
file.close()
"""

"""       EXERCISE 1 - splitting full names to seperate files     """
names_and_surnames = []

with open("namesList.txt", "r", encoding="UTF-8") as file:
    for line in file:
        names_and_surnames.append(tuple(line.replace("\n", "").split(" ")))


with open("names.txt", "w", encoding="UTF-8") as file:
    for name in names_and_surnames:
        file.write(name[0] + "\n")

with open("lastnames.txt", "w", encoding="UTF-8") as file:
    for lastname in names_and_surnames:
        try:
            file.write(lastname[1] + "\n")
        except IndexError:
            file.write("\n")

"""       EXERCISE 2 - reading content if file exists      """
def read_content_from_file(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"{path} is not found in this folder!")

nameOfFile = input("What file do you want to read?\n")

fileContent = read_content_from_file(nameOfFile)


"""       EXERCISE 3 - word count in file      """
path = input("What file do we check: ")
word = input("What word do we count? ")

try:
    with open(path, "r", encoding="UTF-8") as file:
        fileContent = file.read()
        wordCount = fileContent.count(word)
        print(f"File {path} contains {wordCount} apperances of word {word}.")
except FileNotFoundError:
    print(f"There is no file {path}")
except PermissionError:
    print(f"You have no permission to open {path}")

