
def file_to_string(file_name, encoding):
    file = open_file_ext(file_name, 'r', encoding=encoding)
    file_content = file.read()
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
        with open(file_name, operation, encoding=encoding) as file:
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
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition?\n")

    file_content = file_to_string(file_name)

    operation_switcher = (
        'r', 'w', 'a'
    )

    if not has_acronym(file_content, acronym):
        file = open_file_ext(file_name, 'w', encoding)
        file.write(acronym + " - " + definition + "\n")

        file_content = file_to_string(file_name)
        # print("Line")

    try:
        with open(file_name, operation_switcher[2], encoding=encoding) as file:

            if not has_acronym(file_content, acronym):
                file.write(acronym + " - " + definition + "\n")
                # print("Line")
                return
            else:
                print("Acronym already exists, do you want to refactor it?\n")
                refact_dec = input("y/n\n")
                if refact_dec == 'y':
                    return_line(file_content, acronym)
                return

    except:
        raise Exception("File could not be opened.")


main()
