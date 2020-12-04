# COVID Daily Breifing App

### Introduction
This alarm clock allows users to access information on the weather and current Covid-19 infection rates in their local area, as well as the top news headlines in the UK. It provides an easy and efficient way to stay up to date with the constantly-changing Covid-19 situation and keeps users informed and aware of the infection rates in their local area by displaying scheduled notification updates. 
### App Features
- Finds the location of the user to provide updates for their local area. 
- Provides weather, news, and Covid-19 infection rate updates. 
- The user can schedule and cancel alarms at any chosen time. 
- The notifications are updated every hour to efficiently track the events. 
- The announcement alarms use text-to-speech voice announcements and silent notifications are displayed.

### Prerequisites
  - Python 3.7+ (I am using version 3.9)
  - An IDE or texteditor (ex. Pycharm or Sublime)
  - [Weather] and [news] API keys
  - Stable internet connection and some programming knowledge:)
  
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
Alternatively, you could activate your virtualenv and run:
```sh
$ pip install -r requirements.txt
```

### How to use
- When the website is opened, the user interface should look like: 
(insert image of that)
- The user can click on the calendar icon to schedule the date and time of an announcement. 
- The user can also choose whether or not to include a weather and news briefing in the announcement. 
(insert image of that)
- Once the alarm is scheduled, it will be added to the alarms column:
(insert image of that)
- The user can cancel scheduled alarms by clicking on the “x” in the top right corner. 
- When the scheduled time is reached, a voice announcement will be made, reading the updated daily briefing.
- Silent notifications will appear in the notifications column, and will continuously be updated every hour.
(insert image of that)
- Silent notifications can be dismissed by clicking the “x” in the top right corner.


### Developer's guide
- Copy all provided files into a new directory 
- First, you will need to get API keys from the [weather] and [news] websites in order to complete the URL and have access to the updates.
- My code is set to provide news and Covid-19 updates in the Uk, and the current weather in Exeter. The region, as well as the news and types of updates extracted from the websites can be changed to fit your preference. 
- There are plenty of different options to customize the updates. For a full guide on how to access and implement these choices, follow the developer's guide on these websites: 
-- Weather: https://openweathermap.org/api
-- News: https://newsapi.org/docs/endpoints/sources
-- Covid-19: https://coronavirus.data.gov.uk/details/developers-guide
- The images displayed on user interface, announcement voice, and frequency of updates is customizable to suit your preference:
Check out https://pypi.org/project/pyttsx3/ for details on how to customize the text-to-speech function.
- The daily briefing can be easily changed to include updates of your choice by editing the the 'notification_dict' commands. 

### Testing 
- 

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
Copyright (c) [2020] [Zaina Al Shebli]
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
   
