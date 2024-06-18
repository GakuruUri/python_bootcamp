import pandas

data = pandas.read_csv("/home/uriroots/python_bootcamp/day_26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)

# {"A": "Alfa", "B": "Bravo"}

def generate_phonetic():
    word = input("ENter a word: ").upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()