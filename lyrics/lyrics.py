import re

import random

from pprint import pprint
import code

from .context import Context

import tswift

def main():
    lyrics = generate_lyrics('cat')
    print(lyrics)

def generate_lyrics(word):
    song = tswift.Song(title='Rap God', artist='Eminem')

    parts = parse_lyrics(song.lyrics)
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
