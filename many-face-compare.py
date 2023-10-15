#you have to create three folders, criminals,securitycam, and results
#put one pic in criminals and many pics in securitycam folder to compare to.
#results will show up in the folder results with square on the faces.
import face_recognition
import os
from PIL import Image, ImageDraw
import numpy as np
import random

def load(filename):
    img = face_recognition.load_image_file(filename)
    face_locations = face_recognition.face_locations(img)
    return face_recognition.face_encodings(img, face_locations), face_locations

criminal_img = "criminals/biden.jpg"
criminal_cam_encoding, _ = load(criminal_img)
criminal_cam_encoding = criminal_cam_encoding[0]  # Assuming there is one face or the first face is our target

my_dir = 'securitycam/' # Folder where all your image files reside. Ensure it ends with '/
security_img=[]
for i in os.listdir(my_dir): # Loop over the folder to list individual files
    x=0
    image = my_dir + i
    security_img.append(i)
    #print (i)
    print(image)
    security_cam_encoding, security_face_locations = load(image)  # Remember this is a list of face encodings

    result = face_recognition.compare_faces(security_cam_encoding, criminal_cam_encoding)

    # We are now going to draw rectangle around our target, if they are found
    # First we need to found which face in our security photo matched with how
    # criminal.

    flag = False
    for i in range(0, len(result)):
        found = result[i]

        if found:
            image = Image.open(image)
            draw = ImageDraw.Draw(image)
            z=0
            (top, right, bottom, left) = security_face_locations[i]

            # Draw the rectangle
            draw.rectangle([(left, top), (right, bottom)], outline=(255, 0, 0), width=5)

            # Save the modified image
            print ("i= ",i)
            outfile= "results/out"+str(random.random())+".jpg"
            z+=1
            image.save(outfile)
            flag = True
            break

    if flag:
        print("Found the inmate.")
    else:
        print("Could not find the inmate")


    x+=1
print (image)
#print (security_cam_encoding[0])

#security_img = "securitycam/security4.jpg"



