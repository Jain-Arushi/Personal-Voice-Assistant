import pyttsx3                  
                                
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser           
import os                  
import subprocess as sp
import smtplib

engine = pyttsx3.init('sapi5')   
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) # 0-male voice , 1-female voice


def speak(audio):   # speaks results 
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Emma. Please tell me how may I help you")       

def takeCommand():             

    r = sr.Recognizer() 
    with sr.Microphone() as source:    
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_calculator():
    sp.Popen(paths['calculator'])

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('arushipatni05@gmail.com', 'your-password')
    server.sendmail('arushipatni05@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()   #Converting user query into lower case

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open camera' in query:
            open_camera()

        elif 'open calcuator' in query:
            open_calculator()

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) #With the help of os.startfile, you can play any song of your choice.
                                                            #You can also play a random song with the help of a random module.
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to arushi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "arushipatni05@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")
        
        elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks you for using Jarvis")
            exit()

        

        
