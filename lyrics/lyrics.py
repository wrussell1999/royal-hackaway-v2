import os
import json

import tswift

from .generator import Generator

CONFIG = 'config.json'

CACHE = 'cache/'
SONG_CACHE = 'cache/songs.json'

def main():
    with open(CONFIG) as f:
        config = json.load(f)

    if not os.path.exists(SONG_CACHE) or is_more_recent(CONFIG, SONG_CACHE):
        os.makedirs(CACHE, exist_ok = True)

        cache = []
        for artist, songs in config.items():
            if isinstance(songs, str):
                if songs == '*':
                    # all songs by artist
                    cache.extend((song.title, artist) for song in tswift.Artist(artist).songs)
                else:
                    # only one song by artist
                    cache.append((songs, artist))
            else:
                # multiple songs by artist
                cache.extend((song, artist) for song in songs)

        with open(SONG_CACHE, 'w') as f:
            json.dump(cache, f, indent=4)
    else:
        with open(SONG_CACHE) as f:
            cache = json.load(f)

    gen = Generator(cache)

    lyrics = gen.generate_lyrics('cat')
    print(lyrics)

def is_more_recent(fp1, fp2):
    return os.path.getmtime(fp1) > os.path.getmtime(fp2)
