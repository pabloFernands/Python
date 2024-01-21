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
data = pandas.read_csv("nato_phonetic_alphabet.csv")

naut_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(naut_dictionary)
print(naut_dictionary["A"])


def create_nautic():
    '''Create Nautic words from letters'''
    word = input("Enter a word: ").upper()
    try:
        word_found = [naut_dictionary[letter] for letter in word]
    except KeyError:
        print("You need to put only letters.")
        create_nautic()
    else:
        print(word_found)

create_nautic()

