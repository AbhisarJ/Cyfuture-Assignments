import whisper

model = whisper.load_model("turbo")
result = model.transcribe(audio="test_audio.mp3")
print(result["text"])

#Another way is to use the command line to do the same
#I can either specify the language or let the model detect it
#i will let it detect the language
#I used the turbo model but smaller models can be used for faster inference
# and we got the transcription