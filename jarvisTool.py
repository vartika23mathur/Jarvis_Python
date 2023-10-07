import openai
from apiket import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime


openai.api_key=api_data

completion=openai.Completion()


def Reply(question):
    prompt=f'Vartika: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Vartika'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello How Are You? ")


def wishMe():
      hour = int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
            speak("Good Morning! Please tell me how may I help you")

      elif hour>=12 and hour<18:
            speak("Good Afternoon! Please tell me how may I help you")
      else:
            speak("Good Evening!")
            speak("I am Jarvis Sir. Please tell me how may I help you")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print("Vartika Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query




if __name__ == '__main__':
      wishMe()
    while True:
        query=takeCommand().lower()
        ans=Reply(query)
        print(ans)
        speak(ans)
        #verify(ans)
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
                 webbrowser.open("google.com")
        elif 'open amazon' in query:
                 webbrowser.open("amazon.com") 


        elif 'play music' in query:
                 music_dir='C:\\Users\\hp\\Music\\SONGS'
                 songs = os.listdir(music_dir)
                 print(songs)
                 os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
                 strTime = datetime.datetime.now().strftime("%H:%M:%S")
                 speak(f"Sir, the time is {strTime}")
           
        elif 'open code' in query:
                 codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code"
        
        if 'bye' in query:
                  break
            
       
