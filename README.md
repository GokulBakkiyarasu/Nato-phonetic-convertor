# NATO Phonetic Converter

![Screenshot (10)](https://user-images.githubusercontent.com/87391223/230646581-422a0993-4732-49d8-bb6f-f4d49f5341da.png)


This Python program converts a user input string into a list of NATO phonetic code words using the NATO phonetic alphabet data stored in a CSV file. It utilizes the pandas library to read the CSV data into a dictionary.
Requirements

    Python 3.x
    pandas library

## Installation

    Clone or download this repository to your local machine.
    Install the required pandas library by running pip install pandas in your terminal.

## Usage

    Run the main.py file using your Python interpreter.
    Enter a word that you want to convert into NATO phonetic code words when prompted.
    The program will output a list of NATO phonetic code words corresponding to the letters in the input word.



  Enter the word that has to be converted into a nato_phonetic word list: Hello
   Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

## How it works

    The program reads the NATO phonetic alphabet data stored in a CSV file using pandas.
    A dictionary comprehension is used to create a dictionary that maps each letter to its corresponding NATO phonetic code word.

Dictionary comprehension:
```python
  nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}
```
    The user is prompted to input a word that they want to convert into NATO phonetic code words.
    The input word is converted to uppercase and split into a list of individual characters.
    A list comprehension is used to convert each character in the list to its corresponding NATO phonetic code word using the dictionary created in step 2.

List comprehension:
```python
  nato_list = [nato_dictionary[letter] for letter in word]
  ```
  The resulting list of NATO phonetic code words is printed to the console.
