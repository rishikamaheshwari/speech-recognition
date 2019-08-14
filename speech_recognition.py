import speech_recognition as sr
from time import ctime
#record audio
#def rec():
r=sr.Recognizer()  #test microphone is workimg or not
with sr.Microphone() as source:
    print("say something")
    audio=r.listen(source)  #2modes sync and async and r.listen works in async mode
        #return audio
data=""
#def spr():
try:
    data=r.recognize_google(audio) #command for google search engine
    print("you said:" +data)
    #return data
except sr.UnknownValueError:  #there is no data in audio
    print("Google search recognition could not understand audio")
except sr.RequestErrror as e:   #when there is no internet
    print("could not request results from google speech recognition")
        
'''def dec(d):
    if (d=="hello"):
        print('hi')
        return 1
    elif(d=="how are you"):
        print('i am fine')
        return 1
    elif(d=="thank you"):
        print('it was nice to talk to you')
        return 0
    elif(d=="what time is it"):
        print(ctime())
        return 1
    else:
        print('good')
        return 1
q=1
while(q):
    a=rec()
    b=spr(a)
    q=dec(b)'''
    
