import datetime
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voices' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I'm Shanky your voice assistant Please tell me how may i help you ?")


def takeCommand():
    #it takes microphone input from user and returns string input.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio , language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("shankarkarande5008@gmail.com",'Neymarjr@5008')
    server.sendmail('shankarkarande5008@gmail.com' , to , content)
    server.close()

    

if __name__ == "__main__":
    # speak("shankar is good boy")
    wishMe()
    while True:
        query = takeCommand().lower()
    
    #logic for executing tasks based on query.

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D\\yourpath'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\Shankar Karande\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'email to shankar' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "shankukarande@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry my friend shankar. I am not able to send this email")