import keras
from keras import models
from keras.models import load_model
import numpy as np
import tensorflow as tf

class Predictor:
    def __init__(self,model_path='./models/model2.h5'):
        self.model_path = model_path
        self.model = keras.models.load_model(self.model_path)
        self.classes = ['32PSK','16APSK','32QAM','FM','GMSK','32APSK','OQPSK','8ASK','BPSK','8PSK','AM-SSB-SC','4ASK','16PSK','64APSK','128QAM','128APSK','AM-DSB-SC','AM-SSB-WC','64QAM','QPSK','256QAM','AM-DSB-WC','OOK','16QAM']

    def predict(self,signal):
        """
            Function to predict modulation. Input: signal in time domain, numpy array
        """
        prediction = list(self.model.predict(signal))
        return self.classes[prediction.index(max(prediction))]
