from tkinter import *
import speech_recognition as sr


root = Tk()
root.title('WakeUp')
root.geometry("400x400")


global searchFor
searchFor = Entry(root, width=50)
searchFor.pack()


def startRecongition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            weSearchFor = searchFor.get()
            text = r.recognize_google(audio)
            # print("weSearchFor : " + weSearchFor)
            # print("text : " + text)
            if weSearchFor == text:
                wakeUp = Label(root, text="ALERT ::: The Word " +
                               searchFor.get() + " has been said", width=50)
                wakeUp.pack()
            else:
                speechToText = Label(root, text="{}".format(text), width=50)
                speechToText.pack()
        except:
            problem = Label(
                root, text="There was a problem recognizing what you have just said", width=50)
            problem.pack()
            problemAction = Label(
                root, text="please start and repeat it again", width=50)
            problemAction.pack()


def stopRecongition():
    problem = Label(root, text="Stop Listening", width=50)
    problem.pack()


startButton = Button(root, text="Start", padx=20, pady=5,
                     command=startRecongition, fg="white", bg="green")
startButton.pack()


stopButton = Button(root, text="Stop", padx=20, pady=5,
                    command=stopRecongition, fg="white", bg="red")
stopButton.pack()


root.mainloop()
