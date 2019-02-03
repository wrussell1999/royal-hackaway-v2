from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

def make_mp3(text, filename):
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

    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open(filename, 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
