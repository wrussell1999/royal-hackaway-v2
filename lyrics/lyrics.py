import re

import random

from pprint import pprint
import code

from .context import Context

def main():
    lyrics = generate_lyrics('cat')
    print(lyrics)

def generate_lyrics(word):
    with open('lyrics/rap_god.txt') as f:
        rap_god = f.read()

    parts = parse_lyrics(rap_god)
    verse = parts[0]

    lyrics = []
    for line in verse:
        ctx = Context(line)
        nouns = list(ctx.nouns())
        if len(nouns) > 0:
            random.choice(nouns).set(word)

        lyrics.append(ctx.generate())

    return '\n'.join(lyrics)

def parse_lyrics(lyrics, clean = True):
    if clean:
        lyrics = re.sub('\[.*\]', '', lyrics)
        lyrics = lyrics.strip()

    verses = re.split('\n\n+', lyrics)
    verses = [line.split('\n') for line in verses]

    return verses
