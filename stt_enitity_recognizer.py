import speech_recognition as sr
import spacy

nlp = spacy.load("en_core_web_sm")
r = sr.Recognizer()

print("speak now")

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    doc = nlp(text)
    for ent in doc.ents: 
    	print(ent.text, ent.start_char, ent.end_char, ent.label_)

print(text)