import sys
import base64
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLineEdit, QLabel, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage


# Логотип в формате base64
base64_logo = """
    iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAADKUlEQVR4nO2ZS2
    yMURTHbx9RVCORTNrYNJFGQ3SBeCwIaUJj01VFV8TGxsqeeG5QCZGmNpYikUpEUlYIk1BFlWpaFoJGiVcoiwbJTy7n
    cjPm8X3jnslXmX/yJTN3zvf/n3Of554xpoxoAK4Dd8x0BwIz3UE5kIThfxqRNHDDJAHALuAikCqhZgo4D+wMSXpBZs
    gwUB+MOLdevWhZ9IbuHUc8AjTksKsAlgMHgGvAGPBFnlFp2w8sy6PVIBqu41IaveQEhrIEsAV4THRY28323QyuB16H
    6Yy+9NYQ0O+1NQEDnoPPgBPARqAZqJXHfm6T36yNQz+wwOO7DdzPNepaga0F3ohD48AOoCrCe5UyGk/l3fdAa2m8/t
    uZVuCrOHIOmF0Ehx2pXuGwXOt1vM3tQJP0osWRzHkek8uury7heudPM1WI8IA3EhWBON3I3ArBGUXU7k4Wz4uZTgWm
    2Qvh7gjFm6/n3Ba7TYF/u3CPqo6KHHZui61U4K+SkbZYGprfFzooIscVNU6Kxj6jKGJTDIs2RY1NonHFKIo8EZEmRY
    1m0RgrlmBORurgkPZsJqWtLqTzGX7UicZkVL+iBvL7UgRMSVuNYiA1ojEV1a9iRFxepXYn4VdiavHaKIrYU9dijXIi
    anHTKIp0/5SAvYoae0Sj2yiKtIvIiKLGsGi0G+WF6NbJKsXM4a3mhuLEdotYOnQ+xJ8DV+9U98RmefnQ1oC8nd5Nsz
    YUbyHRDhH9DCwOwLcQ+CScnWG8jC7eI8K25DPvH3jmAo+E63RYL6MvfFsBQf4Dib04gRnAVeG4Z6etjrfZT9279mD0
    al2uEnI2zuKXS9oZedfeDOdL+yDwUK0clFGgG3ROA4uAD3F3G2sr73wEWrz2IXdWBU+FCpVMgXXANynpLInA1yL234
    ENJSuZApc94qy9BBwWm54IfKfEtitCEftSiBgc8SGgL1/vAI3ER2OBWdBnr9em1IgbhUkqKAeSMOBNGZsdy9cV+eym
    QyCr5evKfHaJBPAqxjJ5aZIK4FiMQI6apAKYKcFM5AlgQv4P0b0BhgJQLQfpuDz2c3UwgTJMsvEDHSW6Nwb7oTcAAA
    AASUVORK5CYII=
"""

base64_side_menu_icon = """
    iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAALUlEQVR4nGNgGA
    UjChxmYGD4TyV8mNYWHKJ/+IwCYsBoKhoFlIPRVDQKBikAACEWdLZVlt8CAAAAAElFTkSuQmCC
"""

class SideMenu(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(200, 600)
        self.setStyleSheet("background-color: #3F00FF; color: white;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(20)

        # Логотип
        logo_icon, logo_size = _get_icon_from_base64(base64_logo, 40, 40)
        logo = QLabel(self)
        logo.setPixmap(logo_icon.pixmap(logo_size))
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        # Поле поиска
        search_box = QLineEdit(self)
        search_box.setPlaceholderText("Search")
        search_box.setStyleSheet("""
            QLineEdit {
                background-color: #4169E1;
                border: none;
                border-radius: 10px;
                padding: 5px 10px;
                color: white;
            }
            QLineEdit::placeholder {
                color: #4169E1;
            }
        """)
        layout.addWidget(search_box)

        # Кнопки меню
        buttons = [
            ("People", "path_to_people_icon"),
            ("Favourites", "path_to_favourites_icon"),
            ("Workflows", "path_to_workflows_icon"),
            ("Updates", "path_to_updates_icon"),
            ("Plug-Ins", "path_to_plugins_icon"),
            ("Notifications", "path_to_notifications_icon")
        ]

        for text, icon_path in buttons:
            button = QPushButton(text, self)
            button.setIcon(QIcon(icon_path))
            button.setStyleSheet("""
                QPushButton {
                    background-color: #3F00FF;
                    border: none;
                    color: white;
                    text-align: left;
                    padding: 10px;
                    font-size: 16px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #000080;
                }
            """)
            layout.addWidget(button)

        # Добавляем вертикальный разделитель
        separator = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(separator)

        # Нижняя часть меню (пользователь и вопрос)
        bottom_layout = QHBoxLayout()
        user_label = QLabel("Ivan Rastegaev", self)
        user_label.setStyleSheet("font-size: 14px;")
        user_icon = QLabel(self)
        user_pixmap = QPixmap('path_to_user_image')
        user_icon.setPixmap(user_pixmap)
        bottom_layout.addWidget(user_icon)
        bottom_layout.addWidget(user_label)
        bottom_layout.addStretch()
        question_button = QPushButton("?", self)
        question_button.setStyleSheet("""
            QPushButton {
                background-color: #4169E1;
                border: none;
                color: white;
                font-size: 16px;
                width: 30px;
                height: 30px;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        bottom_layout.addWidget(question_button)
        
        layout.addLayout(bottom_layout)
        
        self.setLayout(layout)

    def slide_in(self, start_position, end_position):
        self.move(start_position)
        self.show()
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_position)
        self.animation.setEndValue(end_position)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start()

    def slide_out(self, end_position):
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(300)
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(end_position)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.close)
        self.animation.start()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Assistant")
        self.setGeometry(500, 300, 900, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }
        """)
        # Set the center widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Icon in base64 code
        side_menu_icon, side_menu_icon_size = _get_icon_from_base64(base64_side_menu_icon, 35, 35) 

        # Create a side menu button and set an icon
        self.side_menu_button = QPushButton("", self)
        self.side_menu_button.setIcon(side_menu_icon)
        self.side_menu_button.setIconSize(side_menu_icon_size)
        self.side_menu_button.setGeometry(0, 0, 35, 35)  

        # Set the styles for the side menu button
        self.side_menu_button.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF; 
                border: none;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            }
                    
            QPushButton:hover {
                background-color: #3F00FF;
            }

            QPushButton:focus {
                outline: none;
            }
        """)

        # Connect the button press signal
        self.side_menu_button.clicked.connect(self.toggle_side_menu)

        # Initializing the side menu
        self.side_menu = SideMenu(self)
        self.side_menu.setGeometry(-self.side_menu.width(), 0, self.side_menu.width(), self.side_menu.height())
        self.side_menu_hidden_position = QPoint(-self.side_menu.width(), 0)
        self.side_menu_visible_position = QPoint(0, 0)
        self.side_menu_visible = False

    def toggle_side_menu(self):
        if self.side_menu_visible:
            self.side_menu.slide_out(self.side_menu_hidden_position)
        else:
            self.side_menu.slide_in(self.side_menu_hidden_position, self.side_menu_visible_position)
        self.side_menu_visible = not self.side_menu_visible

    def mousePressEvent(self, event):
        # Check if the click was outside of the side menu
        if self.side_menu_visible and not self.side_menu.geometry().contains(self.mapFromGlobal(event.globalPos())):
            self.side_menu.slide_out(self.side_menu_hidden_position)
            self.side_menu_visible = False
        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        # Hide menu if Esc key is pressed
        if event.key() == Qt.Key_Escape and self.side_menu_visible:
            self.side_menu.slide_out(self.side_menu_hidden_position)
            self.side_menu_visible = False
        super().keyPressEvent(event)

def _get_icon_from_base64(base64_string: str, width: int, height: int):
    """Function for decode image form base64 code"""

    image_data = base64.b64decode(base64_string)
    image = QImage()
    image.loadFromData(image_data)
    pixmap = QPixmap.fromImage(image)
    icon_size = QSize(width, height)
    scaled_pixmap = pixmap.scaled(icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    icon = QIcon(scaled_pixmap)

    return icon, icon_size

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
