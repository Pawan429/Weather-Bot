import spacy
import pandas as pd
import requests, json
from jsonpath_ng import jsonpath, parse
import datetime
from timefhuman import timefhuman

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 


def date_text_converter(date_entity):
	if date_entity == 'today':
		new_date_entity = today
	elif date_entity == "tomorrow":
		new_date_entity = tomorrow
	elif date_entity == "yesterday":
		new_date_entity = yesterday
	else:
		new_date_entity = date_entity[0]

	new_date_entity = timefhuman(new_date_entity)

	return(new_date_entity.strftime("%Y/%m/%d"))


def entity_extractor(text):
	nlp = spacy.load("en_core_web_sm")
	doc = nlp(text)
	entity_data = [[ent.text, ent.start_char, ent.end_char, ent.label_] for ent in doc.ents] 
	entity_df = pd.DataFrame(entity_data, columns = ['text','start_char','end_char','entity'])
	print(entity_df)
	entity_dict = {}
	location_entity = [row['text'] for index, row in entity_df.iterrows() if row['entity'] == 'GPE']
	date_entity = [row['text'] for index, row in entity_df.iterrows() if row['entity'] == 'DATE']
	return(location_entity,date_entity)
			

def get_woeid(city_name):
	woeid_url = "https://www.metaweather.com/api/location/search/?query=" + city_name

	woeid_resp = requests.get(woeid_url)

	# print(woeid_resp.content)

	woeid_resp_dict = json.loads(woeid_resp.content)

	woeid = woeid_resp_dict[0]["woeid"]

	# print("the woeid is " + str(woeid))
	return(woeid)


def get_weather_data(date,woeid):
	url = 'https://www.metaweather.com/api/location/' + str(woeid) +"/" +date

	response = requests.get(url)

	resp_dict = json.loads(response.content)

	path = parse('$..weather_state_name')

	created_list = [match.value for match in path.find(resp_dict)]
	# print(len(created_list))

	# print(resp_dict[0])
	return(most_frequent(created_list))


#most frequent element in list
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num



# print(tomorrow)