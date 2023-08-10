"""       EXERCISE 1 - splitting full names to seperate files     """

with open("namesList.txt", "r", encoding="UTF-8") as namesList:
    with open("names.txt", "r+", encoding="UTF-8") as names:
        with open("lastnames.txt", "r+", encoding="UTF-8") as lastnames:
            if names.read(1) or lastnames.read(1):
                print("There is content in at least one of these files! Delete what's inside and try again")
            else:
                for line in namesList:
                    first_name = tuple(line.split())[0]
                    names.write(first_name + "\n")
                    if len(line.split()) > 1:
                        last_name = tuple(line.split())[1]
                        lastnames.write(last_name + "\n")
                    else:
                        lastnames.write("\n")

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
wordTotal = 0

try:
    with open(path, "r", encoding="UTF-8") as file:
            for line in file:
                words = line.lower().split().count(word)
                wordTotal += words
            print(f"File {path} contains {wordTotal} apperances of word {word}.")
except FileNotFoundError:
    print(f"There is no file {path}")
except PermissionError:
    print(f"You have no permission to open {path}")
    
