from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
import cvlib as cv
                    
# load model
model = load_model('model.h5')

# open webcam
webcam = cv2.VideoCapture(0)

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    # apply face detection
    face, confidence = cv.detect_face(frame)

    #arrays to hold the values
    age_ = []
    gender_ = []

    # loop through detected faces
    for idx, f in enumerate(face):

        # get corner points of face rectangle        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # draw rectangle over face
        cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 4)

        # crop the detected face region
        face_crop = np.copy(frame[startY:endY,startX:endX])

        if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
            continue

        # preprocessing for gender detection model
        face_crop = cv2.resize(face_crop, (200,200))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)

        # apply gender and age detection on face
        predict = model.predict(np.array(face_crop).reshape(-1,200,200,3))
        age_.append(predict[0])
        gender_.append(np.argmax(predict[1]))
        gend = np.argmax(predict[1])
        if gend == 0:
            gend = 'Man'
            col = (255,0,0)
        else:
            gend = 'Woman'
            col = (203,12,255)
        
        #labels
        label =  "Age : " + str(int(predict[0])) + " / " + str(gend)

        # write label and confidence above face rectangle
        cv2.putText(frame, label, (startX, StartY),  cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, col, 4)

    # display output
    cv2.imshow("age and gender detection", frame)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()