import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
import os
from gtts import gTTS
import pygame
# from google import genai
# from google.genai import types
# import google.generativeai as genai

recognizer =sr.Recognizer()
engine=pyttsx3.init()
newsapi="ef7c4b0a43234333bc3a90d04eb09c86"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 
   
    # Initialize the mixer module
    pygame.mixer.init()
    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")
    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10) 

    pygame.mixer.music.unload()    
    os.remove("temp.mp3")     

def aiProcess(command):
    # Store your API key securely in an environment variable
    os.environ["OPENAI_API_KEY"] = "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"  # Replace with your new API key

    # Initialize OpenAI client securely
    client = openai.OpenAI()
    # Make a request
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Virtual Assistant named chatur, skilled in general tasks like Alexa and Google Assistant. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    # Print the assistant's response
    return completion.choices[0].message.content

# --------------------------------------------------------------------------------------------

    # # Store API key securely using environment variables
    # os.environ["GOOGLE_API_KEY"] = "AIzaSyALq0PF4TB6hDWIZOTc9TFptic4XVEGhFk"

    # # Configure Gemini API key
    # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # def aiProcess(command):
    #     """Send a command to the Gemini AI model and return the response."""
    #     model = genai.GenerativeModel("gemini-pro")  # Choose the appropriate model
    #     response = model.generate_content(command)
    #     return response.text

    # # Example usage
    # user_command = command
    # print(aiProcess(user_command))

# ----------------------------------------------------------------------------------------------------------------------

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com") 
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/?oai-dm=1")   
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/jaydhodi09")                
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicLibrary.music[song]    
        webbrowser.open(link) 
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=ef7c4b0a43234333bc3a90d04eb09c86") 
        if r.status_code == 200:
            data = r.json()  # Convert response to JSON
            articles = data.get("articles", [])  # Extract articles

            for i, article in enumerate(articles, 1):
                print(f"{i}. {article['title']}") 

    else:
        #let openai handle the request
        output=aiProcess(c)
        speak(output)                
       

if __name__=='__main__':
    speak("virtual assistant chatur is ready")
while True:
    #  listen Wake word for the jarvis
    # obtain auduio form microphone
    r=sr.Recognizer()
   

        #  recognize speach text`1`
    print("recognizzing ....")
    try:
        with sr.Microphone() as source:
            print("Listening ...z")
            audio=r.listen(source , timeout=2 , phrase_time_limit=1)  #2 para(timeout-ketli var sambdej) & ketla time  
        word=r.recognize_google(audio)
        if(word.lower()=="chatur"):
            speak("Yeh Jay say something?")

            #Listen for command
            with sr.Microphone() as source:
                print("chatur Active ...z")
                audio=r.listen(source)  #2 para(timeout-ketli var sambdej) & 
                command=r.recognize_google(audio)

                processCommand(command)

    
    except Exception as e:
        print("Error ; {0}".format(e))    