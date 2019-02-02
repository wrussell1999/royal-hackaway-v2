import os
import json

import tswift

from .generator import Generator

def main():
    ARTISTS = read_from_config('artists.json')

    SONGS = read_from_config('cache/songs.json')
    if SONGS is None:
        os.makedirs('cache/', exist_ok = True)

        SONGS = []
        for artist, songs in ARTISTS.items():
            if isinstance(songs, str):
                if songs == '*':
                    # all songs by artist
                    SONGS.extend((song.title, artist) for song in tswift.Artist(artist).songs)
                else:
                    # only one song by artist
                    SONGS.append((songs, artist))
            else:
                # multiple songs by artist
                SONGS.extend((song, artist) for song in songs)

        with open('cache/songs.json', 'w') as f:
            json.dump(SONGS, f, indent=4)

    gen = Generator(SONGS)

    lyrics = gen.generate_lyrics('cat')
    print(lyrics)

def read_from_config(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None
