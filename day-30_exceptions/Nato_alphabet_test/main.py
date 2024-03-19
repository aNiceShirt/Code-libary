import pandas

# data = pandas.read_csv("day-30_exceptions/Nato/nato_phonetic_alphabet.csv")

# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)


data = pandas.read_csv("day-30_exceptions/Nato_alphabet_test/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def Nato():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please input only letters from the alphabet")
        Nato()
    else:
        print(output_list)
Nato()