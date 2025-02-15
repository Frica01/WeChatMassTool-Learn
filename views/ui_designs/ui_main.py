# -*- coding: utf-8 -*-


from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QProgressBar, QPushButton, QRadioButton, QSizePolicy, QStackedWidget, QTextEdit,
                               QVBoxLayout, QWidget)

from .resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(
            u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "\n"
            "SET APP STYLESHEET - FULL STYLES HERE\n"
            "DARK THEME - DRACULA COLOR BASED\n"
            "\n"
            "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
            "\n"
            "QWidget{\n"
            "	color: rgb(221, 221, 221);\n"
            "	font: 10pt \"Microsoft YaHei UI\";\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Tooltip */\n"
            "QToolTip {\n"
            "	color: #ffffff;\n"
            "	background-color: rgba(33, 37, 43, 180);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	background-image: none;\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 2px solid rgb(255, 121, 198);\n"
            "	text-align: left;\n"
            "	padding-left: 8px;\n"
            "	margin: 0px;\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Bg App */\n"
            "#bgApp {	\n"
            "	"
            "background-color: rgb(40, 44, 52);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Left Menu */\n"
            "#frame_menu_left_box {	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#frame_logo {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	background-image: url(:/images/images/WeChatMass.png);\n"
            "	background-position: centered;\n"
            "	background-repeat: no-repeat;\n"
            "}\n"
            "#label_subtitle { font: 63 12pt \"Segoe UI Semibold\"; }\n"
            "#label_subtitle_description { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
            "\n"
            "/* MENUS */\n"
            "#frame_menu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color: transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#frame_menu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#frame_menu .QPushButton:pressed"
            " {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#frame_left_bottom .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#frame_left_bottom .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#frame_left_bottom .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#frame_left_sub_box{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Toggle Button */\n"
            "#btn_menu_toggle {\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color: rgb(37, 41, 48);\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "	color: rgb(113, 126, 149);\n"
            "}\n"
            "#btn_menu_toggle:hover {\n"
            "	background-color: rgb(40, 44, 5"
            "2);\n"
            "}\n"
            "#btn_menu_toggle:pressed {\n"
            "	background-color: rgb(189, 147, 249);\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#label_title { padding-left: 10px; }\n"
            "\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Extra Tab */\n"
            "#frame_left_settings_box {	\n"
            "	background-color: rgb(44, 49, 58);\n"
            "}\n"
            "#frame_left_settings_title_box{	\n"
            "	background-color: rgb(189, 147, 249)\n"
            "}\n"
            "\n"
            "/* Icon */\n"
            "#frame_left_settings_icon {\n"
            "	background-position: center;\n"
            "	background-repeat: no-repeat;\n"
            "	background-image: url(:/icons/icons/icon_settings.png);\n"
            "}\n"
            "\n"
            "/* Label */\n"
            "#label_left_settings { color: rgb(255, 255, 255); }\n"
            "\n"
            "/* Btn Close */\n"
            "#btn_close_left_settings { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#btn_close_left_settings:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
            "#btn_close_left_settings:pressed { background-color"
            ": rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Extra Content */\n"
            "#frame_left_settings_content{\n"
            "	border-top: 3px solid rgb(40, 44, 52);\n"
            "}\n"
            "\n"
            "/* Extra Top Menus */\n"
            "#frame_left_settings_top_box .QPushButton {\n"
            "background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	/*border-left: 22px solid transparent;*/\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	/*padding-left: 44px;*/\n"
            "}\n"
            "#frame_left_settings_top_box .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#frame_left_settings_top_box .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Content App */\n"
            "#frame_content_top_box{	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#frame_sub_content_box{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* To"
            "p Buttons */\n"
            "#frame_buttons_top_right .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#frame_buttons_top_right .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#frame_buttons_top_right .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Theme Settings */\n"
            "#frame_right_settings_box { background-color: rgb(44, 49, 58); }\n"
            "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
            "\n"
            "/* Bottom Bar */\n"
            "#frame_bottom_bar { background-color: rgb(44, 49, 58); }\n"
            "#frame_bottom_bar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "/* CONTENT SETTINGS */\n"
            "/* MENUS */\n"
            "#frame_right_settings_content .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            ""
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#frame_right_settings_content .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#frame_right_settings_content .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "LineEdit */\n"
            "QLineEdit {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding-left: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "QTextEdit */\n"
            "QTextEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	b"
            "order-radius: 5px;\n"
            "	padding: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QTextEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QTextEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "	border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "	border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-right-radius: 4px;\n"
            "    border-bottom-right-radi"
            "us: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "	border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 4px;\n"
            ""
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    bac"
            "kground: 3px solid rgb(52, 59, 72);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "	background-image: url(:/icons/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "RadioButton */\n"
            "QRadioButton::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ComboBox */\n"
            "QComboBox{\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88"
            ");\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "	subcontrol-origin: padding;\n"
            "	subcontrol-position: top right;\n"
            "	width: 25px; \n"
            "	border-left-width: 3px;\n"
            "	border-left-color: rgba(39, 44, 54, 150);\n"
            "	border-left-style: solid;\n"
            "	border-top-right-radius: 3px;\n"
            "	border-bottom-right-radius: 3px;	\n"
            "	background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "	color: rgb(255, 121, 198);	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	padding: 10px;\n"
            "	selection-background-color: rgb(39, 44, 54);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Sliders */\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius: 5px;\n"
            "    height: 10px;\n"
            "	margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:horizontal:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            " "
            "   background-color: rgb(189, 147, 249);\n"
            "    border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:horizontal:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "QSlider::groove:vertical {\n"
            "    border-radius: 5px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:vertical:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:vertical {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "	border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:vertical:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:vertical:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////"
            "////////////////////////////////\n"
            "Button */\n"
            "#frame_pages_container QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "#frame_pages_container QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "#frame_pages_container QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
            "")
        self.app_margins = QVBoxLayout(self.styleSheet)
        self.app_margins.setSpacing(0)
        self.app_margins.setObjectName(u"app_margins")
        self.app_margins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_left_box = QFrame(self.bgApp)
        self.frame_menu_left_box.setObjectName(u"frame_menu_left_box")
        self.frame_menu_left_box.setMinimumSize(QSize(60, 0))
        self.frame_menu_left_box.setMaximumSize(QSize(60, 16777215))
        self.frame_menu_left_box.setFrameShape(QFrame.NoFrame)
        self.frame_menu_left_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu_left_box)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title_box = QFrame(self.frame_menu_left_box)
        self.frame_title_box.setObjectName(u"frame_title_box")
        self.frame_title_box.setMinimumSize(QSize(0, 50))
        self.frame_title_box.setMaximumSize(QSize(16777215, 50))
        self.frame_title_box.setFrameShape(QFrame.NoFrame)
        self.frame_title_box.setFrameShadow(QFrame.Raised)
        self.frame_logo = QFrame(self.frame_title_box)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setGeometry(QRect(10, 5, 42, 42))
        self.frame_logo.setMinimumSize(QSize(42, 42))
        self.frame_logo.setMaximumSize(QSize(42, 42))
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.label_subtitle = QLabel(self.frame_title_box)
        self.label_subtitle.setObjectName(u"label_subtitle")
        self.label_subtitle.setGeometry(QRect(70, 8, 160, 20))
        self.label_subtitle.setStyleSheet(u"")
        self.label_subtitle.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_subtitle_description = QLabel(self.frame_title_box)
        self.label_subtitle_description.setObjectName(u"label_subtitle_description")
        self.label_subtitle_description.setGeometry(QRect(70, 27, 160, 16))
        self.label_subtitle_description.setMaximumSize(QSize(16777215, 16))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_subtitle_description.setFont(font1)
        self.label_subtitle_description.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.label_subtitle_description.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.frame_title_box)

        self.frame_left_sub_box = QFrame(self.frame_menu_left_box)
        self.frame_left_sub_box.setObjectName(u"frame_left_sub_box")
        self.frame_left_sub_box.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        self.frame_left_sub_box.setFrameShape(QFrame.NoFrame)
        self.frame_left_sub_box.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.frame_left_sub_box)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_toggle = QFrame(self.frame_left_sub_box)
        self.frame_menu_toggle.setObjectName(u"frame_menu_toggle")
        self.frame_menu_toggle.setMaximumSize(QSize(16777215, 45))
        self.frame_menu_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_menu_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_menu_toggle)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_toggle = QPushButton(self.frame_menu_toggle)
        self.btn_menu_toggle.setObjectName(u"btn_menu_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu_toggle.sizePolicy().hasHeightForWidth())
        self.btn_menu_toggle.setSizePolicy(sizePolicy)
        self.btn_menu_toggle.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_menu_toggle.setFont(font2)
        self.btn_menu_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_toggle.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_toggle.setStyleSheet(u"background-image: url(:/icons/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.btn_menu_toggle)

        self.verticalMenuLayout.addWidget(self.frame_menu_toggle)

        self.frame_menu = QFrame(self.frame_left_sub_box)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setStyleSheet(u"")
        self.frame_menu.setFrameShape(QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_page_home = QPushButton(self.frame_menu)
        self.btn_page_home.setObjectName(u"btn_page_home")
        sizePolicy.setHeightForWidth(self.btn_page_home.sizePolicy().hasHeightForWidth())
        self.btn_page_home.setSizePolicy(sizePolicy)
        self.btn_page_home.setMinimumSize(QSize(0, 45))
        self.btn_page_home.setFont(font2)
        self.btn_page_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_home.setStyleSheet(u"background-image: url(:/icons/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_page_home)

        self.btn_page_pending = QPushButton(self.frame_menu)
        self.btn_page_pending.setObjectName(u"btn_page_pending")
        self.btn_page_pending.setMinimumSize(QSize(0, 45))
        self.btn_page_pending.setFont(font2)
        self.btn_page_pending.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_pending.setStyleSheet(u"background-image: url(:/icons/icons/friend.png);")

        self.verticalLayout_8.addWidget(self.btn_page_pending)

        self.btn_page_msg = QPushButton(self.frame_menu)
        self.btn_page_msg.setObjectName(u"btn_page_msg")
        sizePolicy.setHeightForWidth(self.btn_page_msg.sizePolicy().hasHeightForWidth())
        self.btn_page_msg.setSizePolicy(sizePolicy)
        self.btn_page_msg.setMinimumSize(QSize(0, 45))
        self.btn_page_msg.setFont(font2)
        self.btn_page_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_msg.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_msg.setStyleSheet(u"background-image: url(:/icons/icons/cli-msg.png);")

        self.verticalLayout_8.addWidget(self.btn_page_msg)

        self.verticalMenuLayout.addWidget(self.frame_menu, 0, Qt.AlignTop)

        self.frame_left_bottom = QFrame(self.frame_left_sub_box)
        self.frame_left_bottom.setObjectName(u"frame_left_bottom")
        self.frame_left_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_left_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_left_bottom)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_theme = QPushButton(self.frame_left_bottom)
        self.btn_toggle_theme.setObjectName(u"btn_toggle_theme")
        sizePolicy.setHeightForWidth(self.btn_toggle_theme.sizePolicy().hasHeightForWidth())
        self.btn_toggle_theme.setSizePolicy(sizePolicy)
        self.btn_toggle_theme.setMinimumSize(QSize(0, 45))
        self.btn_toggle_theme.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle_theme.setStyleSheet(u"background-image: url(:/icons/icons/cli-switch-theme-1.png);")
        self.btn_toggle_theme.setCheckable(False)

        self.verticalLayout_9.addWidget(self.btn_toggle_theme)

        self.btn_left_settings = QPushButton(self.frame_left_bottom)
        self.btn_left_settings.setObjectName(u"btn_left_settings")
        sizePolicy.setHeightForWidth(self.btn_left_settings.sizePolicy().hasHeightForWidth())
        self.btn_left_settings.setSizePolicy(sizePolicy)
        self.btn_left_settings.setMinimumSize(QSize(0, 45))
        self.btn_left_settings.setFont(font2)
        self.btn_left_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_left_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_left_settings.setStyleSheet(u"background-image: url(:/icons/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.btn_left_settings)

        self.verticalMenuLayout.addWidget(self.frame_left_bottom, 0, Qt.AlignBottom)

        self.verticalLayout_3.addWidget(self.frame_left_sub_box)

        self.appLayout.addWidget(self.frame_menu_left_box)

        self.frame_left_settings_box = QFrame(self.bgApp)
        self.frame_left_settings_box.setObjectName(u"frame_left_settings_box")
        self.frame_left_settings_box.setMinimumSize(QSize(0, 0))
        self.frame_left_settings_box.setMaximumSize(QSize(0, 16777215))
        self.frame_left_settings_box.setFrameShape(QFrame.NoFrame)
        self.frame_left_settings_box.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.frame_left_settings_box)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_left_settings_title_box = QFrame(self.frame_left_settings_box)
        self.frame_left_settings_title_box.setObjectName(u"frame_left_settings_title_box")
        self.frame_left_settings_title_box.setMinimumSize(QSize(0, 50))
        self.frame_left_settings_title_box.setMaximumSize(QSize(16777215, 50))
        self.frame_left_settings_title_box.setFrameShape(QFrame.NoFrame)
        self.frame_left_settings_title_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_settings_title_box)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.layout_left_settings_subtitle = QGridLayout()
        self.layout_left_settings_subtitle.setObjectName(u"layout_left_settings_subtitle")
        self.layout_left_settings_subtitle.setHorizontalSpacing(10)
        self.layout_left_settings_subtitle.setVerticalSpacing(0)
        self.layout_left_settings_subtitle.setContentsMargins(10, -1, 10, -1)
        self.frame_left_settings_icon = QFrame(self.frame_left_settings_title_box)
        self.frame_left_settings_icon.setObjectName(u"frame_left_settings_icon")
        self.frame_left_settings_icon.setMinimumSize(QSize(20, 0))
        self.frame_left_settings_icon.setMaximumSize(QSize(20, 20))
        self.frame_left_settings_icon.setFrameShape(QFrame.NoFrame)
        self.frame_left_settings_icon.setFrameShadow(QFrame.Raised)

        self.layout_left_settings_subtitle.addWidget(self.frame_left_settings_icon, 0, 0, 1, 1)

        self.label_left_settings = QLabel(self.frame_left_settings_title_box)
        self.label_left_settings.setObjectName(u"label_left_settings")
        self.label_left_settings.setMinimumSize(QSize(150, 0))

        self.layout_left_settings_subtitle.addWidget(self.label_left_settings, 0, 1, 1, 1)

        self.btn_close_left_settings = QPushButton(self.frame_left_settings_title_box)
        self.btn_close_left_settings.setObjectName(u"btn_close_left_settings")
        self.btn_close_left_settings.setMinimumSize(QSize(28, 28))
        self.btn_close_left_settings.setMaximumSize(QSize(28, 28))
        self.btn_close_left_settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_left_settings.setIcon(icon)
        self.btn_close_left_settings.setIconSize(QSize(20, 20))

        self.layout_left_settings_subtitle.addWidget(self.btn_close_left_settings, 0, 2, 1, 1)

        self.verticalLayout_5.addLayout(self.layout_left_settings_subtitle)

        self.extraColumLayout.addWidget(self.frame_left_settings_title_box)

        self.frame_left_settings_content = QFrame(self.frame_left_settings_box)
        self.frame_left_settings_content.setObjectName(u"frame_left_settings_content")
        self.frame_left_settings_content.setFrameShape(QFrame.NoFrame)
        self.frame_left_settings_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_left_settings_content)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_left_settings_top_box = QFrame(self.frame_left_settings_content)
        self.frame_left_settings_top_box.setObjectName(u"frame_left_settings_top_box")
        self.frame_left_settings_top_box.setStyleSheet(u"font: 450 11pt\"Segoe UI\";\n"
                                                       "")
        self.frame_left_settings_top_box.setFrameShape(QFrame.NoFrame)
        self.frame_left_settings_top_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_left_settings_top_box)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 6, -1, 6)
        self.frame_9 = QFrame(self.frame_left_settings_top_box)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_17.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.cb_text_interval = QComboBox(self.frame_9)
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.setObjectName(u"cb_text_interval")
        self.cb_text_interval.setMinimumSize(QSize(120, 0))
        self.cb_text_interval.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.cb_text_interval, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_9, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.frame_left_settings_top_box)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.cb_file_interval = QComboBox(self.frame_4)
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.setObjectName(u"cb_file_interval")
        self.cb_file_interval.setMinimumSize(QSize(120, 0))
        self.cb_file_interval.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.cb_file_interval, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_15 = QFrame(self.frame_left_settings_top_box)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 40))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.radio_btn_animate_true = QRadioButton(self.frame_15)
        self.radio_btn_animate_true.setObjectName(u"radio_btn_animate_true")
        self.radio_btn_animate_true.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio_btn_animate_true.setChecked(True)

        self.horizontalLayout_11.addWidget(self.radio_btn_animate_true)

        self.radio_btn_animate_false = QRadioButton(self.frame_15)
        self.radio_btn_animate_false.setObjectName(u"radio_btn_animate_false")
        self.radio_btn_animate_false.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.radio_btn_animate_false)

        self.verticalLayout_11.addWidget(self.frame_15, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.frame_left_settings_top_box)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_15.addWidget(self.label_2)

        self.import_name_list_line_edit = QLineEdit(self.frame_5)
        self.import_name_list_line_edit.setObjectName(u"import_name_list_line_edit")
        self.import_name_list_line_edit.setMinimumSize(QSize(175, 0))
        self.import_name_list_line_edit.setMaximumSize(QSize(260, 16777215))
        self.import_name_list_line_edit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.import_name_list_line_edit)

        self.btn_import_name_list = QPushButton(self.frame_5)
        self.btn_import_name_list.setObjectName(u"btn_import_name_list")
        self.btn_import_name_list.setMinimumSize(QSize(60, 0))
        self.btn_import_name_list.setMaximumSize(QSize(80, 16777215))
        self.btn_import_name_list.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_import_name_list.setIcon(icon1)
        self.btn_import_name_list.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.btn_import_name_list, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_16 = QFrame(self.frame_left_settings_top_box)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.export_tag_name_list_line_edit = QLineEdit(self.frame_16)
        self.export_tag_name_list_line_edit.setObjectName(u"export_tag_name_list_line_edit")
        self.export_tag_name_list_line_edit.setMinimumSize(QSize(175, 0))

        self.horizontalLayout_12.addWidget(self.export_tag_name_list_line_edit)

        self.btn_export_name_list = QPushButton(self.frame_16)
        self.btn_export_name_list.setObjectName(u"btn_export_name_list")
        self.btn_export_name_list.setMinimumSize(QSize(60, 0))
        self.btn_export_name_list.setMaximumSize(QSize(80, 16777215))
        self.btn_export_name_list.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_name_list.setIcon(icon2)
        self.btn_export_name_list.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.btn_export_name_list)

        self.verticalLayout_11.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.verticalLayout_12.addWidget(self.frame_left_settings_top_box)

        self.frame_left_settings_bottom_box = QFrame(self.frame_left_settings_content)
        self.frame_left_settings_bottom_box.setObjectName(u"frame_left_settings_bottom_box")
        self.frame_left_settings_bottom_box.setFrameShape(QFrame.NoFrame)
        self.frame_left_settings_bottom_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_left_settings_bottom_box)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.frame_left_settings_bottom_box)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)

        self.verticalLayout_12.addWidget(self.frame_left_settings_bottom_box)

        self.extraColumLayout.addWidget(self.frame_left_settings_content)

        self.appLayout.addWidget(self.frame_left_settings_box)

        self.frame_content_box = QFrame(self.bgApp)
        self.frame_content_box.setObjectName(u"frame_content_box")
        self.frame_content_box.setFrameShape(QFrame.NoFrame)
        self.frame_content_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_content_box)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_content_top_box = QFrame(self.frame_content_box)
        self.frame_content_top_box.setObjectName(u"frame_content_top_box")
        self.frame_content_top_box.setMinimumSize(QSize(0, 50))
        self.frame_content_top_box.setMaximumSize(QSize(16777215, 50))
        self.frame_content_top_box.setFrameShape(QFrame.NoFrame)
        self.frame_content_top_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_content_top_box)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.frame_title = QFrame(self.frame_content_top_box)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy1)
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy2)
        self.label_title.setMaximumSize(QSize(16777215, 45))
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_title)

        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_buttons_top_right = QFrame(self.frame_content_top_box)
        self.frame_buttons_top_right.setObjectName(u"frame_buttons_top_right")
        self.frame_buttons_top_right.setMinimumSize(QSize(0, 28))
        self.frame_buttons_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_buttons_top_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_buttons_top_right)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_top_settings = QPushButton(self.frame_buttons_top_right)
        self.btn_top_settings.setObjectName(u"btn_top_settings")
        self.btn_top_settings.setMinimumSize(QSize(28, 28))
        self.btn_top_settings.setMaximumSize(QSize(28, 28))
        self.btn_top_settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_top_settings.setIcon(icon3)
        self.btn_top_settings.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_top_settings)

        self.btn_minimize = QPushButton(self.frame_buttons_top_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(28, 28))
        self.btn_minimize.setMaximumSize(QSize(28, 28))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon4)
        self.btn_minimize.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize_and_restore = QPushButton(self.frame_buttons_top_right)
        self.btn_maximize_and_restore.setObjectName(u"btn_maximize_and_restore")
        self.btn_maximize_and_restore.setMinimumSize(QSize(28, 28))
        self.btn_maximize_and_restore.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.btn_maximize_and_restore.setFont(font3)
        self.btn_maximize_and_restore.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_and_restore.setIcon(icon5)
        self.btn_maximize_and_restore.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_maximize_and_restore)

        self.btn_close = QPushButton(self.frame_buttons_top_right)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_close)

        self.horizontalLayout.addWidget(self.frame_buttons_top_right, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_content_top_box)

        self.frame_sub_content_box = QFrame(self.frame_content_box)
        self.frame_sub_content_box.setObjectName(u"frame_sub_content_box")
        self.frame_sub_content_box.setFrameShape(QFrame.NoFrame)
        self.frame_sub_content_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_sub_content_box)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_pages_content = QFrame(self.frame_sub_content_box)
        self.frame_pages_content.setObjectName(u"frame_pages_content")
        self.frame_pages_content.setFrameShape(QFrame.NoFrame)
        self.frame_pages_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_pages_content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_pages_container = QFrame(self.frame_pages_content)
        self.frame_pages_container.setObjectName(u"frame_pages_container")
        self.frame_pages_container.setStyleSheet(u"")
        self.frame_pages_container.setFrameShape(QFrame.NoFrame)
        self.frame_pages_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_pages_container)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stacked_widget = QStackedWidget(self.frame_pages_container)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setStyleSheet(u"background: transparent;\n"
                                          "")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/PyDracula_vertical.png);\n"
                                "background-position: center;\n"
                                "background-repeat: no-repeat;\n"
                                "background-image: url(:/images/images/WeChatMass_vertical.png);")
        self.stacked_widget.addWidget(self.home)
        self.page_friend = QWidget()
        self.page_friend.setObjectName(u"page_friend")
        self.gridLayout = QGridLayout(self.page_friend)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_14 = QFrame(self.page_friend)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 28pt \"Microsoft YaHei UI\";\n"
                                 "color: rgb(85, 255, 127);")

        self.horizontalLayout_9.addWidget(self.label, 0, Qt.AlignHCenter)

        self.gridLayout.addWidget(self.frame_14, 0, 0, 1, 1)

        self.stacked_widget.addWidget(self.page_friend)
        self.wechat = QWidget()
        self.wechat.setObjectName(u"wechat")
        self.wechat.setStyleSheet(
            u"QFrame #frame_sub_1, QFrame#frame_sub_2, QFrame#frame_sub_3, QFrame#frame_sub_4 {border: 2px solid #5D535E; border-radius: 6px;}\n"
            "QTextEdit {background-color: rgb(27, 29, 35); font: 12pt \"Microsoft YaHei UI\";}")
        self.verticalLayout_21 = QVBoxLayout(self.wechat)
        self.verticalLayout_21.setSpacing(3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_sub_1 = QFrame(self.wechat)
        self.frame_sub_1.setObjectName(u"frame_sub_1")
        self.frame_sub_1.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_sub_1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_sub_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(4, 4, 4, 3)
        self.single_line_msg_text_edit = QTextEdit(self.frame_6)
        self.single_line_msg_text_edit.setObjectName(u"single_line_msg_text_edit")
        self.single_line_msg_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.single_line_msg_text_edit.setStyleSheet(u"")
        self.single_line_msg_text_edit.setTabStopDistance(40.000000000000000)

        self.horizontalLayout_7.addWidget(self.single_line_msg_text_edit)

        self.multi_line_msg_text_edit = QTextEdit(self.frame_6)
        self.multi_line_msg_text_edit.setObjectName(u"multi_line_msg_text_edit")
        self.multi_line_msg_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.multi_line_msg_text_edit.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.multi_line_msg_text_edit)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_sub_1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"font: 500 12pt \"Segoe UI\"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_clear_msg = QPushButton(self.frame_7)
        self.btn_clear_msg.setObjectName(u"btn_clear_msg")
        self.btn_clear_msg.setMinimumSize(QSize(150, 30))
        self.btn_clear_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_msg.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_msg.setIcon(icon6)

        self.gridLayout_4.addWidget(self.btn_clear_msg, 0, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalLayout_6.addWidget(self.frame_7)

        self.verticalLayout_21.addWidget(self.frame_sub_1)

        self.frame_sub_2 = QFrame(self.wechat)
        self.frame_sub_2.setObjectName(u"frame_sub_2")
        self.frame_sub_2.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_sub_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_sub_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QListWidget {\n"
                                    "    background-color: rgb(27, 29, 35);\n"
                                    "    border-radius: 5px;\n"
                                    "    padding: 3px;\n"
                                    "    border: 1px solid rgb(45, 45, 58);\n"
                                    "	font: 12pt \"Microsoft YaHei UI\";\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget::item {padding: 3px;}\n"
                                    "\n"
                                    "QListWidget QScrollBar:vertical {\n"
                                    "    border: none;\n"
                                    "    background: rgb(52, 59, 72);\n"
                                    "    width: 8px;\n"
                                    "    margin: 21px 0 21px 0;\n"
                                    "    border-radius: 0px;\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget QScrollBar::handle:vertical {background: rgb(189, 147, 249);min-height: 25px;border-radius: 4px;}\n"
                                    "\n"
                                    "QListWidget QScrollBar::add-line:vertical {\n"
                                    "    border: none;\n"
                                    "    background: rgb(55, 63, 77);\n"
                                    "    height: 20px;\n"
                                    "	border-bottom-left-radius: 4px;\n"
                                    "    border-bottom-right-radius: 4px;\n"
                                    "    subcontrol-position: bottom;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget QScrollBar::sub-line:vertical {\n"
                                    "	border: none;\n"
                                    "    background: rgb(55, 63, 77);\n"
                                    "    height: 20px;\n"
                                    "	border-top-left-radius: 4px;\n"
                                    "    border-top-right-"
                                    "radius: 4px;\n"
                                    "    subcontrol-position: top;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget QScrollBar::up-arrow:vertical, QListWidget QScrollBar::down-arrow:vertical {background: none;}\n"
                                    "\n"
                                    "QListWidget QScrollBar::add-page:vertical, QListWidget QScrollBar::sub-page:vertical {background: none;}\n"
                                    "\n"
                                    "QMenu {\n"
                                    "    background-color: rgb(37, 39, 48); /* \u83dc\u5355\u80cc\u666f\u8272 */\n"
                                    "    color: rgb(220, 220, 220); /* \u83dc\u5355\u6587\u5b57\u989c\u8272 */\n"
                                    "    border: 1px solid rgb(45, 45, 58); /* \u83dc\u5355\u8fb9\u6846 */\n"
                                    "    font: 12pt \"Segoe UI\"; /* \u5b57\u4f53\u5927\u5c0f\u548c\u7c7b\u578b */\n"
                                    "}\n"
                                    "\n"
                                    "QMenu::item {background-color: transparent; padding: 5px 10px; margin: 1px 1px;}\n"
                                    "\n"
                                    "QMenu::item:selected {background-color: rgb(40, 44, 52);border-left: 2px solid rgb(255, 121, 198);}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_10)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.file_list_widget = QListWidget(self.frame_10)
        self.file_list_widget.setObjectName(u"file_list_widget")
        self.file_list_widget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.file_list_widget.setStyleSheet(u"")
        self.file_list_widget.setDragEnabled(False)

        self.gridLayout_5.addWidget(self.file_list_widget, 0, 0, 1, 1)

        self.horizontalLayout_8.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_sub_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(200, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setStyleSheet(u"font: 500 12pt \"Segoe UI\"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btn_add_file = QPushButton(self.frame_11)
        self.btn_add_file.setObjectName(u"btn_add_file")
        self.btn_add_file.setMinimumSize(QSize(150, 30))
        self.btn_add_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_file.setIcon(icon7)

        self.verticalLayout_22.addWidget(self.btn_add_file, 0, Qt.AlignHCenter)

        self.btn_clear_file = QPushButton(self.frame_11)
        self.btn_clear_file.setObjectName(u"btn_clear_file")
        self.btn_clear_file.setMinimumSize(QSize(150, 30))
        self.btn_clear_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_clear_file.setIcon(icon6)

        self.verticalLayout_22.addWidget(self.btn_clear_file, 0, Qt.AlignHCenter)

        self.horizontalLayout_8.addWidget(self.frame_11)

        self.verticalLayout_21.addWidget(self.frame_sub_2)

        self.frame_sub_3 = QFrame(self.wechat)
        self.frame_sub_3.setObjectName(u"frame_sub_3")
        self.frame_sub_3.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_sub_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_sub_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(4, 4, 4, 3)
        self.name_text_edit = QTextEdit(self.frame_12)
        self.name_text_edit.setObjectName(u"name_text_edit")
        self.name_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.name_text_edit.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.name_text_edit, 0, 0, 1, 1)

        self.horizontalLayout_10.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_sub_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setStyleSheet(u"font: 500 12pt \"Segoe UI\"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_13)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame = QFrame(self.frame_13)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(6)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 9)
        self.rb_at_everyone = QRadioButton(self.frame)
        self.rb_at_everyone.setObjectName(u"rb_at_everyone")
        self.rb_at_everyone.setMinimumSize(QSize(150, 0))
        self.rb_at_everyone.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.rb_at_everyone, 0, 0, 1, 1)

        self.verticalLayout_23.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_13)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.rb_add_remark = QRadioButton(self.frame_2)
        self.rb_add_remark.setObjectName(u"rb_add_remark")
        self.rb_add_remark.setMinimumSize(QSize(150, 0))
        self.rb_add_remark.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.rb_add_remark, 0, 0, 1, 1)

        self.verticalLayout_23.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.btn_clear_name = QPushButton(self.frame_3)
        self.btn_clear_name.setObjectName(u"btn_clear_name")
        self.btn_clear_name.setMinimumSize(QSize(150, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setWeight(QFont.Medium)
        font4.setItalic(False)
        font4.setKerning(True)
        self.btn_clear_name.setFont(font4)
        self.btn_clear_name.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_name.setAutoFillBackground(False)
        self.btn_clear_name.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_clear_name.setIcon(icon6)
        self.btn_clear_name.setAutoDefault(False)

        self.gridLayout_9.addWidget(self.btn_clear_name, 0, 0, 1, 1)

        self.verticalLayout_23.addWidget(self.frame_3)

        self.horizontalLayout_10.addWidget(self.frame_13)

        self.verticalLayout_21.addWidget(self.frame_sub_3)

        self.frame_sub_4 = QFrame(self.wechat)
        self.frame_sub_4.setObjectName(u"frame_sub_4")
        self.frame_sub_4.setStyleSheet(u"QPushButton {\n"
                                       "	border: 2px solid rgb(52, 59, 72);\n"
                                       "	font: 12pt \"Segoe UI\";\n"
                                       "	border-radius: 5px;	\n"
                                       "	background-color: rgb(52, 59, 72);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "	background-color: rgb(40, 44, 52);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "	background-color: rgb(189, 147, 249);\n"
                                       "}")
        self.frame_sub_4.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_sub_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_sub_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"font: 550 13pt \"Microsoft YaHei UI\"; color: #f8f8f2")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.task_label = QLabel(self.frame_8)
        self.task_label.setObjectName(u"task_label")
        self.task_label.setMinimumSize(QSize(120, 30))
        self.task_label.setStyleSheet(
            u"border: 1px solid rgb(52, 59, 72); border-radius: 5px; background-color: rgb(52, 59, 72);\n"
            "\n"
            "")

        self.horizontalLayout_14.addWidget(self.task_label)

        self.task_progress_bar = QProgressBar(self.frame_8)
        self.task_progress_bar.setObjectName(u"task_progress_bar")
        self.task_progress_bar.setMinimumSize(QSize(120, 30))
        self.task_progress_bar.setStyleSheet(u"QProgressBar {\n"
                                             "    border: 2px solid #333;\n"
                                             "    border-radius: 5px;\n"
                                             "	text-align: center;\n"
                                             "	background-color: #21252B;\n"
                                             "}\n"
                                             "\n"
                                             "QProgressBar::chunk {\n"
                                             "    border-radius: 3px;\n"
                                             "    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(255, 131, 208), stop:1 rgb(255, 111, 188));\n"
                                             "}\n"
                                             "")
        self.task_progress_bar.setValue(66)
        self.task_progress_bar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_14.addWidget(self.task_progress_bar, 0, Qt.AlignLeft)

        self.btn_export_result = QPushButton(self.frame_8)
        self.btn_export_result.setObjectName(u"btn_export_result")
        self.btn_export_result.setMinimumSize(QSize(120, 30))
        self.btn_export_result.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_result.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/cil-data-transfer-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_result.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.btn_export_result, 0, Qt.AlignRight)

        self.horizontalLayout_16.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.frame_20 = QFrame(self.frame_sub_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_send_msg = QPushButton(self.frame_20)
        self.btn_send_msg.setObjectName(u"btn_send_msg")
        self.btn_send_msg.setMinimumSize(QSize(120, 30))
        self.btn_send_msg.setMaximumSize(QSize(16777215, 16777215))
        self.btn_send_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_msg.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/cil-chat-bubble.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_msg.setIcon(icon9)

        self.horizontalLayout_13.addWidget(self.btn_send_msg)

        self.btn_pause_send = QPushButton(self.frame_20)
        self.btn_pause_send.setObjectName(u"btn_pause_send")
        self.btn_pause_send.setMinimumSize(QSize(120, 30))
        self.btn_pause_send.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pause_send.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pause_send.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.btn_pause_send, 0, Qt.AlignHCenter)

        self.btn_clear_all = QPushButton(self.frame_20)
        self.btn_clear_all.setObjectName(u"btn_clear_all")
        self.btn_clear_all.setMinimumSize(QSize(120, 30))
        self.btn_clear_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_all.setStyleSheet(u"")
        self.btn_clear_all.setIcon(icon6)

        self.horizontalLayout_13.addWidget(self.btn_clear_all)

        self.horizontalLayout_16.addWidget(self.frame_20, 0, Qt.AlignRight)

        self.verticalLayout_21.addWidget(self.frame_sub_4)

        self.stacked_widget.addWidget(self.wechat)

        self.verticalLayout_15.addWidget(self.stacked_widget)

        self.horizontalLayout_4.addWidget(self.frame_pages_container)

        self.frame_right_settings_box = QFrame(self.frame_pages_content)
        self.frame_right_settings_box.setObjectName(u"frame_right_settings_box")
        self.frame_right_settings_box.setMinimumSize(QSize(0, 0))
        self.frame_right_settings_box.setMaximumSize(QSize(0, 16777215))
        self.frame_right_settings_box.setFrameShape(QFrame.NoFrame)
        self.frame_right_settings_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_right_settings_box)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_right_settings_content = QFrame(self.frame_right_settings_box)
        self.frame_right_settings_content.setObjectName(u"frame_right_settings_content")
        self.frame_right_settings_content.setFrameShape(QFrame.NoFrame)
        self.frame_right_settings_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_right_settings_content)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_right_menu_box = QFrame(self.frame_right_settings_content)
        self.frame_right_menu_box.setObjectName(u"frame_right_menu_box")
        self.frame_right_menu_box.setFrameShape(QFrame.NoFrame)
        self.frame_right_menu_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_right_menu_box)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.frame_right_menu_box)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.frame_right_menu_box)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.frame_right_menu_box)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)

        self.verticalLayout_13.addWidget(self.frame_right_menu_box, 0, Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.frame_right_settings_content)

        self.horizontalLayout_4.addWidget(self.frame_right_settings_box)

        self.verticalLayout_6.addWidget(self.frame_pages_content)

        self.frame_bottom_bar = QFrame(self.frame_sub_content_box)
        self.frame_bottom_bar.setObjectName(u"frame_bottom_bar")
        self.frame_bottom_bar.setMinimumSize(QSize(0, 22))
        self.frame_bottom_bar.setMaximumSize(QSize(16777215, 22))
        self.frame_bottom_bar.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_bottom_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.frame_bottom_bar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.frame_bottom_bar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.frame_bottom_bar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        self.verticalLayout_6.addWidget(self.frame_bottom_bar)

        self.verticalLayout_2.addWidget(self.frame_sub_content_box)

        self.appLayout.addWidget(self.frame_content_box)

        self.app_margins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # if QT_CONFIG(tooltip)
        self.label_subtitle.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.label_subtitle.setText(QCoreApplication.translate("MainWindow", u"WeChatMass", None))
        self.label_subtitle_description.setText(
            QCoreApplication.translate("MainWindow", u"\u9065\u9065\u9886\u5148", None))
        self.btn_menu_toggle.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_page_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_page_pending.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.btn_page_msg.setText(QCoreApplication.translate("MainWindow", u"\u7fa4\u53d1\u6d88\u606f", None))
        # if QT_CONFIG(tooltip)
        self.btn_toggle_theme.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btn_toggle_theme.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u4e3b\u9898", None))
        self.btn_left_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_left_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9762\u677f", None))
        # if QT_CONFIG(tooltip)
        self.btn_close_left_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_close_left_settings.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6587\u672c\u95f4\u9694", None))
        self.cb_text_interval.setItemText(0, QCoreApplication.translate("MainWindow", u"0.05", None))
        self.cb_text_interval.setItemText(1, QCoreApplication.translate("MainWindow", u"0.1", None))
        self.cb_text_interval.setItemText(2, QCoreApplication.translate("MainWindow", u"0.2", None))
        self.cb_text_interval.setItemText(3, QCoreApplication.translate("MainWindow", u"0.3", None))
        self.cb_text_interval.setItemText(4, QCoreApplication.translate("MainWindow", u"0.4", None))
        self.cb_text_interval.setItemText(5, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.cb_text_interval.setItemText(6, QCoreApplication.translate("MainWindow", u"0.6", None))
        self.cb_text_interval.setItemText(7, QCoreApplication.translate("MainWindow", u"0.7", None))
        self.cb_text_interval.setItemText(8, QCoreApplication.translate("MainWindow", u"0.8", None))
        self.cb_text_interval.setItemText(9, QCoreApplication.translate("MainWindow", u"0.9", None))
        self.cb_text_interval.setItemText(10, QCoreApplication.translate("MainWindow", u"1.0", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6587\u4ef6\u95f4\u9694", None))
        self.cb_file_interval.setItemText(0, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.cb_file_interval.setItemText(1, QCoreApplication.translate("MainWindow", u"1.0", None))
        self.cb_file_interval.setItemText(2, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.cb_file_interval.setItemText(3, QCoreApplication.translate("MainWindow", u"2.0", None))
        self.cb_file_interval.setItemText(4, QCoreApplication.translate("MainWindow", u"2.5", None))
        self.cb_file_interval.setItemText(5, QCoreApplication.translate("MainWindow", u"3.0", None))
        self.cb_file_interval.setItemText(6, QCoreApplication.translate("MainWindow", u"3.5", None))
        self.cb_file_interval.setItemText(7, QCoreApplication.translate("MainWindow", u"4.0", None))
        self.cb_file_interval.setItemText(8, QCoreApplication.translate("MainWindow", u"4.5", None))
        self.cb_file_interval.setItemText(9, QCoreApplication.translate("MainWindow", u"5.0", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u52a8\u753b\u542f\u52a8", None))
        self.radio_btn_animate_true.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radio_btn_animate_false.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u597d\u53cb\u540d\u5355", None))
        self.btn_import_name_list.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u597d\u53cb\u540d\u5355", None))
        # if QT_CONFIG(tooltip)
        self.export_tag_name_list_line_edit.setToolTip(QCoreApplication.translate("MainWindow",
                                                                                  u"\u82e5\u83b7\u53d6\u5168\u90e8\u597d\u53cb\u540d\u5355\uff0c\u5219\u8f93\u5165\u5168\u90e8",
                                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.export_tag_name_list_line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u6807\u7b7e", None))
        self.btn_export_name_list.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow",
                                                         u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "hr { height: 1px; border-width: 0; }\n"
                                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                                         "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ff79c6;\">WeChatMassTool</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u57fa\u4e8ePySide6 \u548c Python \u6784\u5efa\u7684\u5fae\u4fe1\u7fa4\u53d1\u5de5\u5177\uff0c\u63d0\u4f9b\u7b80"
                                                         "\u5355\u9ad8\u6548\u7684\u7fa4\u53d1\u6d88\u606f\u529f\u80fd\u3002\u5de5\u5177\u6837\u5f0f\u57fa\u4e8e </span><span style=\" font-weight:700; color:#bd93f9;\">PyDracula</span>\u3002</p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u5982\u4f55\u83b7\u53d6</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u5173\u6ce8\u516c\u4f17\u53f7\uff1a</span><span style=\" font-weight:700; color:#bd93f9;\">\u5c0f\u83dc\u7684Python\u6742\u8d27\u94fa</span><span style=\" font-size:9pt; color:#ffffff;\"><br />\u56de\u590d\uff1a</span><span style=\" font-size:9pt; font-weight:700; color:#ff79c6;\">\u5fae\u4fe1\u7fa4\u53d1</span><span style=\" font-size:9pt; color:#ffffff;\">\uff0c\u5373\u53ef\u83b7\u53d6</span></p>\n"
                                                         ""
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u5982\u4f55\u4f7f\u7528</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u53cc\u51fb\u6b64\u5904\uff0c\u5373\u53ef\u6253\u5f00\u89c6\u9891\u6559\u7a0b</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u6280\u672f\u6808</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u4f7f\u7528 PySide6 \u8fdb\u884c UI \u5f00\u53d1\uff0cPython \u811a\u672c\u8fdb\u884c\u540e"
                                                         "\u7aef\u903b\u8f91\u5904\u7406\u3002</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u5f00\u53d1\u8005</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#bd93f9;\">\u7531\u5c0f\u83dc\u7cbe\u5fc3\u5f00\u53d1</span></p></body></html>",
                                                         None))
        self.label_title.setText(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p><span style=\"font-family:'Microsoft YaHei UI'; color:#ff79c6;\">WeChatMassTool</span> - \u57fa\u4e8ePython\u5f00\u53d1\u7684\u5fae\u4fe1\u7fa4\u53d1\u5de5\u5177.</p></body></html>",
                                                            None))
        # if QT_CONFIG(tooltip)
        self.btn_top_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_top_settings.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_maximize_and_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_maximize_and_restore.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u6b64\u9875\u9762\u5373\u5c06\u6dfb\u52a0\u670b\u53cb\u5708\u70b9\u8d5e\u529f\u80fd\u3002",
                                                      None))
        self.single_line_msg_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                     u"\u5728\u6b64\u5904\u8f93\u5165\u6d88\u606f\uff0c\u4e00\u884c\u4e3a\u4e00\u6761\u6d88\u606f",
                                                                                     None))
        self.multi_line_msg_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                    u"\u5728\u6b64\u5904\u8f93\u5165\u6d88\u606f\uff0c\u4e00\u5171\u4e3a\u4e00\u6761\u6d88\u606f",
                                                                                    None))
        self.btn_clear_msg.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u5165", None))
        self.btn_add_file.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_clear_file.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6587\u4ef6", None))
        self.name_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u5728\u6b64\u8f93\u5165\u597d\u53cb\u6635\u79f0\uff0c\u4e00\u884c\u4e3a\u4e00\u4e2a\u597d\u53cb",
                                                                          None))
        self.rb_at_everyone.setText(QCoreApplication.translate("MainWindow", u"@\u6240\u6709\u4eba", None))
        self.rb_add_remark.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5907\u6ce8", None))
        self.btn_clear_name.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u5165", None))
        self.task_label.setText(QCoreApplication.translate("MainWindow", u"\u9700\u53d1\u9001\uff1a0 \u4f4d", None))
        self.task_progress_bar.setFormat(QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210 %p%", None))
        self.btn_export_result.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u7ed3\u679c", None))
        self.btn_send_msg.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u53d1\u9001", None))
        self.btn_pause_send.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u53d1\u9001", None))
        self.btn_clear_all.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5168\u90e8", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \u5c0f\u83dc", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi
