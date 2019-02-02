import re

from pprint import pprint

def main():
    with open('lyrics/rap_god.txt') as f:
        rap_god = f.read()

    pprint(parse_lyrics(rap_god))

def parse_lyrics(lyrics, clean = True):
    if clean:
        lyrics = re.sub('\[.*\]', '', lyrics)
        lyrics = lyrics.strip()

    verses = re.split('\n\n+', lyrics)
    verses = [line.split('\n') for line in verses]

    return verses
