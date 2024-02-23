from problem_1.utils import alphabet_count

def get_missing_letters(string:str):
    alphabet = list(alphabet_count.keys())
    formatted_string = string.lower().replace(" ", "")
    for letter in formatted_string:
        if letter in alphabet:
            alphabet_count[letter] += 1

    return "".join([missing_letter for missing_letter in alphabet_count if alphabet_count[missing_letter] == 0 ])
    
sentence = "lionel messi is the best footballer in the world"

print(get_missing_letters(sentence))