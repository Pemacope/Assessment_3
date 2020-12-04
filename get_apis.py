from uk_covid19 import Cov19API
import geocoder
import logging
import requests
import json

logging.basicConfig(filename = "sys.log", encoding = 'utf-8')

#get_location function
def get_location():
    """This function gets the location of the user"""
    current_location_data = geocoder.ip('me')

    return current_location_data.city

#get news function
def get_news() -> None:
    """Getting data from news api"""

    #Data request from the api
    base_url = "https://newsapi.org/v2/top-headlines?"

    with open('config.json', 'r') as config_file:
        temp = json.load(config_file)
        api_key = temp["keys"]["news_key"]
        
    country = "gb"

    complete_url = base_url + "country=" + country + "&apiKey=" + api_key

    response = requests.get(complete_url, timeout = 10)
    
    if response.status_code <= 400:
        logging.info('News request failed')
        
    #store news in file
    with open('news.json', 'w') as news_file:
        json.dump(response.json(), news_file)

#get weather function
def get_weather() -> None:
    """Getting data from weather API"""
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    with open('config.json', 'r') as config_file:
        temp = json.load(config_file)
        api_key = temp["keys"]["weather_key"]
        
    city_name = get_location()
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url, timeout = 10)
    
    if response.status_code >= 400:
        logging.info('Weather request failed')
            
    #store weather data in file
    with open('weather.json', 'w') as weather_file:
        json.dump(response.json(), weather_file)
        
#get uk covid numbers
def get_covid() -> None:
    """Getting data from uk covid api"""

    city_name = get_location()
    
    local_only = [
        'areaName={}'.format(city_name)
    ]
    data = {
        "date": "date",
        "areaName": "areaName",
        "newCasesByPublishDate": "newCasesByPublishDate"
    }
    api = Cov19API(filters = local_only, structure = data)

    covid_data = api.get_json()
                                    
    #store covid data in file
    with open('public_health_england.json', 'w') as covid_file:
        json.dump(covid_data, covid_file)
