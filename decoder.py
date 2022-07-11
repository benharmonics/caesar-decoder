#!/bin/python

user_input = input('File or input text to decode: ')

try:
    with open(user_input, 'r') as f:
        source_text = f.read()
except:
    source_text = user_input
    if not source_text:
        print('No text entered.')
        quit()

text = ''.join([c.lower() for c in source_text if c.isalpha()])

with open('100commonwords.txt', 'r') as f:
    common_words = [word for word in f.read().split('\n') if not word.isspace()]

def rotate_text(i, input_text):
    rotated_letters = []
    for c in input_text:
        if ord(c) + i < ord('z'):
            rotated_letters.append(chr(ord(c) + i))
        else:
            overshoot = (ord(c) + i) - ord('z')
            letter = chr(ord('a') + overshoot - 1)
            rotated_letters.append(letter)
    return ''.join(rotated_letters)

counts = []
for i in range(26):
    test_text = rotate_text(i, text)

    count = 0
    for word in common_words:
        count += test_text.count(word)
    counts.append(count)

i_maxima = []
best_guesses = []
for (i, count) in enumerate(counts):
    if count == max(counts):
        i_maxima.append(i)
        best_guesses.append(rotate_text(i, text))

print("(Each rotation increments the letter; i.e. 'a' -> 'b', 'd' -> 'e', 'z' -> 'a')")
print(f'\nROTATION(S) WITH MOST HITS: {i_maxima}')
print(f'HIT DISTRIBUTION: {counts}')
print('BEST GUESS(ES):')
for guess in best_guesses:
    print(f'{guess}')
