import speech_recognition as sr
import os
import webbrowser
import datetime
import subprocess
import wikipedia
import wolframalpha
# import pyttsx3
# import winshell
import smtplib
import pyjokes
import requests
import shutil
import tkinter as tk
import ecapture
from bs4 import BeautifulSoup as bs







def say(words):
    os.system(f"say {words}" )  ##os.system function is used to execute a command in subshell


##wishing the user
def wish():
    time= datetime.datetime.now().hour
    if time>0 and time <12 :
        say("Good Morning sir")
    elif time<19:
        say("good afternoon sir")
    else:
        say("good evening sir")

    myname= "Rabida 1.0"
    say (f"i am your voice assistant {myname}")



##initializing the recognizer classn and listen command through google speech recognition api
def listen():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
        speech= r.recognize_google(audio, language="en-US" )

        try:
            print (f"you said: {speech}")
            return speech
        except Exception as e:
            return "Error encountered!!"

##sending email function

def sendemail(to, content):
    print("sending mail to", to)
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login("mailforpritesh@gmail.com", "Pritesh@98661")
    server.sendmail("mailforpritesh@gmail.com", to, content)
    server.close()

# def getWeather(place):
#     cityName=place.get() #getting input of name of the place from user
#     baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
#     url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName
#     response = requests.get(url)
#     x = response.json()
#
# #If there is no error, getting all the weather conditions
#     if x["cod"] != "404":
#         y = x["main"]
#         temp = y["temp"]
#         temp-=273
#         pressure = y["pressure"]
#         humidity = y["humidity"]
#         desc = x["weather"]
#         description = z[0]["description"]
#         info=(" Temperature= " +str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +"\n humidity = " +str(humidity)+"%" +"\n description = " +str(description))
#         print(info)
#         say("Here is the weather report at")
#         say(place)
#         say(info)
#     else:
#        say(" City Not Found ")

if __name__=='__main__':

    wish()

    say(" How can i help you?")

print ("I am your Voice Assistant")
while True:
    print("listening.......")
    query = listen().lower()


    if "exit" in query:
        exit()


    sites= [["google", 'https://www.google.com'], ['youtube', 'https://www.youtube.com'],['safari', 'https://www.safari.com'],
             ['gmail', 'https://www.gmail.com'], ['spotify', 'https://www.spotify.com'],['facebook', 'https://:www.facebook.com'],
             ['linkedin', 'https://www.linkedin.com'], ['instagram', 'https://www.instagram.com'],
            ['stackoverflow', 'stackoverflow.com']]
    for site in sites:
        if f"open {site[0]}".lower() in query:
             say("opening")
             webbrowser.open(site[1])


     ##to say date and time

    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    day=datetime.datetime.now().day
    hour= datetime.datetime.now().hour
    min= datetime.datetime.now().minute


    if "time" in query:
        if hour>12:
              hour=hour-12
        say(f"the time is {hour} hours and {min} minutes")

    monthlist=[[1,"january"], [2, 'february'], [3,'march'], [4, 'april'], [5,'may'], [6,'june'], [7,'july'], [8, 'august'], [9, 'september'],[10, 'october'], [11,'november'], [12,'december']]

    if "date" in query:
        for pmonth in monthlist:
            if month in pmonth:
                say(f" The date is  {day}, {pmonth[1]}, {year} ")



    if 'email' in query:
        try:
            say('who do you want me to send the email?')
            print("listening...")
            listen()
            say("what is the email address of the receipent")
            to=input("please type the email address: ")
            say('what do you want me to write')
            print("listening...")
            content=listen()
            sendemail(to,content)
        except Exception as e:
            print(e)

    if "wikipedia" in query:
        say("searching in wikipedia")
        query= query.replace("wikipedia", "")
        results= wikipedia.summary(query, sentences=3)
        print(results)
        say(results)

    if 'joke' in query:
        say(pyjokes.get_joke())
