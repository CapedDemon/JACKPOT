#Author :- Shreejan Doali
#Publishd on 30-10-2021
#Language :- python

#libraries needed
import urllib.request
import random
import speech_recognition as sr
import pyttsx3
import time

#link of the website where 10000 words are there
url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(url)#Here I have used the urllib library and I have first opened the link using urlopen() function
words_list = response.read().decode()
game_words = words_list.splitlines()#I have just then used the splitlines fucntion to change the decoded word list into a list

#To make this game more interesting I have included voice in it.
machine = pyttsx3.init('sapi5')#I have used pyttsx3 and taken the voice of sapi5
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)

#This is the function to speak the line which I will give.
def speak(audio):
    machine.say(audio)
    machine.runAndWait()

#This is the function to take voice input from the user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")#When it will take the response it will be printing listening....
        audio = r.listen(source)

    #I have set try and except exception so that if the user tells something it will take it or if the user doesn't says anything it will throw an exception
    try:
        print("Recognizing....")
        text = r.recognize_google(audio, language='en-in')

    except Exception:
        return "Nothing Said!"
    return text


#This is the test function. It will take the number of words as i, main list to be spoken as list_words, and the reverse list as reverse_list
def test(i, list_words = [], reverse_list = []):
    
    speak("The words which I will tell you need to tell it in the reverse order. If anyone is wrong I will say wrong and you lose the test. If it is correct then I will say correct then only you will say the next word.")
    
    speak("Your test will start in 5, 4, 3, 2, 1. Now")
    time.sleep(1)

    speak("The words are :- ")
    time.sleep(1)

    #A for loop from 0 to i. I could have directly used speak(list_words)
    #But I have used the for loop so that I can include the time.sleep(1) for ease
    for j in range(0, i):
        speak(list_words[j])
        time.sleep(1)
    
    #making a variable decison to guess whether user have said all the things corretly or not. 
    #Initial value is 0
    decision = 0

    #Starting a for loop from 0 to i so that 
    # it will be easy to guess whether user have said correct or wrong.
    #Telling a wrong wod will lead the test to end
    for h in range(0, i):
        said_words = takecommand()#Used the takecommand function

        if(said_words != reverse_list[h]):
            decision = 0
            speak("Wrong.")
            print(said_words)
            break

        elif(said_words == reverse_list[h]):
            speak("Correct.")
            decision = 1
            print(said_words)
            continue

    if(decision == 1):
        speak("Yay! You speak all the words correctly. You won the easy level.")

    
    elif(decision == 0):
        speak("You lose the test!!")


#From here the main code begins
if __name__ == "__main__":
    
    print("Welcome to Memory Game Challenge\nIn this game some words will be told to you and you have to repeat the words in the reverse manner in 10 second.\n")
    
    print("Choose level:- \nFor easy press E and select enter\nFor Intermidiate level press I and select enter\nFor impossible level press H an select enter\n")
    level = input()

    #Easy Level
    if(level == 'E'):
        #As it is easy level I have given 5 words to say
        speak("In this level you will be given 5 words total")
        list_words1 = []#This is the word list which the computer will speak
        reverse_list1 = []#This is the reverse list which the user need to speak
        #appending in the main list
        for i in range(0, 5):
            n = random.randint(0, 10000)#Generatng random numbers between 1 to 10000
            list_words1.append(game_words[n])#then appending the items  of the list which I have taken from the internet at the index of the random number generated
        
        #appending the items of the list_words in the reverse manner in the reverse_list
        k = 4
        for j in range(0, 5):
            reverse_list1.append(list_words1[k])
            k = k - 1
        
        test(5, list_words1, reverse_list1)#Giving the arguements to the test function


    #IntermediATE level
    #Same as above
    elif(level == 'I'):
        #As it is intermediate level I have given 10 words to say
        speak("In this level you will be given 10 words total")
        list_words2 = []
        reverse_list2 = []

        for i in range(0, 10):
            n = random.randint(0, 10000)
            list_words2.append(game_words[n])

        k = 9                                       
        for j in range(0, 10):
            reverse_list2.append(list_words2[k])
            k = k - 1

        test(10, list_words2, reverse_list2)

    #Impossible level 
    #Same as above two
    elif(level == 'H'):
        #As it is impossible level I have given 15 words to say
        speak("In this level you will be given 15 words total")
        list_words3 = []
        reverse_list3 = []
        for i in range(0, 15):
            n = random.randint(0, 10000)
            list_words3.append(game_words[n])

        k = 14
        for j in range(0, 15):
            reverse_list3.append(list_words3[k])
            k = k - 1

        test(15, list_words3, reverse_list3)

    else:
        print("Enter the correct input\n")

    print("Press anything to exit")
    a= input()