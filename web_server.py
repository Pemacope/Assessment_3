from flask import Flask
from flask import request
from flask import render_template

from datetime import datetime
import time
import sched
import logging

import random

import json
import get_apis

import pyttsx3

s = sched.scheduler(time.time, time.sleep)

app = Flask(__name__)

@app.route('/')
def main():
    """ Presents the html page, title, image, alarms and notifications """

    update_data()
    
    #Sets alarms and notifications empty because at the beggining of the program the alarms.json and notifications.json files need to be empty 
    alarms,notifications,log = [],[],None

    #store the notifications in the notifications.json file
    with open('notifications.json', 'w') as notifications_file:
        json.dump(notifications, notifications_file)

    #store the alarms in the alarms.json file
    with open('alarms.json', 'w') as alarms_file:
        json.dump(alarms, alarms_file)

    #store the alarms in the alarms.json file
    with open('sys.log', 'w') as log_file:
        json.dump(log, log_file)

    return render_template('index.html', title='Daily briefing', image = "favicon.ico", alarms = alarms, notifications = notifications)

@app.route('/index')
def index():
    """ Checks for user's input and calls functions according to said inputs """

    s.run(blocking = False)

    logging.basicConfig(filename = "sys.log", encoding = 'utf-8')

    notif = request.args.get('notif')

    #Checks if a notification close button has been clicked
    if notif:
        close_notification(notif)

    alarm = request.args.get('alarm_item')

    #Checks if a notification close button has been clicked
    if alarm:
        cancel_alarm(alarm)
    
    date = request.args.get("alarm")
    label = request.args.get("two")

    alarms,notifications = load_data()

    #Checks if the user has submitted an alarm to be scheduled
    if date and label:
        current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")

        #Checks if the user tried to set an alarm to an invalid date, an invalid date being a date in the past
        if hhmm_to_seconds(date) <= hhmm_to_seconds(current_time):
            announcement("An alarm can't be scheduled for a date in the past")
        else:
            news_check = request.args.get("news")
            weather_check = request.args.get("weather")

            date_formatted = date.replace("T"," ")
            news = False
            weather = False

            #check if the user wants to include a news briefing in the alarm
            if news_check:
                news = True

            #check if the user wants to include a weather briefing in the alarm
            if weather_check:
                weather = True

            alarm_dict = { "title": date_formatted, "content": label }

            alarms.append(alarm_dict)

            #store the alarms in the alarms.json file
            with open('alarms.json','w') as alarms_file:
                json.dump(alarms,alarms_file)

            schedule_announcement(date,news,weather)
            
    return render_template('index.html', title='Daily briefing', image = "favicon.ico", alarms = alarms, notifications = notifications)

def schedule_announcement(date: str,news: bool,weather: bool):
    """ Adds the alarm the user scheduled to the scheduler queue"""
    
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")
    delay = hhmm_to_seconds(date) - hhmm_to_seconds(current_time)
    s.enter(int(delay), 1, show_notifications,[news,weather])

    announcement("Alarm scheduled")
    
def show_notifications(news: bool,weather: bool):
    """ Presents the notification and deletes the alarm from the alarms.json file that set off said notification """

    #Get data from json files
    alarms,notifications = load_data()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open('public_health_england.json', 'r') as covid_file:
        covid_file = json.load(covid_file)
    
    daily_cases = int(covid_file["data"][0]['newCasesByPublishDate']) - int(covid_file["data"][1]['newCasesByPublishDate'])

    if daily_cases > 0 :
        percentage = (daily_cases / int(covid_file["data"][1]["newCasesByPublishDate"]))
        content = "There has been an increase of " + str(percentage) + "% in the number of cases since yesterday"
    elif daily_cases < 0 :
        percentage = (daily_cases / int(covid_file["data"][1]["newCasesByPublishDate"]))
        content = "There has been an decrease of " + str(percentage) + "% in the number of cases since yesterday"
    else :
        content = "There hasn't been an increase nor a decrease in the number of cases since yesterday"
    
    covid_dict = { "title": current_time + " " + covid_file["data"][0]["areaName"] + ": Covid update", "content": content} 
    
    notifications.append(covid_dict)

    #Checks if the user asked for the alarm to include a news briefing
    if news:
        with open('news.json', 'r') as news_file:
            news_file = json.load(news_file)

        #Choose a random arcticle
        r = random.randint(0,len(news_file["articles"])-1)

        article = news_file["articles"][r]["title"]

        news_dict = { "title": current_time + " " + covid_file["data"][0]["areaName"] + ": News update", "content": article} 

        notifications.append(news_dict)

    #Checks if the user asked for the alarm to include a weather briefing
    if weather:
        with open('weather.json', 'r') as weather_file:
            weather_file = json.load(weather_file)

        celsius = weather_file["main"]["temp"] - 272.157
        weather_description = weather_file["weather"][0]["description"] 

        weather_dict = { "title": current_time + " " + covid_file["data"][0]["areaName"] + ": Weather update", "content": "The temperature is: " + str(format(celsius, '.2f')) + " ºC and the weather is " + weather_description } 

        notifications.append(weather_dict)

    with open('notifications.json', 'w') as notifications_file:
        json.dump(notifications, notifications_file)

    #Removes the alarm from the alarms.json file since it has been triggered
    for alarm in alarms:
        if alarm["title"] == current_time[:16]:
            announcement(alarm["title"])
            announcement(alarm["content"])
            alarms.remove(alarm)

    with open('alarms.json', 'w') as alarms_file:
        json.dump(alarms, alarms_file)

def close_notification(notif):
    """ Closes the notification the user clicked on """
    
    with open('notifications.json', 'r') as notifications_file:
        notifications = json.load(notifications_file)
        
    for notification_dict in notifications:
        if notification_dict["title"] == notif:
            notifications.remove(notification_dict)
            break

    with open('notifications.json', 'w') as notifications_file:
        json.dump(notifications, notifications_file)

def cancel_alarm(alarm):
    """ Removes the alarm from the scheduler queue and from the alarms.json file """

    with open('alarms.json', 'r') as alarms_file:
        alarms = json.load(alarms_file)

    for alarm_dict in alarms:
        if alarm_dict["title"] == alarm:
            index = alarms.index(alarm_dict)
            s.cancel(s.queue[index])
            alarms.remove(alarm_dict)
            break

    announcement("Alarm cancelled")

    with open('alarms.json', 'w') as alarms_file:
        json.dump(alarms, alarms_file)

def hhmm_to_seconds(alarm_time: str):
    """ Converts the time from a hh_mm format to seconds """
    dataFormat = datetime.strptime(alarm_time,"%Y-%m-%dT%H:%M")

    return time.mktime(dataFormat.timetuple())

def load_data():
    """ Get alarms and notifications data from json files"""

    with open('notifications.json', 'r') as notifications_file:
        notifications = json.load(notifications_file)

    with open('alarms.json', 'r') as alarms_file:
        alarms = json.load(alarms_file)

    return alarms,notifications

def update_data():
    """Every hour the data from the apis will be updated"""

    get_apis.get_news()
    get_apis.get_weather()
    get_apis.get_covid()

    s.enter(3600,1,update_data)

def announcement(quote: str):
    """ Makes the computer read a quote out loud """
    
    engine = pyttsx3.init()
    
    engine.say(quote)
    engine.runAndWait()

if __name__ == '__main__':
    app.run()
