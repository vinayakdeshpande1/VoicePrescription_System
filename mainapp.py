# Import libraries
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox  
import prescription as pr
import speech_recognition as sr
import cv2
from PIL import Image,ImageTk
import pyttsx3
import os
import smtplib
import base64
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Initialize tkinter window, set height/width, 
window = Tk()
window.title("Dr. Voice")
window.iconbitmap("ICON vp.ico")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(),window.winfo_screenheight()))
window.resizable(1,1)

# # Instantiate pytsx3 engine
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# r=sr.Recognizer()

# opencv image
def cv():
    img = cv2.cvtColor(pr.templete, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(int(img.shape[1]*(window.winfo_screenheight()/float(img.shape[0]))),window.winfo_screenheight() - 50))
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image= img)
    image_frame.ImageTk = img
    image_frame.configure(image = img)
    showid = image_frame.after(10,show)

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Initiate pyttsx3 engine
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

r=sr.Recognizer()
   
# Frame to show prescription image
left_frame = Frame(window)
left_frame.grid()

image_frame = Label(left_frame)
image_frame.grid(row=0,column=0)

# Frame to show Add prescription buttons and text boxes
middle_frame = Frame(window,width =0.700,highlightcolor='black',highlightbackground='green',highlightthickness=1,height=window.winfo_screenheight()-50, padx=10,pady=10)

# Enter patient's name into input box
def name():
        with sr.Microphone() as source:
                t1,audio = "",""
                try:
                    r.adjust_for_ambient_noise(source,duration=2)
                    speak("patient\'s name")        
                    audio= r.listen(source)
                    t1 = r.recognize_google(audio)
                    print(t1,audio,source)
                    name_entry.insert(0,t1)
                    pr.name(name_entry.get())
                except:
                    print(t1,audio,source)
                    speak(' could not recognize ')

# Name label
name_label = Label(middle_frame,text="Name",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
name_label.grid(row=1,column=0)
name_entry = Entry(middle_frame,width=50)
name_entry.grid(row=1,column=1, padx=20,pady=10)

# Add Name Button
b = Button(middle_frame, text="Name",bg='lightgreen', command=name)
b.config( height = 1, width = 8, justify=RIGHT)
b.grid(row=1,column=5,)

# Enter patient's age into input box
def age():
        with sr.Microphone() as source:
                 
                try:
                        r.adjust_for_ambient_noise(source,duration=0.5)
                        speak("patient\'s age")
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        age_entry.insert(0,t1)
                        pr.age(age_entry.get())
                except Exception as e:
                        print(e)
                        speak(' could not recognize ')

# Age Label
age_label = Label(middle_frame,text="Age",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
age_label.grid(row=5,column=0)
age_entry = Entry(middle_frame,width=50)
age_entry.grid(row=5,column=1)

# Add Age Button
b1 = Button(middle_frame, text="Age",bg='lightgreen', command=age)
b1.config( height = 1, width = 8)
b1.grid(row=5,column=5)

# # Enter patient's gender into input box
def gender():
        with sr.Microphone() as source:
                try:
                        r.adjust_for_ambient_noise(source,duration=0.5)
                        speak("patient\'s gender")
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        if t1=='mail':
                            t1='male'
                        gen_entry.insert(0,t1)
                        pr.gender(gen_entry.get())
                except:
                        speak(' could not recognize ')

# Gender label
gen_label = Label(middle_frame,text="Gender",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
gen_label.grid(row=10,column=0)
gen_entry = Entry(middle_frame,width=50)
gen_entry.grid(row=10,column=1)

# Add Gender button
b2 = Button(middle_frame, text="Gender",bg='lightgreen', command=gender)
b2.config( height = 1, width = 8)
b2.grid(row=10,column=5)

# Enter patient's serial into input box
def serial():
        with sr.Microphone() as source:
                 
                try:
                        r.adjust_for_ambient_noise(source,duration=0.5)
                        speak("patient\'s serial nmber")
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        sl_entry.insert(0,t1)
                        pr.serial(sl_entry.get())
                except:
                        speak(' could not recognize ')

# Serial Label
sl_label = Label(middle_frame,text="Serial",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
sl_label.grid(row=15,column=0)
sl_entry = Entry(middle_frame,width=50)
sl_entry.grid(row=15,column=1)

# Add Serial button
b3= Button(middle_frame, text="serial",bg='lightgreen', command=serial)
b3.config( height = 1, width = 8)
b3.grid(row=15,column=5)


count=0
# Enter patient's medicines into input box
def medicines():
        global count
        with sr.Microphone() as source: 
                try:
                        count+=1
                        r.adjust_for_ambient_noise(source,duration=2)
                        speak("patient\'s medicines")
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        t1.remove('tablets')
                        t1=t1.split()
                        print(t1, audio)
                        md_entry.insert(0,t1[0])
                        pr.medicine(count,t1[0],t1[1],0,1)
                except:
                        speak(' could not recognize ')

# Medicine label
md_label = Label(middle_frame,text="Medicines",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
md_label.grid(row=20,column=0)
md_entry = Entry(middle_frame,width=50)
md_entry.grid(row=20,column=1)

# Add medicine button
b4= Button(middle_frame, text="Medicines",bg='lightgreen', command=medicines)
b4.config( height = 1, width = 8)
b4.grid(row=20,column=5)

# Enter patient's symptoms into input box
def symptoms():
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source,duration=2)
            speak("patient\'s symptoms")
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            sm_entry.insert(0,t1)
            pr.symptoms(sm_entry.get())
        except:
            speak(' could not recognize ')

# Symptoms label
sm_label = Label(middle_frame,text="Symptoms",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
sm_label.grid(row=30,column=0)
sm_entry = Entry(middle_frame,width=50)
sm_entry.grid(row=30,column=1)

# Add symptoms button
b5 = Button(middle_frame, text="Symptoms",bg='lightgreen', command=symptoms)
b5.config( height = 1, width = 8)
b5.grid(row=30,column=5)

# Enter patient's Diagnosis into input box
def diag():
    with sr.Microphone() as source:     
        try:
            r.adjust_for_ambient_noise(source,duration=0.5)
            speak(" diagnosis ")
            audio= r.listen(source)
            t1 = r.recognize_google(audio)
            dia_entry.insert(0,t1)
            pr.diagnosis(dia_entry.get())
        except:
            speak(' could not recognize ')

# Add diagnosis label
dia_label = Label(middle_frame,text="Diagnosis",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
dia_label.grid(row=35,column=0)
dia_entry = Entry(middle_frame,width=50)
dia_entry.grid(row=35,column=1)

# Add diagnosis button
b6 = Button(middle_frame, text="Diagnosis",bg='lightgreen', command=diag)
b6.config( height = 1, width = 8)
b6.grid(row=35,column=5)


# Enter patient's advice into input box
def advice():
    with sr.Microphone() as source:  
        speak("advice for patient")
        try:
            r.adjust_for_ambient_noise(source,duration=0.5)
            audio = r.listen(source)
            t1 = r.recognize_google(audio)
            ad_entry.insert(0,t1)
            pr.advice(ad_entry.get())
        except:
            speak(' could not recognize ')

# Add advice label
ad_label = Label(middle_frame,text="Advice",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
ad_label.grid(row=40,column=0)

ad_entry = Entry(middle_frame,width=50)
ad_entry.grid(row=40,column=1)

# Add Advice button
b7 = Button(middle_frame, text="Advice",bg='lightgreen', command=advice)
b7.config( height = 1, width = 8)
b7.grid(row=40,column=5)

# Signature Label
sig_label = Label(middle_frame,text="Signature",font=("Poor Richard",15), width=8, justify=LEFT, anchor="w")
sig_label.grid(row=45,column=0)
sig_entry = Entry(middle_frame,width=50)
sig_entry.grid(row=45,column=1)

# Function to save the input data into a file
def save():
    pr.save()
    messagebox.showinfo("Information: ","Saved at location: " + os.getcwd())

# Button to save the data
b8 = Button(middle_frame, text="Save",bg='lightgreen', command=save, font=("Poor Richard",18))
b8.config( height = 1, width = 20)
b8.grid(row=50,column=1)

middle_frame.grid(row=0,column=2,stick=E)

right_frame = Frame(window, width =0.700,highlightcolor='black',highlightbackground='green',highlightthickness=1,height=window.winfo_screenheight()-50, padx=10,pady=10)
e = Label(right_frame,text="Your mail id: ",font=("Poor Richard",15), width=18, justify=LEFT, anchor="w")
e.grid(row=1,column=0)
e_entry = Entry(right_frame,width=50) 
e_entry.grid(row=1,column=1)

f= Label(right_frame,text="Enter your password: ",font=("Poor Richard",15), width=18, justify=LEFT, anchor="w")
f.grid(row=6,column=0)
f_entry = Entry(right_frame,width=50)
f_entry.config(show='*')
f_entry.grid(row=6,column=1)
g= Label(right_frame,text="Receipient's Email id: ",font=("Poor Richard",15), width=18, justify=LEFT, anchor="w")
g.grid(row=11,column=0)
g_entry = Entry(right_frame,width=50)
g_entry.grid(row=11,column=1)
right_frame.grid(row=0,column=2,sticky=N)


# Function to attach file to email
def attachments():
    file_path = filedialog.askopenfilename()
    return file_path
	
# Function to send email
def send():
    try:
        msg = MIMEMultipart()
        filename=attachments()
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",)
        msg.attach(part)
        text = msg.as_string()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(e_entry.get(),f_entry.get())
        server.sendmail(e_entry.get(),g_entry.get(),text)
        server.close()
        messagebox.showinfo("information","< MAIL SENT >") 
    except:
        messagebox.showwarning("warning: ","Mail NOT sent. Try again")  
# Button to share email
b9 = Button(right_frame, text="Share",bg='magenta', command=send, font=("Poor Richard",18))
b9.config( height = 1, width = 20)
b9.grid(row=20,column=1)

# Show the data onto the prescription image
def show():
    pr.name(name_entry.get())
    pr.age(age_entry.get())
    pr.gender(gen_entry.get())
    pr.serial(sl_entry.get())
    pr.medicine(0,md_entry.get(),'',0,1)
    pr.symptoms(sm_entry.get())
    pr.diagnosis(dia_entry.get())
    pr.advice(ad_entry.get())
    pr.signature(sig_entry.get())
    cv()
show()

# About the app
def about():
    messagebox.showinfo('Voice Prescription System')

# How to use the app
def guide():
    messagebox.showinfo('USER MANUAL',
        '1.click on the button that u want to fill the field.\n'
                        'eg: name,age,advice,etc...\n'
                        '2.click on save button after completion of writing prescription.\n'
                        '3.enter mail and click on send button to select file and send.')

# Destroy tkinter instance
def destroy():
    window.destroy()
    

menubar = Menu(window)
window.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About", command=about)
subMenu.add_command(label="guide", command=guide)

subMenu.add_separator()
subMenu.add_command(label="Exit", command=destroy)

window.mainloop()
