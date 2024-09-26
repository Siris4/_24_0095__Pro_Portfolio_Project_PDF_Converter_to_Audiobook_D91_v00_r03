from google.cloud import texttospeech
from google.oauth2 import service_account

# Path to your service account key file
key_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0095__Day91_Pro_Portfolio_Project_PDF_Converter_to_Audiobook__240925\NewProject\r00_env_START\r03\siris-speaks-a3c7c1b182ec.json'

# Authenticate using the service account credentials
credentials = service_account.Credentials.from_service_account_file(key_path)

# Set up the Text-to-Speech client with the credentials
client = texttospeech.TextToSpeechClient(credentials=credentials)

# Define the text you want to convert into speech
text = """This is Siris, testing out this program. I need to test it to see if it will go beyond 200 total characters and how everything will be handled beyond a certain point. You tell me. Is this working? Is it not? Does it break? Does it give an error? This should be 200 characters by now, right? God, I hope so. testing, testing, 1 2 3..."""

# Set up the input for the API
synthesis_input = texttospeech.SynthesisInput(text=text)

# Configure the voice parameters
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",  # Change to your preferred language
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL  # Can be FEMALE or MALE
)

# Specify the audio file format
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3  # Other options include LINEAR16 (WAV)
)

# Call the Text-to-Speech API
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# Save the synthesized speech to an output file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to file 'output.mp3'")
