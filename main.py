import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = pd.Series(df.code.values, index=df.letter).to_dict()
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
# Create a list of phonetic code words
phonetic_list = [nato_dict[letter] for letter in word if letter in nato_dict]

print(phonetic_list)


