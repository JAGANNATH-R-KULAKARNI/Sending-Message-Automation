
import smtplib
import speech_recognition as spr
from email.message import EmailMessage
import pyttsx3 as talker
import pyaudio

talkEngine = talker.init()
listener= spr.Recognizer()

def speak(text):
    print(text)
    talkEngine.say(text)
    talkEngine.runAndWait()

def getTheMessage():
    try:
        with spr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize(voice)
            print(info)
            return info.lower()
    except:
        pass

def Sendemail():
    smtpServer=smtplib.SMTP('smtp.gmail.com',587)
    smtpServer.starttls()
    smtpServer.login('jagbottest@gmail.com','1!2@3#4$')
    emailFormat=EmailMessage()
    emailFormat['From']='jagannath R Kulakarni'
    emailFormat['To']='jagannathrkulakarni.171845@gmail.com'
    speak('Tell me the subject for your email')
    emailFormat['Subject']=getTheMessage()
    speak('Tell me the message for your email')
    emailFormat.set_content(getTheMessage())
    smtpServer.send_message(emailFormat)