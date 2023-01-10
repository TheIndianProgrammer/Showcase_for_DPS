
#=============Imports===============
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QMovie

import speech_recognition as sr
import pyttsx3
import os
import pyjokes
from Infowindow import Ui_infowin
from settings import Ui_Settings
import settings as tts

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from tensorflow.python.framework import ops
import numpy
import tflearn
import tensorflow
import random
import json
#======================================

#=============Data_Feed================
with open("inputs.json") as file:
    data = json.load(file)


words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)
#===================================

#===========Graphics================

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 844)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphics/Icons window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 730, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.Msgbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Msgbox.setGeometry(QtCore.QRect(10, 760, 291, 51))
        self.Msgbox.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                  "border-color: rgb(255, 255, 255);")

        self.Msgbox.setObjectName("Msgbox")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(60, 100, 311, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("animation_logo.gif"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.movie = QMovie("Graphics/animation_logo.gif")
        self.movie.start()
        self.logo.setMovie(self.movie)

        self.micb = QtWidgets.QPushButton(self.centralwidget)
        self.micb.setGeometry(QtCore.QRect(370, 760, 50, 50))
        self.micb.setText("")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Graphics/mic button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.micb.setIcon(icon1)
        self.micb.setIconSize(QtCore.QSize(48, 48))
        self.micb.setCheckable(False)
        self.micb.setFlat(True)
        self.micb.setObjectName("micb")
        self.micb.clicked.connect(lambda: rec(self))

        def rec(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Please Speak...")
                self.audio = r.listen(source)
                try:
                    print("You have said \n" + r.recognize_google(self.audio))
                    self.Msgbox.setText(r.recognize_google(self.audio))
                except Exception as e:
                    print("Error :  " + str(e))

        self.sendb = QtWidgets.QPushButton(self.centralwidget)
        self.sendb.setGeometry(QtCore.QRect(310, 760, 50, 50))
        self.sendb.setText("")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Graphics/send (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.sendb.setIcon(icon2)
        self.sendb.setIconSize(QtCore.QSize(48, 48))
        self.sendb.setCheckable(False)
        self.sendb.setFlat(True)
        self.sendb.setObjectName("sendb")

        #===========Info Button========
                
        self.Infob = QtWidgets.QPushButton(self.centralwidget)
        self.Infob.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.Infob.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Graphics/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Infob.setIcon(icon3)
        self.Infob.setIconSize(QtCore.QSize(30, 30))
        self.Infob.setCheckable(False)
        self.Infob.setFlat(True)
        self.Infob.setObjectName("Infob")

        def open_info(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_infowin()
            self.ui.setupUi(self.window)   
            self.window.show()

        self.Infob.clicked.connect(lambda: open_info(self))

        #========Settings Button========
        self.settingsb = QtWidgets.QPushButton(self.centralwidget)
        self.settingsb.setGeometry(QtCore.QRect(50, 20, 41, 41))
        self.settingsb.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Graphics\\settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsb.setIcon(icon3)
        self.settingsb.setIconSize(QtCore.QSize(30, 30))
        self.settingsb.setCheckable(False)  
        self.settingsb.setFlat(True)
        self.settingsb.setObjectName("settingsb")

        def open_set(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Settings()
            self.ui.setupUi(self.window)   
            self.window.show()
        
        self.settingsb.clicked.connect(lambda: open_set(self))
            
        #= = =
        self.line2 = QtWidgets.QLabel(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(-470, 830, 954, 23))
        self.line2.setText("")
        self.line2.setPixmap(QtGui.QPixmap("Graphics/line.png"))
        self.line2.setObjectName("line2")
        self.line1 = QtWidgets.QLabel(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(-450, -10, 954, 23))
        self.line1.setText("")
        self.line1.setPixmap(QtGui.QPixmap("Graphics/line.png"))
        self.line1.setObjectName("line1")
        self.sgbo = QtWidgets.QLabel(self.centralwidget)
        self.sgbo.setGeometry(QtCore.QRect(70, 230, 321, 271))
        self.sgbo.setText("")
        self.sgbo.setPixmap(QtGui.QPixmap("Graphics/sgbox.png"))
        self.sgbo.setScaledContents(False)
        self.sgbo.setObjectName("sgbo")

        #============Reply Button===========
        self.replyb = QtWidgets.QLabel(self.centralwidget)
        self.replyb.setGeometry(QtCore.QRect(80, 320, 281, 131))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.replyb.setFont(font)
        self.replyb.setStyleSheet("color: rgb(0, 0, 0);")
        self.replyb.setLineWidth(0)
        self.replyb.setAlignment(QtCore.Qt.AlignCenter)
        self.replyb.setWordWrap(True)
        self.replyb.setIndent(2)
        self.replyb.setObjectName("replyb")

        #= = =
        self.sendb.clicked.connect(lambda: chat(self))

        #= = =
        self.info2b = QtWidgets.QPushButton(self.centralwidget)
        self.info2b.setGeometry(QtCore.QRect(10, 690, 121, 41))
        self.info2b.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Graphics/b1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info2b.setIcon(icon4)
        self.info2b.setIconSize(QtCore.QSize(115, 45))
        self.info2b.setFlat(True)
        self.info2b.setObjectName("info2b")
        self.info2b.clicked.connect(lambda: open_info(self))
        
        #============Exit Button===========
        self.exitb = QtWidgets.QPushButton(self.centralwidget)
        self.exitb.setGeometry(QtCore.QRect(320, 690, 131, 41))
        self.exitb.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Graphics/b3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitb.setIcon(icon5)
        self.exitb.setIconSize(QtCore.QSize(160, 40))
        self.exitb.setFlat(True)
        self.exitb.setObjectName("exitb")
        self.exitb.clicked.connect(lambda: self.exit(self, Ui_MainWindow))

        def open_read(self):
            self.c = "README.txt"
            os.startfile(self.c)
        self.tra = QtWidgets.QPushButton(self.centralwidget)
        self.tra.setGeometry(QtCore.QRect(160, 690, 141, 41))
        self.tra.setText("")

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Graphics/b2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tra.setIcon(icon6)
        self.tra.setIconSize(QtCore.QSize(140, 90))
        self.tra.setFlat(True)
        self.tra.setObjectName("tra")
        self.tra.clicked.connect(lambda: open_read(self))
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        def chat(self):
            tts_toggle_var = self.ui.checkradio()
            print("Start talking with the bot (type quit to stop)!")
            print('Text to speech enabled: ',tts_toggle_var)

            #=====================TTS=======================

            #=================Utilities==================
            if self.Msgbox.text() in "Open Snipping Tool":
                self.replyb.setText("Sure...")
                
                c = "C:\Windows\System32\SnippingTool.exe"
                os.startfile(c)

            elif self.Msgbox.text() in ["Open Calculator",'open calculator'] :
                self.replyb.setText("Sure...")
                c = "calc"
                os.startfile(c)

            elif self.Msgbox.text() in ["Open Notepad",'open notepad']:
                self.replyb.setText("Sure...")
                c = "notepad"
                os.startfile(c)

            elif self.Msgbox.text() in ["Open Wordpad",'open wordpad']:
                self.replyb.setText("Sure...")
                c = "C:\Program Files\Windows NT\Accessories\wordpad.exe"
                os.startfile(c)

            elif self.Msgbox.text() in ['tell me a joke', 'Tell me a joke', 
                                        'can you tell me a joke', 
                                        'how funny are you','make me laugh','Make me laugh']:
                
                jokes = pyjokes.get_joke(language="en", category="all")

                self.replyb.setText(jokes+" 🤣")

            else:
                inp = self.Msgbox.text()
                results = model.predict([bag_of_words(inp, words)])
                results_index = numpy.argmax(results)
                tag = labels[results_index]

                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses'] 

                self.replyb.setText(random.choice(responses))

                if tts_toggle_var == True:
                    engine = pyttsx3.init()
                    voices = engine.getProperty('voices')
                    engine. setProperty("rate", 150)
                    engine.setProperty('voice', voices[1].id)
                    engine.say(self.replyb.text())
                    engine.runAndWait()
                else:
                    pass
            #================================================ 
                
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MChat - Chatbot"))
        self.Msgbox.setText(_translate("MainWindow", "Type Something Here..."))
        self.micb.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.sendb.setShortcut(_translate("MainWindow", "Enter, Return"))
        self.Infob.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.settingsb.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.replyb.setText(_translate("MainWindow", "Hello Friend !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
