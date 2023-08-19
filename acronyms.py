
def file_to_string(file_name, encoding):
    file = open_file_ext(file_name, 'r', encoding=encoding)
    file_content = file.read()
    file.close()
    return file_content


def has_acronym(file_content, acronym):
    if file_content.find(acronym) != -1:
        return True
    else:
        return False


def return_line(file_content, acronym):
    position = file_content.find(acronym)
    return position


def open_file_ext(file_name, operation, encoding):
    try:
        file = open(file_name, operation, encoding=encoding)
        if operation == 'r':
            print("File opened to read.")
        elif operation == 'w':
            print("File opened to write.")
        elif operation == 'a':
            print("File opened to append.")
        return file


    except:
        raise Exception("File could not be opened.")


def main():
    encoding = "utf-8"
    file_name = "acronyms.txt"
    acronym = input("What acronym do you want to add?\n").upper()
    definition = input("What is the definition?\n") + ';'

    file_content = file_to_string(file_name, encoding)

    if not has_acronym(file_content, acronym):
        file = open_file_ext(file_name, 'a', encoding)
        file.write(acronym + " - " + definition)
        file.close()
    else:
        print("Acronym already exists, do you want to refactor it?\n")
        refact_dec = input("y/n\n")
        if refact_dec == 'y':
            print()
            # refactoring logic
            pos = file_content.find(acronym) + len(acronym) + 3
            definition_old = ''
            while pos < len(file_content):
                char = file_content[pos]
                if char == ';':
                    break
                definition_old += char
                pos += 1
            file_content = file_content.replace(definition_old, definition)
            file = open_file_ext(file_name, 'w', encoding)
            file.write(file_content)
            file.close()
            print("File formated.")
        else:
            return


main()
