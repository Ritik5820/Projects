import pyttsx3 #A library in module which converts text to speech.
import datetime #A module which shows date and time.
import speech_recognition as sr #A module which recognizes the speech.
import wikipedia #A module for wikipedia to do wikipedia searches.
import webbrowser #A module to open webBrowser.
import os #A module to use os functions.
import time #For time.sleep
import pyautogui #for opening hotkeys
import pywhatkit #for google search

engine = pyttsx3.init('sapi5') #sapi5 is the api which allows the use of voice recognition. Here we are selecting engine sapi5.

voices = engine.getProperty('voices') #voice is object here.
# print(voices[0].id) #checking how many voice we have. 
engine.setProperty('voice', voices[0].id) #setting the voice of a male. 

def speak(text): #Creating a Function to speak. And given the parameter audio.
    engine.say(text) #will convert whatever the text inside the parameter audio.
    engine.runAndWait() #is used to run the command and wait to listen. compulsory to write with engine.say


def startUp():
    speak("Initializing Jarvis")
    time.sleep(1)
    speak("Starting all systems applications")
    time.sleep(1)
    speak("Installing and checking all drivers")
    time.sleep(1)
    speak("Caliberating and examining all the core processors")
    time.sleep(1)
    speak("Checking the internet connection")
    time.sleep(1)
    speak("Wait a moment sir")
    time.sleep(1)
    speak("All drivers are up and running")
    time.sleep(1)
    speak("All systems have been activated")
    time.sleep(1)
    speak("Coming Online in 5, 4, 3, 2, 1!")
    speak("Now I am online")

def wishMe():
    hour = int(datetime.datetime.now().hour) #converting date and time into int to compare it with int.
    
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis. Please tell me how may I help you?")

def takeCommands(): #takes microphone input from user and return string output.
    r = sr.Recognizer() #created an object of class recognizer. Main function is to recognize the speech.
    with sr.Microphone() as source: #using this microphone as source.
        print("Listning...")
        r.adjust_for_ambient_noise(source) #will automatically adjust according to background noice. W/o this, it will keep listning 
        r.pause_threshold = 1 #seconds of non speaking audio.
        audio = r.listen(source) #will listen anything given from microphone.

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN') # recognizing the voice and Using google for voice recognition.
        print(f"User said: {query}\n") 
    
    except Exception as e:
        #print(e) #will print the error but we dont need it.
        speak("Sorry Sir I did not get that. Can you say that again please?") #in case of improper voice this will be printed
        return "None"
    return query

if __name__== "__main__":
    startUp()
    wishMe()
    while True:
        query = takeCommands().lower() #converting query into lower case. and it will keep listning in loop.

        #Logic for excuting tasks based on query.

        #FOR WIKIPEDIA:-
        if 'according to wikipedia' in query:
            speak("Searching Wikipedia Sir...")
            query = query.replace('according to wikipedia',"")
            query = query.replace("who is","")
            query = query.replace("what is","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        #FOR ANY WEBSITE:-
        elif 'open a website' in query:
            speak("Which website you want me to open sir?")
            result = takeCommands()
            
            chromePath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open_new_tab(result + ".com")
            speak("Here you go!")
        
        #TO OPEN FILES:-
        elif 'open chrome' in query:
            speak("Opening Chrome sir...")
            chromePath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            os.startfile(chromePath)
            speak("Here you go!")

        elif 'open code' in query:
            speak('Opening code sir...')
            codePath = r"C:\Users\kohad\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            speak("Here you go!")

        elif 'open excel' in query:
            speak("Opening Excel sir...")
            excelPath = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(excelPath)
            speak("Here you go!")

        elif 'open workbench' in query:
            speak('Opening workbench sir...')
            workBenchPath = r"C:\Program Files\MySQL\MySQL Workbench 8.0\MySQLWorkbench.exe"
            os.startfile(workBenchPath)
            speak("Here you go!")

        elif 'open notepad' in query:
            speak('Opening Notepad sir...')
            notePadPath = r"C:\Windows\system32\notepad.exe"
            os.startfile(notePadPath)
            speak("Here you go!")

        elif 'open disk cleanup' in query:
            speak("Opening Disk Cleanup sir...")
            DiskCleanUpPath = r"C:\Windows\system32\cleanmgr.exe"
            os.startfile(DiskCleanUpPath)
            speak("Here you go!")

        elif 'open paint' in query:
            speak("Opening Paint Sir...")
            paintPath = r"C:\Windows\system32\mspaint.exe"
            os.startfile(paintPath)
            speak("Here you go!")
        
        #TO OPEN HOTKEY FILES:-
        elif 'hidden menu' in query:
            speak("Opening hidden menu sir...")
            pyautogui.hotkey('winleft','x')
            speak("Here you go!")

        elif 'open task manager' in query:
            speak("Opening Task Manager sir...")
            pyautogui.hotkey("ctrl","shift","esc")
            speak("Here you go!")

        elif 'open task view' in query:
            speak("Opening Task View sir...")
            pyautogui.hotkey('winleft','tab')
            speak("Here you go!")
            
        elif 'close this application' in query:
            speak("Closing current application sir...")
            pyautogui.hotkey("alt","f4")
            speak("Application Closed!")
            
        #TO ASK TIME AND DATE:-
        timeStrList = ["the time",'time is it','time it is']
        for items in timeStrList:
            if items in query:
        
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strtime)
                speak(f"The time is {strtime}")
        
        datestrList = ['the date','date is it','date it is']
        for items in datestrList:
            if items in query:
                strdate = datetime.date.today()
                print(strdate)
                speak(f"The date is {strdate}")

        #SHUTDOWN/RESTART/LOGOUT:-   
        shutdownStrList = ['shutdown the computer','shutdown the pc','shutdown computer','shutdown pc']
        for items in shutdownStrList:
            if items in query:
                speak("Shutting Down in 5, 4, 3, 2, 1...")
                speak("Good bye sir!")
                os.system("shutdown /s /t 1")
        
        restartStrList = ['restart the computer','restart the pc','restart computer','restart pc']
        for items in restartStrList:
            if items in query:
                speak("Restarting in 5, 4, 3, 2, 1...")
                speak("See you in a bit sir!")
                os.system("shutdown /r /t 1")
        
        logoutStrList = ['logout the computer','logout the pc','logout computer','logout pc']
        for items in logoutStrList:
            if items in query:
                speak("Logging Out in 5, 4, 3, 2, 1...")
                speak("See you in a bit sir!")
                os.system("shutdown l")

        #FOR GOOGLE SEARCH: 
        googleSearchList = ["search on google","search something on google","search another thing","search another thing on google","search something else"]
        for items in googleSearchList:
            if items in query:
                import wikipedia as googleScrap
                speak("What do you want to search sir?")
                search = takeCommands()
                search = search.replace("search","")
                pywhatkit.search(search)

                try: 
                    result = googleScrap.summary(search,3)
                    speak("This is what i have found on google sir!")
                    print(result)
                    speak(result)

                except:
                    speak("No speakable data available sir!")

        

        # #GENERAL LINES:-

        # elif 'good night' in query:
        #     speak('Sleep well sir.')

        # elif 'thank you' in query: 
        #     speak('Your Welcome sir')

        # elif "bye" in query:
        #     speak("See you sir.")

        # elif "wake up jarvis" in query:
        #     speak("Online and Ready Sir!") 