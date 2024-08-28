import sys
from dataclasses import dataclass
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton,  
    QWidget, 
    QHBoxLayout, 
    QGraphicsOpacityEffect,
    QStackedWidget)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, Qt
from PyQt5.QtGui import QPainter, QBrush, QColor

from modules.icons import base64_const_icons, _get_icon_from_base64
from widgets.side_bar import SideBar
from widgets.chat_box import ChatBox

class Overlay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setStyleSheet("background-color: black;")  # Полупрозрачный черный цвет

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Настройка эффекта прозрачности
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation_show = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation_show.setDuration(300)
        self.opacity_animation_show.setStartValue(0)
        self.opacity_animation_show.setEndValue(1)
        self.opacity_animation_show.setEasingCurve(QEasingCurve.InOutQuad)

        self.opacity_animation_hide = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation_hide.setDuration(300)
        self.opacity_animation_hide.setStartValue(1)
        self.opacity_animation_hide.setEndValue(0)
        self.opacity_animation_hide.setEasingCurve(QEasingCurve.InOutQuad)

        self.setGeometry(parent.rect())
        self.hide()

    def show(self):
        self.setGeometry(self.parent().rect())
        super().show()

    def resizeEvent(self, event):
        self.setGeometry(self.parent().rect())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(0, 0, 0, 150))  # Полупрозрачный черный цвет
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistant")
        self.setGeometry(450, 200, 1100, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0FFFF;
            }
        """)
        self.setMinimumSize(1100, 700)

        # Создаем оверлей
        self.overlay = Overlay(self)

        # Set the center widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        # Icon in base64 code
        self.side_bar_icon, self.side_bar_icon_size = _get_icon_from_base64(base64_const_icons.base64_side_bar_icon, 35, 35)
        self.side_bar_icon_hover,  self.side_bar_icon_hover_size = _get_icon_from_base64(base64_const_icons.base64_side_bar_hover_icon, 35, 35)

        # Create a side menu button and set an icon
        self.side_bar_button = QPushButton("", self)
        self.side_bar_button.setIcon(self.side_bar_icon)
        self.side_bar_button.setIconSize(self.side_bar_icon_size)
        self.side_bar_button.setGeometry(0, 0, 35, 35)  

        # Set the styles for the side menu button
        self.side_bar_button.setStyleSheet("""
            QPushButton {
                background-color: #F0FFFF; 
                border: none;
            }
        """)

        # Connect the button press signal
        self.side_bar_button.clicked.connect(self.toggle_side_bar)
        self.side_bar_button.enterEvent = self.on_enter_side_bar_button
        self.side_bar_button.leaveEvent = self.on_leave_side_bar_button

        # Initializing the side menu
        self.side_bar = SideBar(overlay=self.overlay, parent=self)
        self.side_bar.setGeometry(-self.side_bar.width(), 0, self.side_bar.width(), self.side_bar.height())
        self.side_bar_hidden_position = QPoint(-self.side_bar.width(), 0)
        self.side_bar_visible_position = QPoint(0, 0)

        self.chat_box = ChatBox()
        self.layout.addWidget(self.chat_box)
        self.chat_box.stackUnder(self.overlay)
        self.overlay.hide()

    def on_enter_side_bar_button(self, event):
        # Меняем иконку при наведении курсора
        self.side_bar_button.setIcon(self.side_bar_icon_hover)
        event.accept()

    def on_leave_side_bar_button(self, event):
        # Возвращаем исходную иконку, когда курсор уходит
        self.side_bar_button.setIcon(self.side_bar_icon)
        event.accept()
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the side menu to match the height of the main window
        if self.side_bar.is_visible:
            self.side_bar.setFixedSize(self.side_bar.width(), self.height())
        if self.side_bar.account_menu.is_visible:
            self.side_bar.account_menu.resize_proportionally()
        if self.side_bar.settings_menu.is_visible:
            self.side_bar.settings_menu.resize_proportionally()
        if self.side_bar.authors_menu.is_visible:
            self.side_bar.authors_menu.resize_proportionally()
        if self.side_bar.about_app_menu.is_visible:
            self.side_bar.about_app_menu.resize_proportionally()
        if self.overlay:
            self.overlay.resize(self.size())

    def toggle_side_bar(self):
        if not self.side_bar.is_visible:
            self.chat_box.setDisabled(True)
            self.overlay.opacity_animation_show.start()
            self.overlay.show()
            self.overlay.stackUnder(self.side_bar)
            self.side_bar.slide_in(self.side_bar_hidden_position, self.side_bar_visible_position)
            self.side_bar.is_visible = True
        else:
            self.chat_box.setDisabled(False)
            self.side_bar.slide_out(self.side_bar_hidden_position)
            self.side_bar.is_visible = False
            self.overlay.opacity_animation_hide.start()
            self.overlay.hide()

    def mousePressEvent(self, event):
        # Check if the click was outside of the side menu
        if self.side_bar.is_visible and not self.side_bar.geometry().contains(self.mapFromGlobal(event.globalPos())):
            self.toggle_side_bar()
        if self.side_bar.account_menu.is_visible and not self.side_bar.account_menu.geometry().contains(self.mapFromGlobal(event.globalPos())):
            self.side_bar.account_menu.close_menu()
            self.side_bar.account_menu.is_visible = False
        if self.side_bar.settings_menu.is_visible and not self.side_bar.settings_menu.geometry().contains(self.mapFromGlobal(event.globalPos())):
            self.side_bar.settings_menu.close_menu()
            self.side_bar.settings_menu.is_visible = False
        if self.side_bar.authors_menu.is_visible and not self.side_bar.authors_menu.geometry().contains(self.mapFromGlobal(event.globalPos())):
            self.side_bar.authors_menu.close_menu()
            self.side_bar.authors_menu.is_visible = False
        if self.side_bar.about_app_menu.is_visible and not self.side_bar.about_app_menu.geometry().contains(self.mapFromGlobal(event.globalPos())):
            self.side_bar.about_app_menu.close_menu()
            self.side_bar.about_app_menu.is_visible = False
        super().mousePressEvent(event)

    # def keyPressEvent(self, event):
    #     # Hide menu if Esc key is pressed
    #     if event.key() == Qt.Key_Escape and global_parametrs.side_bar_visible:
    #         self.toggle_side_bar()
    #     if event.key() == Qt.Key_Escape and global_parametrs.account_menu_visible:
    #         self.side_bar.account_menu.close_menu()
    #         self.overlay.opacity_animation_hide.start()
    #         self.overlay.hide()
    #         global_parametrs.account_menu_visible = False
    #     super().keyPressEvent(event)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())