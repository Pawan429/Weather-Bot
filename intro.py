from gtts import gTTS 
import speech_recognition as sr
import os
import time

intro_text = "Hi! I'm shitzu. I am your personal weather bot. How can I help?"

def play_text(intro_text):

	intro_tts = gTTS(text=intro_text, lang='en')
	intro_tts.save('temp.mp3')
	time.sleep(0.8) 
	# play the converted audio 
	os.system("afplay temp.mp3") 
	os.remove("temp.mp3")
	os.system("afplay beep.mp3") 
	return()



#Eg: Whats the weather in philadelphia tomorrow

def listen_to_user():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("speak now")
		# read the audio data from the default microphone
		audio_data = r.record(source, duration=7)
		print("Recognizing...")
		# convert speech to text
		try:
			global text 
			text = r.recognize_google(audio_data)
			print(text)
		except:
			play_text("Sorry I didn't get that! can you repeat once again")
			listen_to_user()
	
	return(text)
