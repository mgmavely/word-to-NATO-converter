import pandas

# Loop through rows of a data frame
with open("nato_phonetic_alphabet.csv") as data:
    new_data = pandas.read_csv(data)
    new_data_frame = pandas.DataFrame(new_data)
    for (index, row) in new_data_frame.iterrows():
        code_words = {row.letter: row.code for (index, row) in new_data_frame.iterrows()}



while True:
    inp = input("Enter a word! ")
    try:
        inp_to_code_words = [code_words[i.upper()] for i in inp]
        print(inp_to_code_words)
        break
    except KeyError:
        print("Sorry, only letters in the alphabet")
