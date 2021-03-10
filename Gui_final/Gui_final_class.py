from PyQt5 import QtCore, QtGui, QtWidgets
from pyparrot.Minidrone import Mambo
import sys
import random
from pyOpenBCI import OpenBCICyton
import threading
import time
import numpy as np
from scipy import signal
from pyqtgraph import PlotWidget
import os
from scipy.signal import butter, sosfilt, sosfreqz
from threading import Lock, Thread
import datetime
import plotly.graph_objects as go
import subprocess


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras.layers import Input, Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
class BCI:
        
    ########################################################
    ############## Variables globales ######################
    data = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    SCALE_FACTOR = (4500000)/24/(2**23-1) #From the pyOpenBCI repo
    colors = 'bbbbbbbb'
    i = 0
    s = 0
    m = 0
    t = 0
    fila = 0 
    stm =0
    inittimer = False
    prueba = 0
    LowF = 8
    HighF =13
    features=[]
    datafilt=[]
    switch = 0
    altura = 0

    ########################################################
    ################ Modelo IA Keras #######################

    input_shape = (625,16)
    inputs = keras.layers.Input(input_shape)
    x = keras.layers.Conv1D(16, 250, activation='relu',input_shape=input_shape)(inputs)
    x = keras.layers.MaxPool1D(pool_size=2, strides = 2, padding = 'same')(x)
    x = keras.layers.Conv1D(16, 80, activation='relu',input_shape=input_shape)(x)
    x = keras.layers.MaxPool1D(pool_size=2, strides = 2, padding = 'same')(x)
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(256,activation = 'relu')(x)
    x = keras.layers.Dropout(0.2)(x)
    outputs = keras.layers.Dense(units=4, activation= 'softmax')(x)

    model = keras.Model(inputs = inputs, outputs=outputs, name ='model_sing')

    model.compile(optimizer = 'adam' , loss = 'sparse_categorical_crossentropy' , metrics = ['accuracy'])
    model.load_weights('pesosI80.h5') ### Cargar los pesos

    def save_data_EEG(self, sample):
            global data , fila , inittimer
            data.append([i*SCALE_FACTOR for i in sample.channels_data])
            fila+= 1

            
    def butter_bandpass(self,lowcut, highcut, fs, order=5):
            nyq = 0.5 * fs
            low = lowcut / nyq
            high = highcut / nyq
            sos = butter(order, [low, high], analog=False, btype='band', output='sos')
            return sos
    def butter_bandpass_filter(self,data, lowcut, highcut, fs, order=5):
        sos = self.butter_bandpass(lowcut, highcut, fs, order=order)
        y = sosfilt(sos, data)
        return y

    def start_board_Ultracortex():
        global board

        try:       
            board = OpenBCICyton( "COM3", daisy= True)
            board.start_stream(ui.save_data_EEG)
        
        except:
            #ui.Errores("DONGLE DESCONECTADO")
            print("DONGLE DESCONECTADO")
