import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access api_key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        # print(row.score)
        pass

nato = pd.read_csv("./nato_phonetic_alphabet.csv")

#
# word = input("Enter a word : ")
# for i in word.upper():
#     for (index, row) in nato.iterrows():
#         if i in row.letter:
#             print(i, row.code)


# # TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# new_d = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(new_d)
#
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word : ")
#
# for i in word.upper():
#     for (api_key, value) in new_d.items():
#         if i in api_key:
#             print(i, value)


# #TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(phonetic_dict)
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#


def gene():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("only letters")
        gene()
    else:
        print(output_list)


gene()