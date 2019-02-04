# Rap God

Rap God is our [creation](https://devpost.com/software/rap-god) from [Royal Hackaway](https://royalhackaway.com/).

We won the Nexmo Prize (best use of their API) and best audio hack.

After being inspired by a friend's creation of a rap bot, we decided to build a
bot that could alter existing rap songs to be about new topics. Then, of
course, we needed a way to access the bot, and we wanted to do something with
the [Nexmo API](https://www.nexmo.com/), so we decided that we would interface
with it using texts and phone calls.

## Tools

The entire project is built in python. We've used quite a few libraries, including:
- flask (for building a web server)
- nexmo (for interfacing with the nexmo platform)
- nltk (natural language processing)
- tswift (for fetching song lyrics)
- google-cloud-texttospeech (for text-to-speech)
- pydub (for layering 2 MP3 files ontop of eachother)

## Team

Our team was just two people,

- [Justin Chadwell](https://github.com/jedevc): Natural language processing and lyric generation
- [Will Russell](https://github.com/wrussell1999): Nexmo, flask, tts and mp3 layering

## Installation

To install:

```bash
$ git clone https://github.com/jedevc/royal-hackaway-2019.git
$ cd royal-hackaway-2019
$ virtualenv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

Before you can run, ensure that you have created the required files for the
Nexmo API and the Google Cloud Platform so that you can access their APIs.

To run:

```bash
python3 -m caller
```

...

## Technical details

Using the Nexmo API, we get the user to text our bot using SMS with the theme
they'd like to use for their own rap. Then, we select a random song from our
list of songs to use as a base. We then use NLP to tag the song and to modify
it so that we replace some of the nouns with our desired subject, effectively
changing what the song is about. The lyrics are converted into an MP3 with the Google Cloud TTS API, with a beat added behind them, using pydub, to create the rap.

The result is then sent back to the user. This is done with a phone call, where
the rap is played back to them.
