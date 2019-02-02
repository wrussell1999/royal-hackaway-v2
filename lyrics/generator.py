import os
import re
import random

import tswift

from .context import Context

class Generator:
    def __init__(self, songs):
        self.songs = songs

    def generate_lyrics(self, word):
        song = random.choice(self.songs)

        song = tswift.Song(*song)

        parts = self.parse_lyrics(song.lyrics)
        verse = parts[0]

        lyrics = []
        for line in verse:
            ctx = Context(line)
            nouns = list(ctx.nouns())
            if len(nouns) > 0:
                random.choice(nouns).set(word)

            lyrics.append(ctx.generate())

        return '\n'.join(lyrics)

    def parse_lyrics(self, lyrics, clean = True):
        if clean:
            lyrics = re.sub('\[.*\]', '', lyrics)
            lyrics = lyrics.strip()

        verses = re.split('\n\n+', lyrics)
        verses = [line.split('\n') for line in verses]

        return verses