from dataclasses import dataclass
from PyQt5.QtWidgets import ( 
    QPushButton, 
    QVBoxLayout, 
    QDialog, 
    QLineEdit, 
    QLabel, 
    QHBoxLayout,
    QCheckBox, 
    QSpacerItem,
    QSizePolicy, 
    QGraphicsOpacityEffect)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt

class SettingsMenu(QDialog):
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
            }
        """)

        self.raise_()

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Заголовок
        self.header = QLabel("Settings", self)
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

        self.assistant_name_selection = QLabel("Assistant name", self)
        self.assistant_name_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)

        layout.addWidget(self.assistant_name_selection)

        self.assistant_name_layout = QHBoxLayout()

        self.assistant_name_tayler_checkbox = QCheckBox("Tayler")
        self.assistant_name_tayler_checkbox.setStyleSheet("""
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
        self.assistant_name_tayler_checkbox.setChecked(True)

        self.assistant_name_marla_checkbox = QCheckBox("Marla")
        self.assistant_name_marla_checkbox.setStyleSheet("""
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

        self.assistant_name_marla_checkbox.stateChanged.connect(self.on_assistant_name_marla_checkbox_changed)
        self.assistant_name_tayler_checkbox.stateChanged.connect(self.on_assistant_name_tayler_checkbox_changed)

        self.assistant_name_layout.addWidget(self.assistant_name_tayler_checkbox)
        self.assistant_name_layout.addWidget(self.assistant_name_marla_checkbox)

        layout.addLayout(self.assistant_name_layout)

        self.spotify_keys_selection = QLabel("Spotify keys", self)
        self.spotify_keys_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)

        layout.addWidget(self.spotify_keys_selection)

        self.spotify_client_id = QLineEdit(self)
        self.spotify_client_id.setPlaceholderText("Spotify Client ID")
        self.spotify_client_id.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.spotify_client_id)

        self.spotify_client_secret = QLineEdit(self)
        self.spotify_client_secret.setPlaceholderText("Spotify Client Secret")
        self.spotify_client_secret.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.spotify_client_secret)

        self.spotify_redirect_uri = QLineEdit(self)
        self.spotify_redirect_uri.setPlaceholderText("Spotify Redirect Uri")
        self.spotify_redirect_uri.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                color: #3F00FF;
                background-color: #F0F8FF;
                border: 1px solid #3F00FF;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.spotify_redirect_uri)

        self.interface_language_selection = QLabel("Interface language", self)
        self.interface_language_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)

        layout.addWidget(self.interface_language_selection)

        self.interface_language_layout = QHBoxLayout()

        self.interface_russian_language_checkbox = QCheckBox("Russian")
        self.interface_russian_language_checkbox.setStyleSheet("""
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
        self.interface_english_language_checkbox = QCheckBox("English")
        self.interface_english_language_checkbox.setStyleSheet("""
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
        self.interface_english_language_checkbox.setChecked(True)

        self.interface_russian_language_checkbox.stateChanged.connect(self.on_interface_russian_language_checkbox_changed)
        self.interface_english_language_checkbox.stateChanged.connect(self.on_interface_english_language_checkbox_changed)

        self.interface_language_layout.addWidget(self.interface_russian_language_checkbox)
        self.interface_language_layout.addWidget(self.interface_english_language_checkbox)

        layout.addLayout(self.interface_language_layout)

        self.debug_mode_selection = QLabel("Debug mode", self)
        self.debug_mode_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)
        layout.addWidget(self.debug_mode_selection)

        self.caution_selection = QLabel("Caution: If you aren't a developer, don't touch checkboxes below", self)
        self.caution_selection.setWordWrap(True)
        self.caution_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #E32636;                             
            }
        """)
        layout.addWidget(self.caution_selection)

        self.debug_mode_checkbox = QCheckBox("Enable debug mode")
        self.debug_mode_checkbox.setStyleSheet("""
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
        layout.addWidget(self.debug_mode_checkbox)

        self.logging_layout = QHBoxLayout()

        self.logging_checkbox = QCheckBox("Enable logging")
        self.logging_checkbox.setChecked(True)
        self.logging_checkbox.setStyleSheet("""
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
        self.logging_layout.addWidget(self.logging_checkbox)

        self.open_logs_button = QPushButton("Open logs", self)
        self.open_logs_button.setStyleSheet("""
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
        self.open_logs_button.clicked.connect(self.open_logs)
        self.logging_layout.addWidget(self.open_logs_button)
        layout.addLayout(self.logging_layout)

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

    def on_assistant_name_marla_checkbox_changed(self, state):
        if state == Qt.Checked:
            self.assistant_name_tayler_checkbox.setChecked(False)
            # Owner.language = 'ru'

    def on_assistant_name_tayler_checkbox_changed(self, state):
        if state == Qt.Checked:
            self.assistant_name_marla_checkbox.setChecked(False)
            # Owner.language = 'en'

    def on_interface_russian_language_checkbox_changed(self, state):
        if state == Qt.Checked:
            self.interface_english_language_checkbox.setChecked(False)
            # Inerface.language = 'ru'

    def on_interface_english_language_checkbox_changed(self, state):
        if state == Qt.Checked:
            self.interface_russian_language_checkbox.setChecked(False)
            # Interface.language = 'en'

    def open_logs(self):
        pass

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