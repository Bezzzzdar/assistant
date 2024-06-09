from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,  
    QLabel, 
    QToolBar,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
import sys
import json
import pathlib

from modules.rec_module import record_and_recognize_audio

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voise recognizer")
        self.setGeometry(500, 500, 300, 300)

        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize())
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon(str(pathlib.Path('./app', 'icons', 'triangle.png'))), "&Record voice", self)
        button_action.triggered.connect(self.ClickOnToolbarButton)
        toolbar.addAction(button_action)
 
    def ClickOnToolbarButton(self):
        voise_input = record_and_recognize_audio()

        label_text = "Recognized voise:" + "\n" + str(voise_input)
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

class VoiseAssistant:
    name = ""
    sex = ""
    language = ""

def execute_commad():
    with open(pathlib.Path('./app', 'commands', 'commands.json'), "r") as file:
        templates = json.load(file)
        

if __name__ == "__main__":

    assistant = VoiseAssistant()
    assistant.name = "Assistant"
    assistant.sex = "male"
    assistant.language = "ru"

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

    

    