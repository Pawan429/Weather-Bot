from intro import play_text,listen_to_user, intro_text
from stt_enitity_recognizer import entity_extractor, date_text_converter,get_woeid,get_weather_data




play_text(intro_text)

spoken_text = listen_to_user()

city_name, date = entity_extractor(spoken_text)

city_name = city_name[0]
print(get_woeid(city_name))

date = date_text_converter(date)

print(type(date))
print(date)

Weather_condition = get_weather_data(date,get_woeid(city_name))

print(Weather_condition)

weather_text = "As per the last updated value, the weather in " + str(city_name) + " was " + str(Weather_condition)


play_text(weather_text)

