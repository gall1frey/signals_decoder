import keras
from keras import models
from keras.models import load_model
#pip install opencv-python
import cv2
import numpy as np
import tensorflow as tf

# def prepare(model_path):
import pickle 
import pickle_compat

model_path = keras.models.load_model(r"C:\Users\Sanjna\Desktop\5th sem\mini project\review 2\model.h5")

with open(r"C:\Users\Sanjna\Desktop\5th sem\mini project\review 2\input signals to be classified\psk8.pkl","rb") as f:
    data = f.read()
d = pickle.loads(data)

e =(model_path.variables)
# signals = pk.loads(open(r"C:\Users\Sanjna\Desktop\5th sem\mini project\review 2\input signals to be classified\psk8.pkl",'r'))
pickle_compat.patch()
op=pickle.load(open(r"C:\Users\Sanjna\Desktop\5th sem\mini project\RML2016.10a_dict.pkl","rb"))
#print(op.keys())
# # prediction = model_path.()
# # print(prediction)
#predictions = new_model.predict_classes([X_test])

# predict_x=model.predict(X_test) 
# classes_x=np.argmax(predict_x,axis=1)

classes = ['32PSK',
 '16APSK',
 '32QAM',
 'FM',
 'GMSK',
 '32APSK',
 'OQPSK',
 '8ASK',
 'BPSK',
 '8PSK',
 'AM-SSB-SC',
 '4ASK',
 '16PSK',
 '64APSK',
 '128QAM',
 '128APSK',
 'AM-DSB-SC',
 'AM-SSB-WC',
 '64QAM',
 'QPSK',
 '256QAM',
 'AM-DSB-WC',
 'OOK',
 '16QAM']


abc = model_path.predict(op[('QPSK', 2)])
defe = np.argmax(abc,axis=1)
for i in defe:
    print(classes[i])

