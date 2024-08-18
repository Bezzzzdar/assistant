import sys
import base64
from dataclasses import dataclass
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton, 
    QVBoxLayout, 
    QWidget, 
    QDialog, 
    QLineEdit, 
    QLabel, 
    QHBoxLayout, 
    QSizePolicy, 
    QSpacerItem, 
    QTextEdit,
    QLayout)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QSize, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QImage

from modules.icons import Base64Icons, Base64ConstIcons, Base64UserIcons

const_icons = Base64ConstIcons()
user_icons = Base64UserIcons()

@dataclass
class GlobalParametrs:
    side_menu_visible: bool = False
    modal_account_menu_visible: bool = False

global_parametrs = GlobalParametrs()

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
        logo_icon, logo_size = _get_icon_from_base64(const_icons.base64_side_menu_logo, 40, 40)
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
                padding: 10px 15px;
                color: white;
                font-size: 16px
            }
            QLineEdit::placeholder {
                color: #4169E1;
            }
        """)
        layout.addWidget(search_box)

        self.button_style = """
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
        """

        self.account_button = QPushButton("Account", self)
        account_button_icon, account_button_icon_size = _get_icon_from_base64(const_icons.base64_account_icon, 25, 25)
        self.account_button.setIcon(account_button_icon)
        self.account_button.setIconSize(account_button_icon_size)
        self.account_button.setStyleSheet(self.button_style)
        layout.addWidget(self.account_button)
        self.account_button.clicked.connect(self.display_account_menu)


        self.settings_button = QPushButton("Settings", self)
        settings_button_icon, settings_button_icon_size = _get_icon_from_base64(const_icons.base64_settings_icon, 25, 25)
        self.settings_button.setIcon(settings_button_icon)
        self.settings_button.setIconSize(settings_button_icon_size)
        self.settings_button.setStyleSheet(self.button_style)
        layout.addWidget(self.settings_button)
        self.settings_button.clicked.connect(self.display_settings_menu)


        self.authors_button = QPushButton("Authors", self)
        authors_button_icon, authors_button_icon_size = _get_icon_from_base64(const_icons.base64_authors_icon, 25, 25)
        self.authors_button.setIcon(authors_button_icon)
        self.authors_button.setIconSize(authors_button_icon_size)
        self.authors_button.setStyleSheet(self.button_style)
        layout.addWidget(self.authors_button)
        self.authors_button.clicked.connect(self.display_authors_menu)


        self.about_app_button = QPushButton("About app", self)
        about_app_button_icon, about_app_button_icon_size = _get_icon_from_base64(const_icons.base64_about_app_icon, 25, 25)
        self.about_app_button.setIcon(about_app_button_icon)
        self.about_app_button.setIconSize(about_app_button_icon_size)
        self.about_app_button.setStyleSheet(self.button_style)
        layout.addWidget(self.about_app_button)
        self.about_app_button.clicked.connect(self.display_about_app_menu)


        # Добавляем вертикальный разделитель
        separator = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(separator)

        # Нижняя часть меню
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)

        user_label_icon = QLabel(self)
        profile_icon, profile_icon_size = _get_icon_from_base64(user_icons.base64_profile_icon, 35, 35)
        user_label_icon.setPixmap(profile_icon.pixmap(profile_icon_size))
        user_label_icon.setFixedSize(profile_icon_size)
        user_label_text = QLabel(self)
        user_label_text.setText("Ivan Rastegaev")
        user_label_text.setStyleSheet("font-size: 14px;")
        user_label_text.setAlignment(Qt.AlignCenter)

        bottom_layout.setSpacing(0)

        bottom_layout.addWidget(user_label_icon)
        bottom_layout.addWidget(user_label_text)
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
    
    def display_account_menu(self):
        if self.parent() and isinstance(self.parent(), MainWindow):
            self.modal_account_menu = ModalAccountMenu(self.parent())
            self.modal_account_menu.show()
            self.slide_out(QPoint(-self.width(), 0))
            global_parametrs.side_menu_visible = False
            global_parametrs.modal_account_menu_visible = True
            # modal_account_menu.exec_()

    def display_settings_menu(self):
        if self.parent() and isinstance(self.parent(), MainWindow):
            modal_settings_menu = ModalSettingsMenu(self.parent())
            self.slide_out(QPoint(-self.width(), 0))
            global_parametrs.side_menu_visible = False
            modal_settings_menu.exec_()

    def display_authors_menu(self):
        if self.parent() and isinstance(self.parent(), MainWindow):
            modal_authors_menu = ModalAuthorsMenu(self.parent())
            self.slide_out(QPoint(-self.width(), 0))
            global_parametrs.side_menu_visible = False
            modal_authors_menu.exec_()

    def display_about_app_menu(self):
        if self.parent() and isinstance(self.parent(), MainWindow):
            modal_about_app_menu = ModalAboutAppMenu(self.parent())
            self.slide_out(QPoint(-self.width(), 0))
            global_parametrs.side_menu_visible = False
            modal_about_app_menu.exec_()

class ModalAccountMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent
        self.initial_width_ratio = 0.44
        self.initial_height_ratio = 0.92
        self.setWindowFlags(Qt.Tool | self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(350, 550)
        self.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                border: 1px solid #D3D3D3;
                border-radius: 10px;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Заголовок
        header = QLabel("Account", self)
        header.setStyleSheet("""
            QLabel {
                background-color: #3F00FF;
                color: white;
                padding: 10px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                font-weight: bold;
            }
        """)
        header.setFixedHeight(30)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Поле для имени пользователя
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.username_input)

        # Поле для email
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.email_input)

        # Кнопка для сохранения настроек
        save_button = QPushButton("Save", self)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        layout.addWidget(save_button)

        close_button = QPushButton("Close", self)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        close_button.clicked.connect(self.closeModal)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def resize_proportionally(self):
        # Пропорции виджета относительно размеров окна
        if self.main_window is None:
            return
        
        main_window_width = self.main_window.width()
        main_window_height =  self.main_window.height()
        modal_menu_width = int(main_window_width * self.initial_width_ratio)
        modal_menu_height = int(main_window_height * self.initial_height_ratio)

        self.setFixedSize(modal_menu_width, modal_menu_height)
        

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_proportionally()
    
    def showEvent(self, event):
        super().showEvent(event)
        if self.main_window:
            # Получаем положение и размеры главного окна
            main_window_rect = self.main_window.rect()
            main_window_pos = self.main_window.pos()

            # Определяем центр главного окна
            center = main_window_pos + main_window_rect.center() + QPoint(0, 31)
            self.move(center - self.rect().center())

            self.resize_proportionally()

            # Добавляем анимацию
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(300)
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.setEasingCurve(QEasingCurve.InOutQuad)  
            self.animation.start()

    def closeModal(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.close)
        self.animation.start()
        global_parametrs.modal_account_menu_visible = False


class ModalSettingsMenu(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 550)
        self.setStyleSheet("""
            QDialog {
                background-color: #FFFFFF;
                border: 1px solid #D3D3D3;
                border-radius: 10px;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Заголовок
        header = QLabel("Settings", self)
        header.setStyleSheet("""
            QLabel {
                background-color: #3F00FF;
                color: white;
                padding: 10px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                font-weight: bold;
            }
        """)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Поле для имени пользователя
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.username_input)

        # Поле для email
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.email_input)

        # Кнопка для сохранения настроек
        save_button = QPushButton("Save", self)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        layout.addWidget(save_button)

        close_button = QPushButton("Close", self)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        close_button.clicked.connect(self.closeModal)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def closeModal(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.close)  
        self.animation.start()
    
    def showEvent(self, event):
        super().showEvent(event)
        if self.main_window:
            # Получаем положение и размеры главного окна
            main_window_rect = self.main_window.rect()
            main_window_pos = self.main_window.pos()

            # Определяем центр главного окна
            center = main_window_pos + main_window_rect.center()
            self.move(center - self.rect().center())

            # Добавляeм анимацию
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(200)
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.setEasingCurve(QEasingCurve.InOutQuad)  
            self.animation.start()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the account settings menu
        if self.main_window:
            self.setFixedSize(int(self.main_window.width() / 2.5), int(self.main_window.height() / 1.5))


class ModalAuthorsMenu(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 550)
        self.setStyleSheet("""
            QDialog {
                background-color: #FFFFFF;
                border: 1px solid #D3D3D3;
                border-radius: 10px;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Заголовок
        header = QLabel("Authors", self)
        header.setStyleSheet("""
            QLabel {
                background-color: #3F00FF;
                color: white;
                padding: 10px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                font-weight: bold;
            }
        """)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Поле для имени пользователя
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.username_input)

        # Поле для email
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.email_input)

        # Кнопка для сохранения настроек
        save_button = QPushButton("Save", self)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        layout.addWidget(save_button)

        close_button = QPushButton("Close", self)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        close_button.clicked.connect(self.closeModal)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def closeModal(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.close)  
        self.animation.start()

    def showEvent(self, event):
        super().showEvent(event)
        if self.main_window:
            # Получаем положение и размеры главного окна
            main_window_rect = self.main_window.rect()
            main_window_pos = self.main_window.pos()

            # Определяем центр главного окна
            center = main_window_pos + main_window_rect.center()
            self.move(center - self.rect().center())

            # Добавляeм анимацию
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(200)
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.setEasingCurve(QEasingCurve.InOutQuad)  
            self.animation.start()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the account settings menu
        if self.main_window:
            self.setFixedSize(int(self.main_window.width() / 2.5), int(self.main_window.height() / 1.5))


class ModalAboutAppMenu(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 550)
        self.setStyleSheet("""
            QDialog {
                background-color: #FFFFFF;
                border: 1px solid #D3D3D3;
                border-radius: 10px;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Заголовок
        header = QLabel("About app", self)
        header.setStyleSheet("""
            QLabel {
                background-color: #3F00FF;
                color: white;
                padding: 10px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                font-weight: bold;
            }
        """)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Поле для имени пользователя
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.username_input)

        # Поле для email
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("""
            QLineEdit {
                background-color: #F0F8FF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.email_input)

        # Кнопка для сохранения настроек
        save_button = QPushButton("Save", self)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        layout.addWidget(save_button)

        close_button = QPushButton("Close", self)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #3F00FF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000080;
            }
        """)
        close_button.clicked.connect(self.closeModal)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def closeModal(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.close)  
        self.animation.start()
    
    def showEvent(self, event):
        super().showEvent(event)
        if self.main_window:
            # Получаем положение и размеры главного окна
            main_window_rect = self.main_window.rect()
            main_window_pos = self.main_window.pos()

            # Определяем центр главного окна
            center = main_window_pos + main_window_rect.center()
            self.move(center - self.rect().center())

            # Добавляeм анимацию
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(200)
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.setEasingCurve(QEasingCurve.InOutQuad)  
            self.animation.start()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the account settings menu
        if self.main_window:
            self.setFixedSize(int(self.main_window.width() / 2.5), int(self.main_window.height() / 1.5))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Assistant")
        self.setGeometry(500, 300, 900, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0FFFF;
            }
        """)
        self.setMinimumSize(900, 600)

        # Set the center widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Icon in base64 code
        side_menu_icon, side_menu_icon_size = _get_icon_from_base64(const_icons.base64_side_menu_icon, 35, 35) 

        # Create a side menu button and set an icon
        self.side_menu_button = QPushButton("", self)
        self.side_menu_button.setIcon(side_menu_icon)
        self.side_menu_button.setIconSize(side_menu_icon_size)
        self.side_menu_button.setGeometry(0, 0, 35, 35)  

        # Set the styles for the side menu button
        self.side_menu_button.setStyleSheet("""
            QPushButton {
                background-color: #F0FFFF; 
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
        global_parametrs.side_menu_visible = False

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the side menu to match the height of the main window
        if global_parametrs.side_menu_visible:
            self.side_menu.setFixedSize(self.side_menu.width(), self.height())
        if global_parametrs.modal_account_menu_visible:
            self.side_menu.modal_account_menu.resize_proportionally()


    def toggle_side_menu(self):
        if global_parametrs.side_menu_visible:
            self.side_menu.slide_out(self.side_menu_hidden_position)
        else:
            self.side_menu.setFixedSize(self.side_menu.width(), self.height())  # Match height of main window
            self.side_menu.slide_in(self.side_menu_hidden_position, self.side_menu_visible_position)
        global_parametrs.side_menu_visible = not global_parametrs.side_menu_visible

    def mousePressEvent(self, event):
        # Check if the click was outside of the side menu
        if global_parametrs.side_menu_visible and not self.side_menu.geometry().contains(self.mapFromGlobal(event.globalPos())):
            self.side_menu.slide_out(self.side_menu_hidden_position)
            global_parametrs.side_menu_visible = False
        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        # Hide menu if Esc key is pressed
        if event.key() == Qt.Key_Escape and global_parametrs.side_menu_visible:
            self.side_menu.slide_out(self.side_menu_hidden_position)
            global_parametrs.side_menu_visible = False
        super().keyPressEvent(event)

def _get_icon_from_base64(base64_icon: str, width: int, height: int):
    """Function for decode image from base64 code"""
    image_data = base64.b64decode(base64_icon)
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
