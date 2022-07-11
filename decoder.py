#!/bin/python

# Get input: either input the name of a file to be read or
# the input text will be interpreted literally
user_input = input('File or input text to decode: ')
try:
    with open(user_input, 'r') as f:
        source_text = f.read()
except:
    source_text = user_input
    if not source_text:
        print('No text entered.')
        quit()

text = ''.join([c.lower() for c in source_text])

# get a list of ~100 of the most commonly used words in English
with open('100commonwords.txt', 'r') as f:
    common_words = [word for word in f.read().split('\n') if not word.isspace()]

def rotate_text(i, input_text):
    """Caesar cipher: rotate text by i letters"""
    rotated_letters = []
    for c in input_text:
        if c.isalpha():
            if ord(c) + i <= ord('z'):
                letter = chr(ord(c) + i)
            else:
                overshoot = (ord(c) + i) - ord('z')
                letter = chr(ord('a') + overshoot - 1)
        else:
            letter = c
        rotated_letters.append(letter)
    return ''.join(rotated_letters)

scores = []
for i in range(26):
    test_text = rotate_text(i, text)
    score = 0
    for word in common_words:
        # weight scores toward longer words
        score += test_text.count(word) * len(word)
    scores.append(score)

distribution = [s / sum(scores) for s in scores]

# When we rotate 14 positions in our rotate_text function, if you think about
# it, we're undoing 12 rotations in the encoding. So the encoding undone by
# by our function is 26 minus the number of steps we took.
percentages = [f'{round(100 * d, 1)}%' for d in reversed(distribution)]
# The final percentage now corresponds to 0 rotations (the one before it corresponds
# to 25 rotations). The first percentage corresponds to 1 rotation. Let's move the
# last percentage to the front of the array for formatting
percentages = [percentages[-1], *percentages[:-1]]

steps_to_maxima = []
best_guesses = []
for (i, count) in enumerate(scores):
    if count == max(scores):
        steps_to_maxima.append(i)
        best_guesses.append(rotate_text(i, text))
rotations = [26 - i for i in steps_to_maxima]

print("(Each rotation increments the letter; e.g. a → b, d → e, z → a)")
print(f'\nROTATION(S) WITH MOST HITS: {rotations}')
print('Try decoding the text transformed (a → b, b → c, etc)\nassuming '
      'the cipher was based on these numbers while being encoded.')
print(f'\nSCORE DISTRIBUTION:\nROT 0-12: {percentages[:13]}\nROT 13-25: {percentages[13:]}')
print('\nBEST GUESS(ES):')
for rot, guess in zip(rotations, best_guesses):
    output_len = 200
    end = min(output_len, len(guess) - 1)
    report = f'{guess[:end]}'
    if end == output_len:
        report += '...'
    print(f' • Encoded text interpreted as ROT{rot}, now decoded:')
    print(report)

