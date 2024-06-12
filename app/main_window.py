from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,  
    QLabel, 
    QToolBar,
)
from modules.record_and_recognize import record_and_recognize_audio
from modules.assistant import VoiseAssistant
import pathlib
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Assistant")
        self.setGeometry(500, 500, 300, 300)

        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize())
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon(str(pathlib.Path('./app', 'icons', 'triangle.png'))), "&Record voice", self)
        button_action.triggered.connect(self.ClickOnToolbarButton)
        toolbar.addAction(button_action)
        
        button_action_say_text = QAction("Say text", self)
        button_action_say_text.triggered.connect(self.ClickOnToolbarButtonSayText)
        toolbar.addAction(button_action_say_text)

    def ClickOnToolbarButton(self):
        voise_input = record_and_recognize_audio()

        label_text = "Recognized voise:" + "\n" + str(voise_input)
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

    def ClickOnToolbarButtonSayText(self):
        assistant = VoiseAssistant('Tyler', 'ru')
        VoiseAssistant.assistant_say(assistant, "text to say")
        

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()