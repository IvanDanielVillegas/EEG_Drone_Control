# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_borrador1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyparrot.Minidrone import Mambo

from Gui_final_class import BCI
############## Variables globales ######################

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



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 259)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 108, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 50, 71, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 110, 71, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 170, 71, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 90, 141, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 150, 141, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 50, 71, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 170, 71, 41))
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.Izquierdo)
        self.pushButton_2.clicked.connect(self.Adelante)
        self.pushButton_3.clicked.connect(self.Derecho)
        self.pushButton_4.clicked.connect(self.Atras)
        self.pushButton_5.clicked.connect(self.Despegar)
        self.pushButton_6.clicked.connect(self.Aterrizar)
        self.pushButton_7.clicked.connect(self.Arriba)
        self.pushButton_8.clicked.connect(self.Abajo)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Izquierdo"))
        self.pushButton_2.setText(_translate("Dialog", "Adelante"))
        self.pushButton_3.setText(_translate("Dialog", "Derecho"))
        self.pushButton_4.setText(_translate("Dialog", "Atras"))
        self.pushButton_5.setText(_translate("Dialog", "Despegar"))
        self.pushButton_6.setText(_translate("Dialog", "Arerrizar"))
        self.pushButton_7.setText(_translate("Dialog", "Arriba"))
        self.pushButton_8.setText(_translate("Dialog", "Abajo"))

    def Izquierdo(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            mambo.fly_direct(roll=10, pitch=0, yaw=0, vertical_movement=0, duration=1)
            mambo.smart_sleep(1)
            mambo.hover()
            
    def Adelante(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            mambo.fly_direct(roll=0, pitch=10, yaw=0, vertical_movement=0, duration=1)
            mambo.smart_sleep(1)
            mambo.hover()
    
    def Derecho(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            mambo.fly_direct(roll=-10, pitch=0, yaw=0, vertical_movement=0, duration=1)
            mambo.smart_sleep(1)
            mambo.hover()
            
    def Atras(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            mambo.fly_direct(roll=0, pitch=-10, yaw=0, vertical_movement=0, duration=1)
            mambo.smart_sleep(1)
            mambo.hover()
            
    def Despegar(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            print("taking off!")
            mambo.safe_takeoff(8)
            mambo.hover()
            
    def Aterrizar(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            print("landing")
            mambo.safe_land(5)
            mambo.disconnect()
            print("disconnect")
            #subprocess.Popen.kill()
        
    def Arriba(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=10, duration=1)
        
    def Abajo(self):
        if (mambo.sensors.flying_state != "emergency"):
            print(mambo.sensors.flying_state)
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-10, duration=1)

    def updater_EEG(self):
        f = open("prediccion.txt")
        dato = f.readline()
        f.close()
        print(np.array(dato))
        
        
if __name__ == "__main__":
    import sys
    
    subprocess.Popen("python Gui_final_ui.py", shell=True)
    
    mamboAddr = "d0:3a:a4:6b:e6:23"
    mambo = Mambo(mamboAddr, use_wifi=True)
    print("trying to connect")
    success = mambo.connect(num_retries=3)
    print("connected: %s" % success)

    
            
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    #timerEEG = QtCore.QTimer()
    #timerEEG.timeout.connect(ui.updater_EEG)
    #timerEEG.start(500)

    ###

    
    sys.exit(app.exec_())

