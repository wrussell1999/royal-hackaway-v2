import json

import tswift

from .generator import Generator

def main():
    ARTISTS = read_from_config('artists.json')
    SONGS = read_from_config('cache/songs.json')
    if SONGS is None:
        os.makedirs('cache/', exist_ok = True)

        SONGS = [(song.title, artist) for artist in ARTISTS for song in tswift.Artist(artist).songs]

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
