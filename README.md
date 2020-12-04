# COVID Daily Briefing App

### Introduction
This daily briefing alarm clock provides the user with easy access to the latest information on covid infection rates and weather in their local area, as well as the top UK headlines. 
### App Features
- Finds the location of the user to provide updates for their local area. 
- Provides Covid-19 infection rate, news and weather updates. 
- The user has the capability of scheduling and canceling alarms at any chosen time. 
- The data is updated every hour to ensure the user receives recent and up to date information. 
- The alarm clock utilizes text-to-speech voice announcements for immediate notificatinos and displays silent notifications.

### Prerequisites
  - Python 3.7+ (I am using version 3.9)
  - An IDE or texteditor (ex. Pycharm or Idle)
  - [Weather] and [news] API keys
  - Stable internet connection
  
### Installation
> Packages in the requirement.txt file need to be installed first using pip: 

To install **flask**, run:
```sh
$ pip install Flask
```
To install **requests**, run:
```sh
$ pip install requests
```
To install **pyttsx3**, run:
```sh
$ pip install pyttsx3
```
To install **geopy**, run:
```sh
$ pip install geopy
```
To install **uk-covid19**, run:
```sh
$ pip install uk-covid19
```
### How to use
- When the website is opened, the user interface should look like: 

- The user can click on the calendar icon to schedule the date and time of an announcement. 
- The user can also choose whether or not to include adittional briefings in the announcement through two chceckboxes, one to include a news briefing and another to include a weather briefing . 
- Once the alarm is scheduled, it will be added to the alarms column on left-hand side of the HTML page and a voice will report the sucessful scheduling.
- The user can cancel scheduled alarms by clicking on the “x” in the top right corner of said alarm and a voice announcement will report the alarm canceling. 
- When the scheduled time is reached, a voice announcement will be made, reading the alarm responsible for the notification or notifications shown.
- Silent notifications will appear in the notifications column on the right-hand side of the HTML page.
- Silent notifications can be dismissed by clicking the “x” in the top right corner.


### Developer's guide
- Copy all provided files into a new directory 
- First, you will need to get API keys from the [weather] and [news] websites in order to complete the URL and have access to the updates.
- The daily briefing will give covid numbers and weather information from the location in the UK where the user is located and the news will be from the UK as a whole.
- The daily briefing can be easily changed to include updates of your choice by editing the the 'notification_dict' commands. 

### Links and Sources
- Weather API: https://openweathermap.org/api
- News API: https://newsapi.org/docs/endpoints/sources
- Covid-19 API: https://coronavirus.data.gov.uk/details/developers-guide
- Pyttsx3 guide: https://pypi.org/project/pyttsx3/ 
- Requests guide: https://realpython.com/python-requests/
- Flask guide: https://flask.palletsprojects.com/en/1.1.x/quickstart/
- Requirements.txt guide: https://www.jetbrains.com/help/pycharm/managing-dependencies.html

### License
----
Copyright (c) [2020] [Pedro Miguel Catarino da Silva Pereira]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files "covid-daily-briefing-app", to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.






   [weather]: <https://openweathermap.orgr>
   [news]: <https://newsapi.org/>
   
