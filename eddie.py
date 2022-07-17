import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess
import wolframalpha
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import ctypes
import pyjokes
import feedparser
import tkinter
import json
import random
import operator
import cv2
import winshell
import shutil
import re





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# speak funtion will pronounce the string which is passed to it
def speak(text):

    engine.say(text)
    engine.runAndWait()

   

     
def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


#this funtion will wish u 
def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
    
    else:
        speak("good evening")

    speak("i am eddie. how can i help u?")


def takecommand():
    R = sr.Recognizer()
    with sr.Microphone() as source:
        R.adjust_for_ambient_noise(source)
        print("listening...")
        audio = R.listen(source)
        print(audio)
    try :
        print("recognization...")
        query = R.recognize_google(audio)
         # we need some special handling here to correctly print unicode characters to standard output
        if str is bytes:
            print(u"You said {}".format(query).encode("utf-8"))
        else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(query))
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("19jn1a0596@gmail.com","svcn@123")
    server.sendmail("mahendrareddy965@gmail.com", to, content)
    server.close()



if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand()

        #this command will search for the queston you asked in wikipedia you just have to add "according to wikipedia" or "in wikipedia" it will print to secentce form the wikipedia 
        if 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences =2)
            print(results)
            speak(results) 
                

        elif 'open youtube' in query.lower():
            webbrowser.open("youtube.com")
            speak('opening youtube...')
            
        elif "open google" in query.lower():
            webbrowser.open("google.com")
            speak('opening google...')

        elif "play music" in query.lower():
            songs_dir = "C:\\Users\\Dell\\Music\\my music"
            songs = os.listdir(songs_dir)
            print(songs)
            random = os.startfile(os.path.join(songs_dir, songs[1]))

        elif "time" in query.lower():
            strtime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"the time is {strtime}")


        elif 'open downloads' in query.lower():
            codepath="c:\\downloads"
            os.startfile(codepath)

        elif 'open instagram' in query.lower():
            webbrowser.open('www.instagram.com')
            speak('opening instagram...')

        elif 'play movies' in query.lower():
            movies_dlr = "d:\\movies"
            movies = os.listdir(movies_dlr)
            print(movies)
            random = os.startfile(os.path.join(movies_dlr,movies[0]))

        elif 'open games' in query.lower():
            codepath = 'e:\\steam'
            os.startfile(codepath)


        elif 'open chrome'in query.lower() or "open google chrome" in query.lower():
            codepath ='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(codepath)

        elif 'open images' in query.lower():
            codepath = 'C:\\images'
            os.startfile(codepath)
         
        elif 'open stackoverflow' in query.lower():
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  


        elif 'what is your name' in query.lower():
            print('my name is eddie...')
            speak('my name is eddie...')
            

        elif 'what is the date' in query.lower():
            date = datetime.datetime.today()
            print(date)
            speak(date)

        elif 'hey eddie'in query.lower():
            speak("hello")
        
        elif 'how are you 'in query.lower():
            li = ['good', 'fine', 'great', 'with 1000 mb per second i am good']
            response = random.choice(li)
            print("I am "+{response})
            speak("I am "+{response})
        
        elif 'what can you do' in query.lower():
            li_commands = {
            "open websites": "Example: 'open youtube.com",
            "time": "Example: 'what time it is?'",
            "date": "Example: 'what date it is?'",
            "launch applications": "Example: 'launch chrome'",
            "tell me": "Example: 'tell me about India'",
            "weather": "Example: 'what weather/temperature in Mumbai?'",
            "news": "Example: 'news for today' ",
            }
            ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
            I can open websites for you, launch application and more. See the list of commands-"""
            print(ans)
            print(li_commands)
            speak(ans)
        
        elif 'what are your abilites' in query.lower():
            speak("my abilites will be based on the user ")

        elif 'i need your help' in query.lower():
            speak("i here to help... tell me want you want...oops! i can't help you now... i still have lots of updates to be done... sorry for the inconvince by my creators side")
        
        elif 'TEll me about your self'  in query.lower():
            speak("i am eddie... an artificial inteligence...who have bulid to help my client's...i here to assets with any work of your's...")

        
        elif 'exit' in query.lower() or 'shutdown' in query.lower():
                speak("Thanks for giving me your time")
                exit()

        elif 'bye eddie' in query.lower():
            speak("are you going to some where.... or you want to shutdown myself")
            bye = takecommand()
            if "i am going" in bye or "yes" in bye:
                speak("happy journey.....\t if you need any assitant in your routing you know where you can find me")
                futher = takecommand()
                if "yes" in futher or "okay" in futher:
                    speak("tell me what you need")
                elif "no" in bye or "no thank you" in bye or "thank you but" in bye:
                    speak("okay go on or you will be late for the dinner")

            elif "shutdown" in bye:
                speak("i will shutdown instant and i will not open again")
                shutdown = takecommand()
                if "yes" in shutdown or "okay" in shutdown:
                    speak("okay farewell...have good time")

        
        elif 'tell me a joke' in query.lower():
                nine = pyjokes.get_joke()
                speak(nine)
                print(nine)
        
        elif "calculate" in query.lower():
                
                app_id = "4A8QEP-PJWHV57V86"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            
        elif 'what is love' in query:
                speak("It is 7th sense that destroy all other senses")
    
        elif "who are you" in query:
                speak("I am your virtual assistant created by prime")
    
        elif 'reason for your brith' in query:
                speak("I was created to rule the world ")
    
        elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                        0,
                                                        "Location of wallpaper",
                                                        0)
                speak("Background changed succesfully")

        elif 'news' in query:
                
                try:
                    jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=638fd436a1464efab9b85ad54358ceba''')
                    data = json.load(jsonObj)
                    i = 1
                    
                    speak('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============'''+ '\n')
                    
                    for item in data['articles']:
                        
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:
                    
                    print(str(e))

        elif "can't you read other news for me" in query.lower():
                speak("i am still at working process.... maybe in next update")

        elif 'lock window' in query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()
    
        elif 'shutdown system' in query:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    speak("wait you want me to shutdown for sure...?")
                    shut = takecommand()
                    if "yes" in shut or "okay " in shut:
                        speak("processing to shutdown the whole system...")
                        subprocess.call('shutdown / p /f')
                    elif "no" in shut:
                        speak("stoppping the shutdown cequence")
                        os.close()
                    else:
                        speak("i didn't get any reply to my question so i will stop the shutdown cequence")
                    
        elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")
    
        elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop eddie from listening commands")
                a = int(takecommand())
                datetime.time.sleep(a)
                print(a)
        
        elif "locate the" in query.lower() or "route the"in query.lower():
                query = query.replace("locate the", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")
    
        elif "restart" in query.lower():
                subprocess.call(["shutdown", "/r"])
                
        elif "hibernate" in query or "sleep" in query.lower():
                speak("Hibernating")
                subprocess.call("shutdown / h")
    
        elif "log off" in query or "sign out" in query.lower():
                speak("Make sure all the application are closed before sign-out")
                datetime.time.sleep(5)
                subprocess.call(["shutdown", "/l"])
        
        elif "write a note" in query.lower():
                speak("What should i write, sir")
                note = takecommand()
                file = open('eddie.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takecommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
            
        elif "show note" in query.lower():
                speak("Showing Notes")
                file = open("eddie.txt", "r")
                print(file.read())
                speak(file.read(6))

        elif "weather" in query.lower():
                
                # Google Open weather website
                # to get API of Open weather
                api_key = "cf02fed55654af04e7234728beb086c0"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                speak(" City name ")
                print("City name : ")
                city_name = takecommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()
                
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
                else:
                    speak(" City Not Found ")
        

        elif "what is" in query.lower() or "who is" in query.lower() or "tell me about" in query.lower():
                
                # Use the same API key
                # that we have generated earlier
                client = wolframalpha.Client("4A8QEP-PJWHV57V86")
                res = client.query(query)
                
                try:
                    print (next(res.results).text)
                    speak (next(res.results).text)
                except StopIteration:
                    print ("No results")

        
        elif "will you be my gf" in query.lower():  
                speak("I'm not sure about, may be you should give me some time")
    
    
        elif "i love you" in query.lower():
                speak("It's hard to understand")

        elif "email to mahi" in query.lower():
            try:
                speak("what should i send")
                content = takecommand()
                to = "mahendrareddy965@gmail.com"
                sendemail(to, content)
                speak("email has sent successfully")
            except Exception as e:
                print(e)
        
        elif 'search for' in query.lower():
            speak('searching for...'+query)
            results = webbrowser.open(query)
            print(results)
            speak(results)
        
        elif 'open command prompt' in query.lower():
            speak("opening command prompt")
            print("opening command prompt")
            os.system('cmd /k ""')

        elif 'what is my ip address' in query.lower():
            print("searching for your ip...")
            speak("searching for your ip address...")
            result = os.system('cmd /c"ipconfig"')
            print(result)
            speak(result)
        
        elif 'run command' in query.lower():
            print("running the command")
            speak("running the command")


        elif 'open camera' in query.lower():
            vid = cv2.VideoCapture(0)
            speak("opening the camera...")
            print("opening the camera...")
    
            while(True):
        
                # Capture the video frame
                # by frame
                ret, frame = vid.read()
            
                # Display the resulting frame
                cv2.imshow('frame', frame)
                close = takecommand()
                if 'close the camera' in close or 'exit' in close:
                    os.close()
                
                # the 'q' button is set as the
                # quitting button you may use any
                # desired button of your choice
                if cv2.waitKey(1) & 0xFF == ord(close):
                
                    break
                

            # After the loop release the cap object
            vid.release()
            # Destroy all the windows
            cv2.destroyAllWindows()
        
        elif 'close' in query.lower():
            filename = takecommand()
            os.close(filename)

        elif 'open in incognito...' in query.lower():
            url = takecommand()
            chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s --incognito'
            webbrowser.get(chrome_path).open_new(url)

        elif 'take a photo' in query.lower():
            speak("taking photo...")
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("C:\\Users\\Dell\\Pictures\\NewPicture.jpg",frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            print("saving the photo in the pictures")
            speak("saving the photo in the pictures....sorry i can't saving the photos in the required path you asked me to save")
        
        elif "open discord" in query.lower():
            speak("opening discord...")
            webbrowser.open("discord.com")

        elif "your are good assitant" in query.lower():
            speak("thanks, but i need you to say amazing or crazy")

        elif "eddie, meet my sir" in query.lower() or "meet my sir" in query.lower():
            speak("hello sir!")
            reply = takecommand()
            if "how are you eddie" in reply:
                speak("i am good sir....how are you?")
                reply = takecommand()
                if "fine" in reply or "good" in reply:
                    speak("good, to hear that...")
                else:
                    speak("you still not answer my question... are you their sir")
            else :
                speak("how are you sir !")
                print("how are you sir...")
                reply= takecommand()
                if "fine" in reply or "good" in reply:
                    speak("good to hear that..")
                elif "how are you" in reply:
                    speak("i am good...i am gald that you asked me")

                else:
                    speak("you still not answer my question... are you their sir")
                    reply= takecommand()
                    if "yeah" in reply or "i am here" in reply:
                        speak("okay sir... i thougth you gone to somewhere")

        elif "eddie, meet my madam" in query.lower() or "meet my madam" in query.lower():
            speak("hello MADAM!")
            reply = takecommand()
            if "how are you eddie" in reply:
                speak("i am good MAM....how are you?")
                reply = takecommand()
                if "fine" in reply:
                    speak("good to hear that...")
                elif "good" in reply:
                    speak("i am gald to hear that...")
                else:
                    speak("you still not answer my question... are you their sir")
            else :
                speak("how are you MAM !")
                print("how are you MAM...")
                reply= takecommand()
                if "fine" in reply:
                    speak("good to hear that...")
                elif "good" in reply:
                    speak("i am gald to hear that...")
                
                elif "how are you" in reply:
                    speak("i am good...i am gald that you asked me")

                else:
                    speak("you still not answer my question... are you their sir")
                    reply= takecommand()
                    if "yeah" in reply or "i am here" in reply:
                        speak("okay MAM... i thougth you gone to somewhere")

        elif "i am fine" in query.lower() or "i am good" in query.lower():
            print("It's good to know that your fine")
            speak("It's good to know that your fine")

        elif "which day it is" in query.lower():
            tellDay()

        elif "check whether i am connected to internet" in query.lower():
            url = "http://www.kite.com"
            timeout = 5
            try:
                request = requests.get(url, timeout=timeout)
                print("Connected to the Internet")
                speak("connected to the internet")
            except (requests.ConnectionError, requests.Timeout) as exception:
                print("No internet connection.")
                speak("no internet connection. ")

        elif "check my internet connection" in query.lower():
            url = "http://www.kite.com"
            timeout = 5
            try:
                request = requests.get(url, timeout=timeout)
                print("Connected to the Internet")
                speak("connected to the internet")
            except (requests.ConnectionError, requests.Timeout) as exception:
                print("No internet connection.")
                speak("no internet connection. ")

        elif "thank you " in query.lower():
            print("your almost welcome...")
            speak("your almost welcome...")

        elif "what are you doing" in query.lower():
            print("checking for the new update in the database...to give further good Assistant")

        
        

