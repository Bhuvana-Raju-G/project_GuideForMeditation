import pyttsx3

def speakout(words):
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()
 
def rest():
    engine = pyttsx3.init()
    engine.say("rest for few seconds")
    engine.runAndWait()
    
def counter(n):
    for i in range(int(n)):
        speakout(i)