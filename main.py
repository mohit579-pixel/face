import face_recognition
import cv2
import numpy as np
import csv
import os
import smtplib
from datetime import datetime
from twilio.rest import Client
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pickle

#for returning the names from Excel file
def loaddata(filenane):
	mylist = []
	with open(filenane) as numbers:
		numbers_data = csv.reader (numbers,delimiter=',')
		next (numbers_data)
		for row in numbers_data:
			mylist.append (row[0])
		return mylist                      

    
    
#This functions retrives the encodings from another python file    
files=open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(files)
files.close()
known_face_encoding, known_faces_names = encodeListKnownWithIds

print("Encode File Loaded")    
def main():                           
	video_capture = cv2.VideoCapture(0)
	 
	students = known_faces_names.copy()
	 
	face_locations = []
	face_encodings = []
	face_names = []
	s=True
	 
	 
	now = datetime.now()
	current_date = 'attendance'
	 
	 
	 
	f = open(current_date+'.xlsx','a+',newline = '')
	lnwriter = csv.writer(f)
	 
	while True:
	    _,frame = video_capture.read()
	    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
	    rgb_small_frame = small_frame[:,:,::-1]
	    if s:
	        face_locations = face_recognition.face_locations(rgb_small_frame)
	        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
	        face_names = []
	        for face_encoding in face_encodings:
	            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
	            name=""
	            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
	            best_match_index = np.argmin(face_distance)
	            if matches[best_match_index]:
	                name = known_faces_names[best_match_index]
	 
	            face_names.append(name)
	            if name in known_faces_names:
	                font = cv2.FONT_HERSHEY_SIMPLEX
	                bottomLeftCornerOfText = (10,100)
	                fontScale              = 1.5
	                fontColor              = (255,0,0)
	                thickness              = 3
	                lineType               = 2
	 
	                cv2.putText(frame,name+' Present', 
	                    bottomLeftCornerOfText, 
	                    font, 
	                    fontScale,
	                    fontColor,
	                    thickness,
	                    lineType)
	 
	                if name in students:
	                    students.remove(name)
	                    print(students)
	                    current_time = now.strftime("%H-%M-%S")
	                    lnwriter.writerow([name,current_time])
	    cv2.imshow("Attendence System",frame)
	    if cv2.waitKey(1) == ord('q'):
	        break
	 
	video_capture.release()
	cv2.destroyAllWindows()
	f.close()
	
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login('mohitkahandelwal@gmail.com ','moycpqdpunhqzmfs')
	
	
	SID = 'ACdff99c49859cbd2fa771379933c5b996'
	AUTH_TOKEN = '963081bf9569f4d75e5a4ced89153d23'
	cl = Client(SID, AUTH_TOKEN)
	
	
	
	
	new_list=loaddata('attendance.xlsx')
	for row in new_list:
	    if (row=='mohit'):
	        server.sendmail('mohitkahandelwal@gmail.com ','mohitkhandelwal290@gmail.com ','Dear parent, Your child Mohit Khandelwal has Entered the colledge primicies')
	        print('mail send')
	        cl.messages.create(body='Dear parent, Your child Mohit Khandelwal has Entered the colledge primicies'+'mohit', from_='+16206588807', to='+919423408300')
	        
	    if (row=='Richa'):
	        server.sendmail('mohitkahandelwal@gmail.com ','richagaikwad2020@gmail.com ','Dear parent, Your child Richa Gailward has Entered the colledge primicies')
	        print('mail send')
	        cl.messages.create(body='Dear parent, Your child Richa Gailward has Entered the colledge primicies', from_='+16206588807', to='+919763436098')
	        
	    if (row=='varsha'):
	        server.sendmail('mohitkahandelwal@gmail.com ','varshagarje2003@gmail.com ','Dear parent, Your child Varsha Garge has Entered the colledge primicies')
	        print('mail send')
	        cl.messages.create(body='Dear parent, Your child Varsha Garge has Entered the colledge primicies', from_='+16206588807', to='+919370363146')
	        
	    if (row=='Pruthevesh'):
	        server.sendmail('mohitkahandelwal@gmail.com ','pruthveshbaitule@gmail.com ','Dear parent, Your child Pruthvesh Baitule has Entered the colledge primicies')
	        print('mail send')
	        cl.messages.create(body='Dear parent, Your child Pruthvesh Baitule has Entered the colledge primicies', from_='+16206588807', to='+919890818559')
	        
 
    
    
    
    

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == '12' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful---------------------------!!')
        messagebox.showinfo('Yayyy','Wait for few seconds......')
        main()
        
        
    else:
        messagebox.showerror('Error','Login Failed')


root = Tk()

root.title('Login Form')

root.geometry('350x500')

root.configure(background='#0096DC')



text_label = Label(root,text='DPU',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))


email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))



root.mainloop()


