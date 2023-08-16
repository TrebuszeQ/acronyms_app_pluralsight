
def file_to_string(file_name):

    with open(file_name, 'r', encoding="utf-8") as file:
        file_content = file.read()
    return file_content


def has_acronym(file_content, acronym):
    if file_content.find(acronym) != -1:
        return True
    else:
        return False


def main():
    file_name = "acronyms.txt"
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition?\n")

    file_content = file_to_string(file_name)

    try:
        with open(file_name, 'a', encoding="utf-8") as file:

            if not has_acronym(file_content, acronym):
                file.write(acronym + " - " + definition + "\n")
                print("Line")
                return
            else:
                print("Acronym already exists added.")
                return

    except:
        raise Exception("File could not be opened.")

main()