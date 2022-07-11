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

counts = []
for i in range(26):
    rotated_letters = []
    for c in text:
        if ord(c) < ord('z'):
            rotated_letters.append(chr(ord(c) + i))
        else:
            rotated_letters.append('a')
    test_text = ''.join(rotated_letters)

    count = 0
    for word in common_words:
        count += test_text.count(word)
    counts.append(count)

indices_of_maxima = []
for (i, count) in enumerate(counts):
    if count == max(counts): indices_of_maxima.append(i)

print("(Each rotation increments the letter; i.e. 'a' -> 'b', 'd' -> 'e', 'z' -> 'a')")
print(f'\nRotation(s) with most hits: {indices_of_maxima}')
print(f'Hit distribution: {counts}')
