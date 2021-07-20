def fill_dictionary():
    dictionary_of_numbers = {}

    while True:
        key = input()
        if key == "Search":
            break
        value = input()
        if not value.isnumeric():
            print("The variable number must be an integer")
            print(dictionary_of_numbers)
            exit()
        if value == "Search":
            break
        number = int(value)
        dictionary_of_numbers[key] = number

    return dictionary_of_numbers


def find_in_store():
    searched = input()

    while searched != "Remove":
        print(numbers_dictionary.get(searched, "Number does not exist in dictionary"))
        searched = input()


def remove_from_store(dictionary_of_numbers):
    line = input()

    while line != "End":
        searched = line
        if searched in dictionary_of_numbers:
            del dictionary_of_numbers[searched]
        else:
            print("Number does not exist in dictionary")
            print(dictionary_of_numbers)
            line = input()
            continue

        print(dictionary_of_numbers)
        line = input()


numbers_dictionary = fill_dictionary()
find_in_store()
remove_from_store(numbers_dictionary)
