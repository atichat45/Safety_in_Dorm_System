import cv2, sys, numpy, os
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'     #This folder include the name of People Datasets
sub_data = 'New Person'   #This will create folders in datasets with the face of people, so change it's name to your name after run this program.

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)    # defining the size of images 

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0) #'0' is use for your webcam, if you've any other camera use another number

print("Please move your face left and right until the programe is complete.")
# The program loops until it has 60 images of your face.
count = 1
while True: 
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
        print("Picture %d and Remain %d" %(count,60 - count))
        count += 1
    if count == 61:
        break
    
    cv2.imshow('Add person to Safety in Dorm System', im)
    key = cv2.waitKey(150)
    if key == 27:
        break
