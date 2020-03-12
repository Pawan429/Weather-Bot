import requests, json

from jsonpath_ng import jsonpath, parse

city_name = "Philadelphia"

woeid_url = "https://www.metaweather.com/api/location/search/?query=" + city_name

woeid_resp = requests.get(woeid_url)

print(woeid_resp.content)

woeid_resp_dict = json.loads(woeid_resp.content)

woeid = woeid_resp_dict[0]["woeid"]

print("the woeid is " + str(woeid))


url = 'https://www.metaweather.com/api/location/' + str(woeid) +'/2020/03/07/'

response = requests.get(url)

resp_dict = json.loads(response.content)

path = parse('$..weather_state_name')

created_list = [match.value for match in path.find(resp_dict)]
# print(len(created_list))

print(resp_dict[0])
print(resp_dict[0]['weather_state_name'])

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
# import os 

# The text that you want to convert to audio 
mytext = 'the weather in '+ city_name+' is ' + str(resp_dict[0]['weather_state_name'])

import pyglet

tts = gTTS(text=mytext, lang='en')
filename = 'temp.mp3'
tts.save(filename)

import os
os.system("afplay temp.mp3") 
