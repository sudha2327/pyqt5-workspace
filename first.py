# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from keras.preprocessing import image
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dropout



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 110, 151, 121))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 211, 21))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.drop = QtWidgets.QPushButton(self.centralwidget)
        self.drop.setGeometry(QtCore.QRect(90, 280, 75, 23))
        self.drop.setObjectName("drop")
        self.classify = QtWidgets.QPushButton(self.centralwidget)
        self.classify.setGeometry(QtCore.QRect(90, 360, 75, 23))
        self.classify.setObjectName("classify")
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setGeometry(QtCore.QRect(300, 400, 75, 23))
        self.train.setObjectName("train")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 270, 181, 91))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.drop.clicked.connect(self.loadImage)
        self.classify.clicked.connect(self.classifyff)
        self.train.clicked.connect(self.training)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "hindi charcter  CNN "))
        self.drop.setText(_translate("MainWindow", "DROP"))
        self.classify.setText(_translate("MainWindow", "CLASSIFY"))
        self.train.setText(_translate("MainWindow", "TRAIN"))

    def loadImage(self):
        filename=QtWidgets.QFileDialog.getOpenFileName(None,"Select Image","","Image Files(*.png,*.jpg,*.jpeg,*.bmp);;All Files(*)")

        if filename:
            print(filename)
            self.file=filename
            pixmap=QtGui.QPixmap(filename)
            pixmap=pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setpixmap(pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.Alignment)

    def classifyff(self):

        json_file=open('model.json','r')
        loaded_model_json=json_file.read()
        json_file.close()
        loaded_model=model_from_json(loaded_model_json)
        loaded_model.load_weight("model.h5")
        print("model has been loadede")
              label=["sunna","ek","das","be","tran","char","panc","cha","sat","at","nav","ALA","ANA","B","BHA","CH","CHH","D","DA","DH","DHA","F","G","GH","GNA","H","J","JH","K","KH","KSH","L","M","N","P","R","S","SH","SHH","T","TA","TH","THA","V","Y"]
        path2=self.file

        print(path2)

        test_image=image.load_img(path2, target_size=(128,128))
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image,axis=0)
        result=loaded_model.predict(test_image)

        fresult=np.max(result)
        label2=label(result.argmax())
        print(label2)
        self.textEdit.setText(label2)

    def training(self):

        self.textEdit.setText("training under process")
        model=Sequential()
        model.add(Conv2d(32,kernl_size=(3,3),activation='relu',input_shape=(128,128)))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2d(64,kernal_size=(3,3),activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Dense(0.2))
        model.add(Flatten())
        model.add(Dense(128,activation='relu'))
        model.add(Dropout(0.3))
        model.add(Dense(45,activation='softmax'))
        model.compile(optimizer='adam',loss='categorical_cressentropy',metrics=['accuracy'])

        train_datagen=ImageDataGenerator(rescale=None,
                                        shear_range=0.2,
                                        zoom_range=0.2,
                                        horizontal_flip=True)
        test_datagen=ImageDataGenerator(rescale=1./255)

        training_Set=train_datagen.flow_from_directory("S:/coding/Intern project/Pyqt5 workspace/char reg/train",
                                                       target_size=(128,128),
                                                       batch_size=32,
                                                       class_mode='categorical')

        labels=(training_Set,class_indics)
        print(labeles)
        val_Set = test_datagen.flow_from_directory("S:/coding/Intern project/Pyqt5 workspace/char reg/val",
                                                         target_size=(128, 128),
                                                         batch_size=32,
                                                         class_mode='categorical')

        model.fit_generator(training_Set,steps_per_epoch=100,epochs=10,validation_Data=val_Set,validation_steps=125)


        model_json=model.to_json()
        with open("model.json","w") as json_file:
            json_file.write("model.h5")
            print("sved model")
            self.textEdit.setText("saved model to the disk")





        










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
