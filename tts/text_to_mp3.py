from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

test_data = '''I'm beginning to feel like a Rap God, Rap God
All my people from the front to the back nod, back nod
Now who thinks their arms are long enough to slap box, slap box?
They said I rap like a robot, so call me Rapbot'''
synthesis_input = texttospeech.types.SynthesisInput(text=test_data)

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
with open('output.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
