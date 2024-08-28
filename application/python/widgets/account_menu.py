import base64
from io import BytesIO

from dataclasses import dataclass
from PyQt5.QtWidgets import ( 
    QPushButton, 
    QVBoxLayout, 
    QDialog, 
    QLineEdit, 
    QLabel, 
    QHBoxLayout, 
    QSizePolicy, 
    QSpacerItem, 
    QGraphicsOpacityEffect,
    QCheckBox, 
    QFileDialog,
    QWidget)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QColor

from modules.icons import base64_user_icons, _get_icon_from_base64


class AccountMenu(QDialog):
    def __init__(self, overlay, parent):
        super().__init__(parent)
        self.main_window = parent
        self.overlay = overlay
        self.initial_width_ratio = 0.44
        self.initial_height_ratio = 0.92
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 600)
        self.setStyleSheet("""
            QDialog {
                background-color: #F0FFFF;
                border-radius: 10px;
                border: 2px solid #F0FFFF
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Заголовок
        self.header = QLabel("Account", self)
        self.header.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #3F00FF;
                font-weight: bold;                           
            }
        """)
        self.header.setFixedHeight(40)
        self.header.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        layout.addWidget(self.header)
        
        self.owner_icon_selection = QPushButton(self)
        self.owner_icon_selection.setFixedSize(100, 100)
        self.owner_icon_selection.setStyleSheet("""
            QPushButton {
                background-color: #F0FFFF;
                border: none;                                    
            }
        """)
        owner_icon, owner_icon_size = _get_icon_from_base64(base64_user_icons.base64_profile_icon, 100, 100)
        rounded_owner_icon = self.make_round_icon(owner_icon.pixmap(owner_icon_size))
        self.owner_icon_selection.setIcon(rounded_owner_icon)
        self.owner_icon_selection.setIconSize(owner_icon_size)
        layout.addWidget(self.owner_icon_selection, alignment=Qt.AlignCenter)

        self.personal_data_selection = QLabel("Personal data", self)
        self.personal_data_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)

        self.owner_icon_selection.clicked.connect(self.change_user_icon)
        layout.addWidget(self.personal_data_selection)

        # Поле для имени пользователя
        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("First name")
        self.first_name_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.first_name_input)

        # Поле для фамилии пользователя
        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Last name")
        self.last_name_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.last_name_input)

        self.owner_tag_selection = QLabel("User tag", self)
        self.owner_tag_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)
        layout.addWidget(self.owner_tag_selection)

        # Поле для тэга пользователя
        self.tag_input = QLineEdit(self)
        self.tag_input.setPlaceholderText("@bezzdarn0st")
        self.tag_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.tag_input)

        self.owner_language_selection = QLabel("Language", self)
        self.owner_language_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)
        layout.addWidget(self.owner_language_selection)

        self.owner_language_layout = QHBoxLayout()

        self.owner_russian_language_checkbox = QCheckBox("Russian")
        self.owner_russian_language_checkbox.setStyleSheet("""
            QCheckBox {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0FFFF;
                border: none;
                padding: 5px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 8px; 
                border: 2px solid #3F00FF;
                background-color: #F0FFFF;
            }
            QCheckBox::indicator:checked {
                background-color: #3F00FF;
                border: 2px solid #3F00FF; 
            }
        """)
        self.owner_russian_language_checkbox.setChecked(True)
        self.owner_english_language_checkbox = QCheckBox("English")
        self.owner_english_language_checkbox.setStyleSheet("""
            QCheckBox {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0FFFF;
                border: none;
                padding: 5px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                border: 2px solid #3F00FF;
                background-color: #F0FFFF;
            }
            QCheckBox::indicator:checked {
                background-color: #3F00FF;
                border: 2px solid #3F00FF; 
            }
        """)

        self.owner_russian_language_checkbox.stateChanged.connect(self.on_owner_russian_language_checkbox_changed)
        self.owner_english_language_checkbox.stateChanged.connect(self.on_owner_english_language_checkbox_changed)

        self.owner_language_layout.addWidget(self.owner_russian_language_checkbox)
        self.owner_language_layout.addWidget(self.owner_english_language_checkbox)

        layout.addLayout(self.owner_language_layout)


        separator = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(separator)

        self.bottom_layout = QHBoxLayout()
        # Кнопка для сохранения настроек
        self.save_button = QPushButton("Save", self)
        self.save_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
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
        self.bottom_layout.addWidget(self.save_button)

        self.close_button = QPushButton("Close", self)
        self.close_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
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
        self.close_button.clicked.connect(self.close_menu)
        self.bottom_layout.addWidget(self.close_button)

        layout.addLayout(self.bottom_layout)
        self.setLayout(layout)

        # Настройка эффекта прозрачности
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(300)
        self.opacity_animation.setStartValue(0)
        self.opacity_animation.setEndValue(1)
        self.opacity_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.is_visible = False
        self.hide()

    def change_user_icon(self):
        # Открываем диалоговое окно для выбора файла
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select the icon", "", "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)
        
        if file_name:
            # Если файл выбран, сохраняем его в base64
            with open(file_name, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                base64_user_icons.base64_profile_icon = encoded_image
            
            # Получаем иконку и её размер, применяем закругление
            owner_icon, owner_icon_size = _get_icon_from_base64(base64_user_icons.base64_profile_icon, 100, 100)
            rounded_icon = self.make_round_icon(owner_icon.pixmap(owner_icon_size))  # Создаем круглую иконку
            self.owner_icon_selection.setIcon(rounded_icon)
            self.owner_icon_selection.setIconSize(owner_icon_size)

            owner_icon, owner_icon_size = _get_icon_from_base64(base64_user_icons.base64_profile_icon, 30, 30)
            rounded_icon = self.make_round_icon(owner_icon.pixmap(owner_icon_size))  # Создаем круглую иконку
            self.main_window.side_bar.user_label_icon.setPixmap(rounded_icon.pixmap(owner_icon_size))
            self.main_window.side_bar.user_label_icon.setFixedSize(owner_icon_size)

    def make_round_icon(self, pixmap):
        size = min(pixmap.width(), pixmap.height())
        rounded_pixmap = QPixmap(size, size)
        rounded_pixmap.fill(Qt.transparent)

        # Рисуем круглую маску
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(pixmap)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, size, size)
        painter.end()

        return QIcon(rounded_pixmap)

    def on_owner_russian_language_checkbox_changed(self, state):
        if state == Qt.Checked:
            self.owner_english_language_checkbox.setChecked(False)
            # Owner.language = 'ru'

    def on_owner_english_language_checkbox_changed(self, state):
        if state == Qt.Checked:
            self.owner_russian_language_checkbox.setChecked(False)
            # Owner.language = 'en'

    def resize_proportionally(self):
        # Пропорции виджета относительно размеров окна
        if self.main_window:
            main_window_width = self.main_window.width()
            main_window_height =  self.main_window.height()
            menu_width = int(main_window_width * self.initial_width_ratio)
            menu_height = int(main_window_height * self.initial_height_ratio)

            self.setFixedSize(menu_width, menu_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_proportionally()
    
    def showEvent(self, event):
        super().showEvent(event)
        if self.main_window:
            self.is_visible = True
            self.resize_proportionally()
            self.opacity_animation.start()
            self.main_window.side_bar_button.lower()

    def close_menu(self):
        self.opacity_animation.setDirection(QPropertyAnimation.Backward)
        self.opacity_animation.finished.connect(self.close)
        self.opacity_animation.start()
        self.overlay.opacity_animation_hide.start()
        self.overlay.hide()
        self.is_visible = False
        self.main_window.side_bar_button.stackUnder(self.main_window.side_bar)