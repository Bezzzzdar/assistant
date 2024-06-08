import speech_recognition
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,  
    QLabel, 
    QToolBar,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voise recognizer")
        self.setGeometry(500, 500, 300, 300)

        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize())
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon("triangle.png"), "&Record voice", self)
        button_action.triggered.connect(self.ClickOnToolbarButton)
        toolbar.addAction(button_action)
 
    def ClickOnToolbarButton(self):
        voise_input = record_and_recognize_audio()

        label_text = "Recognized voise:" + "\n" + str(voise_input)
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
       
def record_and_recognize_audio():
    
    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=3)

        try:
            
            #print("listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            #print("something went wrong...")
            return
        
        try:
            #print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass
    
    os.remove("microphone-results.wav")
    return(recognized_data)

if __name__ == "__main__":

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


    