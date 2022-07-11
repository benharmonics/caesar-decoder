# caesar-decoder
Makes a "best guess" decryption of text encoded using a Caesar cipher

Trivial script that makes the best guess at decoding a test encoded with some kind of Caesar cipher.
It tries all the possibilities and just returns the one(s) which match most frequently with 98 of the most
common English words.

It has no dependencies, if that matters to you. Unless you run the scraper, but the data is provided for you anyway.

Clone the repo, then you just need Python to run the script:

```bash
python decoder.py
```

Then the program will prompt you:

```
File or input text to decode: <enter encoded text>
```
