import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def convertor():
    word = input("Enter the word that has to be converted into a nato_phonetic word list: ").upper()
    # used  in oder if the user have entered white along the beginning or ending of the word 
    word = word.strip()
    try:
        nato_list = [nato_dictionary[letter] for letter in word]
        print(nato_list)
    except KeyError:
        print("Sorry, please enter a letter in alphabet.")
        convertor()


convertor()
