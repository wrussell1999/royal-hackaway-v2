import os
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

def make_mp3(text, filename):
    print("Starting sound synthesis...")
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
        speaking_rate=0.70,
        pitch=-15.0)

    os.makedirs(os.path.dirname(filename), exist_ok = True)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open(filename, 'w+b') as out:
        out.write(response.audio_content)
        print(f'Audio content written to {filename}')
