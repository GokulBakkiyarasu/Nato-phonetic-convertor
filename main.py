import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word that has to be converted into a nato_phonetic word list: ").upper()
nato_list = [nato_dictionary[letter] for letter in word]
print(nato_list)
