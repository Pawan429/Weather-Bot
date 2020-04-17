from gtts import gTTS 
import os

intro_text = "Hi! I'm shitzu. I am your personal weather bot. How can I help?"

def play_text(intro_text):

	intro_tts = gTTS(text=intro_text, lang='en')
	intro_tts.save('intro.mp3')

	# play the converted audio 
	os.system("afplay intro.mp3") 
	return()

# play_text(intro_text)

