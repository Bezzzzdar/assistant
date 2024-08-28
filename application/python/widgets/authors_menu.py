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

class AuthorsMenu(QDialog):
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
        self.header = QLabel("Authors", self)
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
        
        self.Bezzzzdar_github_url = "https://github.com/Bezzzzdar"
        self.Chessman2003_github_url = "https://github.com/Chessman2003"
        self.poperskop_github_url = "https://github.com/poperskop"

        self.text_description = f"""
            • Ivan Rastegaev (aka <a href="{self.Bezzzzdar_github_url}">Bezzzzdar</a>) - main developer, QA, project manager.<br>
            <br>
            • Pavel Golubtsov (aka <a href="{self.Chessman2003_github_url}">Chessman2003</a>) - web developer.<br>
            <br>
            • Alexander Shestopyorov (aka <a href="{self.poperskop_github_url}">poperskop</a>) - developer of neurolinguistic processing tools.<br>
        """
        self.text_description_selection = QLabel(self)
        self.text_description_selection.setWordWrap(True)
        self.text_description_selection.setText(self.text_description)
        self.text_description_selection.setOpenExternalLinks(True)
        self.text_description_selection.setTextFormat(Qt.RichText)
        self.text_description_selection.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #3F00FF;                             
            }
        """)
        layout.addWidget(self.text_description_selection)

        separator = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(separator)

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
        layout.addWidget(self.close_button)
        
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