student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
# Read the csv file
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# create dictionary from the imported csv
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# is_not_valid = True
#
# # while not cause_error:
# while is_not_valid:
#     user_input = input("Enter a word ").upper()
#
# # loop through the user_input and return the code
#     try:
#         p_code = [new_dict[i] for i in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alpahabet please")
#     else:
#         is_not_valid = False
#         print(p_code)
#
# other solution by making it as function

def generate_phoenetic():
    user_input = input("Enter a word ").upper()
    # loop through the user_input and return the code
    try:
        p_code = [new_dict[i] for i in user_input]
    except KeyError:
        print("Sorry, only letters in the alpahabet please")
        generate_phoenetic()
    else:
        print(p_code)

generate_phoenetic()
