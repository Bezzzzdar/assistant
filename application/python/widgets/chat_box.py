from PyQt5.QtWidgets import (
    QPushButton, 
    QVBoxLayout, 
    QDialog, 
    QLineEdit, 
    QLabel, 
    QHBoxLayout, 
    QSizePolicy, 
    QSpacerItem,
    QWidget,
    QListWidget,
    QListWidgetItem)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, Qt

class ChatBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #F0FFFF;
                border-radius: 10px;
            }
        """)
        self.setFixedSize(1000, 650)
        layout = QVBoxLayout()

        # Список сообщений
        self.message_list = QListWidget()
        self.message_list.setStyleSheet("""
            QListWidget {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.message_list)

        # Поле для ввода и кнопка отправки
        input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Ask the assistant")
        self.message_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #3F00FF; 
                height: 18px;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                background-color: #3F00FF;
                height: 20px;
                width: 50px;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

        # Соединение сигнала отправки сообщения с функцией
        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.add_message("You", message, align_right=True)
            self.message_input.clear()

            # Имитация ответа ассистента
            self.receive_message("Assistant", self.get_assistant_reply(message))

    def get_assistant_reply(self, message):
        # Эта функция имитирует работу вашего ассистента
        # Здесь можно вызывать функции голосового ассистента
        return f"Echo: {message}"

    def receive_message(self, sender, message):
        self.add_message(sender, message, align_right=False)

    def add_message(self, sender, message, align_right=False):
        # Создание нового сообщения
        item = QListWidgetItem(f"{sender}: {message}")
        
        # Настройка выравнивания
        if align_right:
            item.setTextAlignment(Qt.AlignRight)
        else:
            item.setTextAlignment(Qt.AlignLeft)

        self.message_list.addItem(item)

