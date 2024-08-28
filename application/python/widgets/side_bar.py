from PyQt5.QtWidgets import (
    QPushButton, 
    QVBoxLayout, 
    QDialog, 
    QLineEdit, 
    QLabel, 
    QHBoxLayout, 
    QSizePolicy, 
    QSpacerItem,
    QWidget)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, Qt

from modules.icons import base64_const_icons, base64_user_icons, _get_icon_from_base64
from widgets.account_menu import AccountMenu
from widgets.settings_menu import SettingsMenu
from widgets.authors_menu import AuthorsMenu
from widgets.about_app_menu import AboutAppMenu

class SideBar(QDialog):
    def __init__(self, overlay, parent=None):
        super().__init__(parent)
        self.overlay = overlay
        self.is_visible = False
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(200, 600)
        self.setStyleSheet("background-color: #3F00FF; color: white;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(20)

        # Логотип
        logo_icon, logo_size = _get_icon_from_base64(base64_const_icons.base64_side_bar_logo, 40, 40)
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
        account_button_icon, account_button_icon_size = _get_icon_from_base64(base64_const_icons.base64_account_icon, 25, 25)
        self.account_button.setIcon(account_button_icon)
        self.account_button.setIconSize(account_button_icon_size)
        self.account_button.setStyleSheet(self.button_style)
        layout.addWidget(self.account_button)
        self.account_button.clicked.connect(self.display_account_menu)


        self.settings_button = QPushButton("Settings", self)
        settings_button_icon, settings_button_icon_size = _get_icon_from_base64(base64_const_icons.base64_settings_icon, 25, 25)
        self.settings_button.setIcon(settings_button_icon)
        self.settings_button.setIconSize(settings_button_icon_size)
        self.settings_button.setStyleSheet(self.button_style)
        layout.addWidget(self.settings_button)
        self.settings_button.clicked.connect(self.display_settings_menu)


        self.authors_button = QPushButton("Authors", self)
        authors_button_icon, authors_button_icon_size = _get_icon_from_base64(base64_const_icons.base64_authors_icon, 25, 25)
        self.authors_button.setIcon(authors_button_icon)
        self.authors_button.setIconSize(authors_button_icon_size)
        self.authors_button.setStyleSheet(self.button_style)
        layout.addWidget(self.authors_button)
        self.authors_button.clicked.connect(self.display_authors_menu)


        self.about_app_button = QPushButton("About app", self)
        about_app_button_icon, about_app_button_icon_size = _get_icon_from_base64(base64_const_icons.base64_about_app_icon, 25, 25)
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

        self.user_label_icon = QLabel(self)
        profile_icon, profile_icon_size = _get_icon_from_base64(base64_user_icons.base64_profile_icon, 30, 30)
        self.user_label_icon.setPixmap(profile_icon.pixmap(profile_icon_size))
        self.user_label_icon.setFixedSize(profile_icon_size)
        user_label_text = QLabel(self)
        user_label_text.setText("Ivan Rastegaev")
        user_label_text.setStyleSheet("font-size: 16px;")
        user_label_text.setAlignment(Qt.AlignCenter)

        bottom_layout.setSpacing(0)

        bottom_layout.addWidget(self.user_label_icon)
        bottom_layout.addWidget(user_label_text)
        layout.addLayout(bottom_layout)
        self.setLayout(layout)

        if self.parent():
            self.account_menu = AccountMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.account_menu)

            self.settings_menu = SettingsMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.settings_menu)

            self.authors_menu = AuthorsMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.authors_menu)

            self.about_app_menu = AboutAppMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.about_app_menu) 

    def slide_in(self, start_position, end_position):
        self.setFixedSize(self.width(), self.parent().height())
        self.move(start_position)
        self.show()
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_position)
        self.animation.setEndValue(end_position)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.parent().side_bar_button.hide()
        self.animation.start()
        

    def slide_out(self, end_position):
        self.parent().side_bar_button.show()
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(300)
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(end_position)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.close)
        self.animation.start()

    def display_account_menu(self):
        if self.parent():
            self.account_menu = AccountMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.account_menu)
            # self.parent().chat_box.hide()
            self.account_menu.show()
            self.slide_out(QPoint(-self.width(), 0))
            self.is_visible = False
            
    def display_settings_menu(self):
        if self.parent():
            self.settings_menu = SettingsMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.settings_menu)
            self.settings_menu.show()
            self.slide_out(QPoint(-self.width(), 0))
            self.is_visible = False

    def display_authors_menu(self):
        if self.parent():
            self.authors_menu = AuthorsMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.authors_menu)
            self.authors_menu.show()
            self.slide_out(QPoint(-self.width(), 0))
            self.is_visible = False

    def display_about_app_menu(self):
        if self.parent():
            self.about_app_menu = AboutAppMenu(overlay=self.overlay, parent=self.parent())
            self.parent().layout.addWidget(self.about_app_menu) 
            self.about_app_menu.show()
            self.slide_out(QPoint(-self.width(), 0))
            self.is_visible = False