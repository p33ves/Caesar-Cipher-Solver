
from nltk.corpus import words
input_string = input("Enter the given string:").lower()
word_split = input_string.split()

for shift in range(1, 26):
    for this_word in word_split:
        possibility = list()
        for i in this_word:
            if ord(i) in range(ord('a'), ord('z') + 1):
                if ord(i)+shift > ord('z'):
                    possibility.append(chr(ord(i)+shift-26))
                else:
                    possibility.append(chr(ord(i)+shift))
            else:    
                possibility.append(i)
        new_word = ''.join(possibility)
        if new_word in words.words():
            print(f"Formed at Shift = {shift} for word: {this_word} as new word: {new_word}")