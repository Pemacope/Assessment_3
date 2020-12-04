import geocoder
import requests
import json

#get_location function
def get_current_location():
    """This function gets the location of the user"""
    current_location_data = geocoder.ip('me')

    return current_location_data.city

#get news function
def get_news():
    """Getting data from news api"""

    #Data request from the api
    base_url = "https://newsapi.org/v2/top-headlines?"

    with open('config.json', 'r') as config_file:
        temp = json.load(config_file)
        api_key = temp["keys"]["news_key"]
        
    country = "gb"

    complete_url = base_url + "country=" + country + "&apiKey=" + api_key

    response = requests.get(complete_url, timeout = 10)
    
    if response.status_code >= 400:
        print('News request failed')
        
    #store news in file
    with open('news.json', 'w') as news_file:
        json.dump(response.json(), news_file)

#get weather function
def get_weather():
    """Getting data from weather API"""
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    with open('config.json', 'r') as config_file:
        temp = json.load(config_file)
        api_key = temp["keys"]["weather_key"]
        
    city_name = get_location()
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url, timeout = 10)
    
    if response.status_code >= 400:
        print('Weather request failed')

    #The relevant weather information is for me the Air Temperature and the Weather Description
    ##response = response.json()
    ##celsius = response["main"]["temp"] - 272.15
    ##weather_description = response["weather"][0]["description"]   
            
    #store weather data in file
    with open('weather.json', 'w') as weather_file:
        json.dump(response.json(), weather_file)
        
#get uk covid numbers
def get_covid():
    """Getting data from uk covid api"""
    
    base_url ='https://api.coronavirus.data.gov.uk/v1/data?'

    city_name = get_location()
    
    filters = 'filters=areaType=ltla;areaName='+city_name

    structure = 'structure={"areaName":"areaName", "date":"date","newCases":"newCasesByPublishDate","cumCasesByPublishDate":"cumCasesByPublishDate"}'

    complete_url = base_url + filters + '&' + structure
    
    response = requests.get(complete_url, timeout = 10)

    if response.status_code >= 400:
        print('Covid request failed')
                                            
    #store covid data in file
    with open('public_health_england.json', 'w') as covid_file:
        json.dump(response.json(), covid_file)
