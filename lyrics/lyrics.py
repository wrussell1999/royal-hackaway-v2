import re

import nltk

from pprint import pprint
import code

def main():
    with open('lyrics/rap_god.txt') as f:
        rap_god = f.read()

    parts = parse_lyrics(rap_god)

    sent = Sentence(parts[0][0])

    next(sent.nouns()).set('cat')
    print(sent.generate())

def parse_lyrics(lyrics, clean = True):
    if clean:
        lyrics = re.sub('\[.*\]', '', lyrics)
        lyrics = lyrics.strip()

    verses = re.split('\n\n+', lyrics)
    verses = [line.split('\n') for line in verses]

    return verses

class Sentence:
    def __init__(self, contents):
        self._words = nltk.word_tokenize(contents)
        self._tagged_words = nltk.pos_tag(self._words)

    def generate(self):
        return ' '.join(self._words)

    def get(self, position):
        return self._tagged_words[position]

    def set(self, position, value):
        self._words[position] = value
        self._tagged_words = nltk.pos_tag(self._words)

    def nouns(self):
        for i, (word, tag) in enumerate(self._tagged_words):
            if tag[0] == 'N':
                yield Token(self, i)

class Token:
    def __init__(self, context, position):
        self._context = context
        self._position = position

    def get(self):
        return self._context.get(self._position)

    def set(self, value):
        return self._context.set(self._position, value)
