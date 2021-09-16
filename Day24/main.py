# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("my_file.txt", mode="a") as file:
#     file.write("\nHere is some new text")
#
# with open("new_file.txt", mode="w") as file:
#     file.write("Some more text")

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
