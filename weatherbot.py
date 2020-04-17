from intro import play_text,listen_to_user, intro_text
from stt_enitity_recognizer import entity_extractor, date_text_converter,get_woeid,get_weather_data




play_text(intro_text)

spoken_text = listen_to_user()

city_name, date = entity_extractor(spoken_text)

city_name = city_name[0]

date = date_text_converter(date)

print(date)

# Weather_condition = get_weather_data(date,get_woeid(city_name))


# weather_text = "As per the last updated value, the weather in " + str(city_name) + " was " + str(Weather_condition['weather_state_name'])


# play_text(weather_text)





# woeid = get_woeid(city_name)

# weather_data = get_weather_data(date,woeid)

# print(weather_data['weather_state_name'])