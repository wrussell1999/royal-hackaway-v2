import re
import os
import json
import argparse

import random

from pprint import pprint
import code

from .context import Context

import tswift

def main():
    gen = Generator()

    lyrics = gen.generate_lyrics('cat')
    print(lyrics)

class Generator:
    def __init__(self):
        self.songs = None
        self.fetch_data()

    def fetch_data(self):
        try:
            with open('cache/songs.json') as f:
                self.songs = json.load(f)
        except FileNotFoundError:
            os.makedirs('cache/', exist_ok = True)

            with open('artists.json') as f:
                artists = json.load(f)

            self.songs = [(song.title, artist) for artist in artists for song in tswift.Artist(artist).songs]

            with open('cache/songs.json', 'w') as f:
                json.dump(self.songs, f, indent=4)

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
