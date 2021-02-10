import pyttsx3
import speech_recognition as sr 
import pip 
import wikipedia
import webbrowser
import os
import pyjokes
import random
import smtplib
from requests import get
import sys
import datetime

#import code for gui

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_JarvisGUI 


 
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):

 engine.say(audio)
 print(audio)
 engine.runAndWait()

def wishme():

 hour = int( datetime .datetime.now().hour)
 if  hour>=0 and hour<12:
  speak("good morning!")
 elif hour>=12 and hour<18:
     speak("good afternoon!")
 else:
    speak("good evining!")
 speak(" hey, i am jarvis. how i may help you  ")

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    server.login('dilipkumarsuna4@gmail.com', 'dilip77500')
    server.sendmail('dilipkumarsuna4@gmail.com', to, content)
    server.close()

def jokes(): 
    my_joke= pyjokes.get_joke('en', category='neutral')
    print(my_joke)
    speak(my_joke)

class MainThread(QThread):
    def _init_(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
    
        except Exception as e:
            print(e)    
            print("Unable to Recognize your voice.")  
            return "None"
        
        return query


    def TaskExecution(self):
        wishme()

        while True:
            self.query = self.takeCommand().lower() 

            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)

            
            elif 'open youtube' in self.query:
                webbrowser.open("https://www.youtube.com/")

            elif 'open google' in self.query:
                webbrowser.open("https://www.google.com/")

            elif 'open news' in self.query:
                webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")

            elif 'search' in self.query or 'search in google' in self.query:
                self.query = self.query.replace("search", " ") 
                self.query = self.query.replace("search in google", " ")          
                webbrowser.open("https://www.google.com/#q=" + self.query + " ")
                

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open visual studio' in self.query:
                codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
                os.startfile(codePath)

            elif 'open pycharm' in self.query:
                codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
                os.startfile(codePath)

            elif 'open photoshop' in self.query:
                codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
                os.startfile(codePath)

            elif 'open chrome' in self.query:
                codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)

            elif 'open word' in self.query:
                codePath = "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                os.startfile(codePath)

            elif 'open excel' in self.query:
                codePath = "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                os.startfile(codePath)

            elif 'open powerpoint' in self.query:
                codePath = "C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
                os.startfile(codePath)


            elif 'email to dilip ' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "rinkusuna01@gmail.com"   
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
    
            elif 'send a mail' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    speak("whome should i send")
                    to = input()    
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")


            elif 'joke' in self.query:
                jokes()

            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "who i am" in self.query:
                speak("If you talk then definately your a human.")

            elif "why you came to world" in self.query:
                speak("Thanks to dilip. further It's a secret")
                
            elif "who are you" in self.query:
                speak("i am jarvis")

            elif "who made you" in self.query or "who created you" in self.query: 
                speak("I have been created by Dilip")

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is : {ip}")



            elif "exit" in self.query or "stop" in self.query:
                speak("okay")
                sys.exit(0)
            
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close) 
  
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/Dilip Kumar Suna/OneDrive/Desktop/Jarvis UI/7LP8.gif")     
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/Dilip Kumar Suna/OneDrive/Desktop/Jarvis UI/image4.gif")     
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/Dilip Kumar Suna/OneDrive/Desktop/Jarvis UI/image5.gif")     
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) 
        startExecution.start()  
 
    def showTime(self):
        current_time = QTime.currentTime()  
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
     
        

        

       
      
        



        
              

 
 
 


