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

text = source_text.lower()

# get a list of ~100 of the most commonly used words in English
with open('100commonwords.txt', 'r') as f:
    common_words = [word for word in f.read().split('\n')]

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

# We'll score each possible rotation based on how many
# hits it scores when compared to our common words list
scores = []
for i in range(26):
    test_text = rotate_text(i, text)
    score = 0
    for word in common_words:
        # weight scores toward longer words
        score += test_text.count(word) * len(word)
    scores.append(score)

# Score distribution (percentage of total)
distribution = [s / sum(scores) for s in scores]

percentages = [f'{round(100 * d, 1)}%' for d in reversed(distribution)]
# When we reversed the distribution, we put the 'null' rotation at the end
# of the list; let's move it back to the beginning for formatting
percentages = [percentages[-1], *percentages[:-1]]

steps_to_maxima = []
best_guesses = []
for (i, score) in enumerate(scores):
    if score == max(scores):
        steps_to_maxima.append(i)
        best_guesses.append(rotate_text(i, text))
# When we rotate 14 positions in our rotate_text function, if you think about
# it, we're undoing 12 rotations in the encoding. So the encoding undone by
# by our function is 26 minus the number of steps we took.
rotations = [26 - i for i in steps_to_maxima]

print("(Each rotation increments the letter; e.g. a → b, d → e, z → a)")
print('Try decoding the text transformed (a → b, b → c, etc)\nassuming '
      'the cipher was based on these numbers while being encoded;\ni.e. if '
      'the rotation with the most hits is 14, the cipher was\ndetermined to be '
      'likely encoded with ROT14.')
print(f'\nROTATION(S) WITH MOST HITS: {rotations}')
print(f'\nSCORE DISTRIBUTION:')
for i, percentage in enumerate(percentages[::2]):
    pad_length = len('ROT XX-XX:')
    init_str = f'ROT {2 * i}-{2 * i + 1}:'
    final_str = init_str + " " * (pad_length - len(init_str))
    print(f'{final_str} {percentage} {percentages[2 * i + 1]}')
print('\nBEST GUESS(ES):')
for rot, guess in zip(rotations, best_guesses):
    output_len = 200
    end = min(output_len, len(guess) - 1)
    report = f'{guess[:end]}'
    if end == output_len:
        report += '...'
    print(f' • Encoded text interpreted as ROT{rot}, now decoded:')
    print(report)

