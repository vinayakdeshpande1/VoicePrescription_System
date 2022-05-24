# Import Libraries
import cv2
import os
from datetime import date
from PIL import Image

# Get today's date
today = date.today().strftime("%d/%m/%Y")

# Color Codes in (B,G,R)
black = (1,1,1)
white = (255,255,255)
red = (20, 20, 255)

# Global Variables used during program execution
global addname,addage,addgender,addserial,addsignature,addsymptom,adddiagnosis,addadvice,templete,quantity,medname,af_bf,tim,medpos,qtypos,af_bfpos,timpos
addname = ""
addage = ""
addgender= ""
addserial = ""
addsignature = ""
addsymptom = ""
adddiagnosis = ""
addadvice = ""
templete = ""
medname = []
quantity = []
af_bf = []
tim = []
medpos =[]
qtypos =[]
af_bfpos = []
timpos = []

# Insert Medicines one by one
for i in range(20):
    num = 500 + ((i-1) * 20)
    medpos.append((60,num)) 
    qtypos.append((350,num)) 
    af_bfpos.append((430,num)) 
    timpos.append((500,num))  
    medname.append("")
    quantity.append("")
    af_bf.append("")
    tim.append("")

# Fill the text in the template
def generate():
    global addname,addage,addgender,addserial,addsignature,addsymptom,adddiagnosis,addadvice,templete,quantity,medname,af_bf,tim,medpos,qtypos,af_bfpos,timpos
    templete = cv2.imread(os.getcwd() + '/prescription.png' )
    write(str(addname),(112,158), red, 0.6)
    write(str(addage),(105, 194),red,size=0.45)
    write(str(addgender),(318, 193),red)
    write(str(addserial),(316, 228),red,size=0.45)
    write(str(addsignature),(211,871),red)
    write(str(addsymptom),(149, 299),red)
    write(str(adddiagnosis),(145, 335),red)
    write(str(addadvice),(145, 371),red)
    write(str(today),(105, 228),red,size=0.45)

    for j in range(20):
        write(str(medname[j]),medpos[j] )
        write(str(quantity[j]),qtypos[j],size=0.45)
        write(str(af_bf[j]),af_bfpos[j] )
        write(str(tim[j]),timpos[j])
        j = j+1
        
# Function to write text on the image provided text and text-position and size of the text
def write(text,origin, color=black,size=0.6):
    global templete
    cv2.putText(templete, text , origin ,  cv2.FONT_HERSHEY_DUPLEX, size, color , 1, cv2.LINE_AA)

# Modify global name
def name(x):
    global addname
    addname = x
    generate()

# Modify global age
def age(x):
    global addage
    addage = x
    generate()

# Modify global gender
def gender(x):
    global addgender
    addgender = x
    generate()

# Modify global serial
def serial(x):
    global addserial
    addserial = x

# Modify global medicine
def medicine(number,med,qty=1,ab=0,t=1):
    global medname,quantity,af_bf,tim
    if(number < 20):
        
        if(ab == 0):
            food = "BF"
        else:
            food = "AF"
        
        if(t == 1):
            time = ""
        elif(t == 2):
            time = ""
        elif(t == 3):
            time = ""
        elif(t == 4):
            time = ""

        del medname[number]
        medname.insert(number,med) 

        del quantity[number]
        quantity.insert(number,qty)

        del af_bf[number]
        af_bf.insert(number,food)

        del tim[number]
        tim.insert(number,time)
        
# Modify global signature
def signature(x):
    global addsignature
    addsignature = x
    generate()

# Modify global symptoms
def symptoms(x):
    global addsymptom
    addsymptom = x
    generate()

# Modify global diagnosis
def diagnosis(x):
    global adddiagnosis
    adddiagnosis = x
    generate()

# Modify global advice
def advice(x):
    global addadvice
    addadvice = x
    generate()

# Save the Prescription as PDF
def save():
    global addserial, addname, addage, addgender, addsignature, addsymptom, adddiagnosis, addadvice, templete
    path = "/".join(os.getcwd().split("\\")) + '/prescriptions/'
    im_pil = Image.fromarray(cv2.cvtColor(templete,cv2.COLOR_BGR2RGB))
    im_pil.save(path + "_" + str(addname) + "_" + str(addserial) + ".pdf","PDF",resolution = 100)



