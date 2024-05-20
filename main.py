                                                      ##AI MODEL###
import speech_recognition as sr
import os
import openai
from config import apikey
import pyttsx3
import webbrowser
import datetime

##define globaL CHAT##
chatStr = ""

##CHATTING FUNCTION##
def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Priyanshu: {query}\n Nexus: "
    response = openai.Completion.create(
         model="gpt-3.5-turbo-instruct",
         prompt=chatStr,
         temperature=0.7,
         max_tokens=256,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0
     )
    # todo: Wrap this inside of a try catch block
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

## TASK FUNCTION##
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",     #"davinci-002",#
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    # todo: Wrap this inside of a  try catch block

    #print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

##USING SYSTEM VOICE##
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# day of the week#
def day():
    now = datetime.datetime.now()
    day_of_week_name = now.strftime("%A")
    speak("Today is " + day_of_week_name)

##WISG=HING THE USER ##
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

## SPEAKING FUBCTION##
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

## FROM THIS FUNCTION LWO WILL TAKE USER INPUTS##
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Trying to Recognize....")
            query = r.recognize_google(audio, language="en-in")
            print("You said: " + query)
            return query
        except Exception as e:
            return "I could not understand Sorry from Nexus"

## MAIN ##
if __name__ == '__main__':
    print('Welcome to Nexus A.I')
    wishMe()
    speak("THIS SIDE athena ")
    #speak("I am glad to be here for you")
    speak("WHAT CAN I DO FOR YOU  SIR")

    while True:
        print("listening Voices.....")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:

           if f"Open {site[0]}".lower() in query.lower():
               speak(f"Opening {site[0]} sir...")
               webbrowser.open(site[1])

         # todo: Add a feature to play a specific song

        musics = [["despacito","C:/Users/rajak/Downloads/Despacito(PagalWorld).mp3"],["hereeiye","C:/Users/rajak/Downloads/_Heeriye(PagalWorld.com.cm).mp3"],["phele bhi main","C:/Users/rajak/Downloads/Pehle Bhi Main(PagalWorld.com.cm).mp3"]]
        for music in musics:
            if f"play {music[0]}".lower() in query.lower():
                speak(f"Playing {music[0]} sir...")
                os.startfile(music[1])

            if "which day is today" .lower() in query.lower():
                day()


            if "THE TIME" in query:
               hour = datetime.datetime.now().strftime("%H")
               min = datetime.datetime.now().strftime("%M")
               seconds = datetime.datetime.now().strftime("%S")
               speak(f"Sir time is {hour} hours {min}  minutes {seconds} seconds")

            elif "OPEN CAMERA".lower() in query.lower():
               filePath = "C:/Program Files/WindowsApps/Microsoft.WindowsCamera_2023.2312.3.0_x64__8wekyb3d8bbwe/WindowsCamera.exe"
               speak("Opening Camera")
               os.startfile(filePath)

            elif "OPEN VS CODE".lower() in query.lower():
               filePath = "C:/Users/rajak/AppData/Local/Programs/Microsoft VS Code/Code.exe"
               speak("Opening VS code")
               os.startfile(filePath)

            elif "USING ARTIFICIAL INTELLIGENCE".lower() in query.lower():
               ai(prompt=query)
               speak(f"Writing your Command")

            elif "QUIT Nexus".lower() in query.lower():
               speak("Quitting sir..")
               speak("just call me whenever you need me sir")
               speak("I am always there for you ")
               exit()

            elif "RESET THE CHAT".lower() in query.lower():
               speak(" OK SIR Resetting the chat")
               chatStr = ""

            else:
               print("Chatting...")
               chat(query)

