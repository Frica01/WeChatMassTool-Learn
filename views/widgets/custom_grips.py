# -*- coding: utf-8 -*-
# Name:         custom_grips.py
# Author:       小菜
# Date:         2024/6/6 下午10:54
# Description:

from PySide6.QtCore import (Qt, QRect, QSize)
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (QWidget, QSizeGrip, QFrame, QHBoxLayout)


class Widgets:

    def top(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_top = QFrame(Form)
        self.container_top.setObjectName(u"container_top")
        self.container_top.setGeometry(QRect(0, 0, 500, 10))
        self.container_top.setMinimumSize(QSize(0, 10))
        self.container_top.setMaximumSize(QSize(16777215, 10))
        self.container_top.setFrameShape(QFrame.NoFrame)
        self.container_top.setFrameShadow(QFrame.Raised)
        self.top_layout = QHBoxLayout(self.container_top)
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_left = QFrame(self.container_top)
        self.top_left.setObjectName(u"top_left")
        self.top_left.setMinimumSize(QSize(10, 10))
        self.top_left.setMaximumSize(QSize(10, 10))
        self.top_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.top_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_left.setFrameShape(QFrame.NoFrame)
        self.top_left.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_left)
        self.top_grip = QFrame(self.container_top)
        self.top_grip.setObjectName(u"top")
        self.top_grip.setCursor(QCursor(Qt.SizeVerCursor))
        self.top_grip.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.top_grip.setFrameShape(QFrame.NoFrame)
        self.top_grip.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_grip)
        self.top_right = QFrame(self.container_top)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setMinimumSize(QSize(10, 10))
        self.top_right.setMaximumSize(QSize(10, 10))
        self.top_right.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.top_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_right.setFrameShape(QFrame.NoFrame)
        self.top_right.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_right)

    def bottom(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_bottom = QFrame(Form)
        self.container_bottom.setObjectName(u"container_bottom")
        self.container_bottom.setGeometry(QRect(0, 0, 500, 10))
        self.container_bottom.setMinimumSize(QSize(0, 10))
        self.container_bottom.setMaximumSize(QSize(16777215, 10))
        self.container_bottom.setFrameShape(QFrame.NoFrame)
        self.container_bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout = QHBoxLayout(self.container_bottom)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_left = QFrame(self.container_bottom)
        self.bottom_left.setObjectName(u"bottom_left")
        self.bottom_left.setMinimumSize(QSize(10, 10))
        self.bottom_left.setMaximumSize(QSize(10, 10))
        self.bottom_left.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.bottom_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_left.setFrameShape(QFrame.NoFrame)
        self.bottom_left.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_left)
        self.bottom_grip = QFrame(self.container_bottom)
        self.bottom_grip.setObjectName(u"bottom")
        self.bottom_grip.setCursor(QCursor(Qt.SizeVerCursor))
        self.bottom_grip.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.bottom_grip.setFrameShape(QFrame.NoFrame)
        self.bottom_grip.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_grip)
        self.bottom_right = QFrame(self.container_bottom)
        self.bottom_right.setObjectName(u"bottom_right")
        self.bottom_right.setMinimumSize(QSize(10, 10))
        self.bottom_right.setMaximumSize(QSize(10, 10))
        self.bottom_right.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.bottom_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_right.setFrameShape(QFrame.NoFrame)
        self.bottom_right.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_right)

    def left(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.left_grip = QFrame(Form)
        self.left_grip.setObjectName(u"left")
        self.left_grip.setGeometry(QRect(0, 10, 10, 480))
        self.left_grip.setMinimumSize(QSize(10, 0))
        self.left_grip.setCursor(QCursor(Qt.SizeHorCursor))
        self.left_grip.setStyleSheet(u"background-color: rgb(255, 121, 198);")
        self.left_grip.setFrameShape(QFrame.NoFrame)
        self.left_grip.setFrameShadow(QFrame.Raised)

    def right(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        self.right_grip = QFrame(Form)
        self.right_grip.setObjectName(u"right")
        self.right_grip.setGeometry(QRect(0, 0, 10, 500))
        self.right_grip.setMinimumSize(QSize(10, 0))
        self.right_grip.setCursor(QCursor(Qt.SizeHorCursor))
        self.right_grip.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.right_grip.setFrameShape(QFrame.NoFrame)
        self.right_grip.setFrameShadow(QFrame.Raised)


class CustomGrip(QWidget):
    def __init__(self, parent, position, disable_color=False):

        # SETUP UI
        QWidget.__init__(self)
        self.parent = parent
        self.setParent(parent)
        self.wi = Widgets()

        if position == Qt.TopEdge:
            self.init_top_grip(disable_color)
        elif position == Qt.BottomEdge:
            self.init_bottom_grip(disable_color)
        elif position == Qt.LeftEdge:
            self.init_left_grip(disable_color)
        elif position == Qt.RightEdge:
            self.init_right_grip(disable_color)

    def init_top_grip(self, disable_color):
        self.wi.top(self)
        self.setGeometry(0, 0, self.parent.width(), 10)
        self.setMaximumHeight(10)

        # GRIPS
        QSizeGrip(self.wi.top_left)
        QSizeGrip(self.wi.top_right)

        # RESIZE TOP
        def resize_top(event):
            delta = event.pos()
            height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
            geo = self.parent.geometry()
            geo.setTop(geo.bottom() - height)
            self.parent.setGeometry(geo)
            event.accept()

        self.wi.top_grip.mouseMoveEvent = resize_top

        # ENABLE COLOR
        if disable_color:
            self.wi.top_left.setStyleSheet("background: transparent")
            self.wi.top_right.setStyleSheet("background: transparent")
            self.wi.top_grip.setStyleSheet("background: transparent")

    def init_bottom_grip(self, disable_color):
        self.wi.bottom(self)
        self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
        self.setMaximumHeight(10)

        # GRIPS
        self.bottom_left = QSizeGrip(self.wi.bottom_left)
        self.bottom_right = QSizeGrip(self.wi.bottom_right)

        # RESIZE BOTTOM
        def resize_bottom(event):
            delta = event.pos()
            height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
            self.parent.resize(self.parent.width(), height)
            event.accept()

        self.wi.bottom_grip.mouseMoveEvent = resize_bottom

        # ENABLE COLOR
        if disable_color:
            self.wi.bottom_left.setStyleSheet("background: transparent")
            self.wi.bottom_right.setStyleSheet("background: transparent")
            self.wi.bottom_grip.setStyleSheet("background: transparent")

    def init_left_grip(self, disable_color):
        self.wi.left(self)
        self.setGeometry(0, 10, 10, self.parent.height())
        self.setMaximumWidth(10)

        # RESIZE LEFT
        def resize_left(event):
            delta = event.pos()
            width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
            geo = self.parent.geometry()
            geo.setLeft(geo.right() - width)
            self.parent.setGeometry(geo)
            event.accept()

        self.wi.left_grip.mouseMoveEvent = resize_left

        # ENABLE COLOR
        if disable_color:
            self.wi.left_grip.setStyleSheet("background: transparent")

    def init_right_grip(self, disable_color):
        self.wi.right(self)
        self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
        self.setMaximumWidth(10)

        def resize_right(event):
            delta = event.pos()
            width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
            self.parent.resize(width, self.parent.height())
            event.accept()

        self.wi.right_grip.mouseMoveEvent = resize_right

        # ENABLE COLOR
        if disable_color:
            self.wi.right_grip.setStyleSheet("background: transparent")

    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def resizeEvent(self, event):
        if hasattr(self.wi, 'container_top'):
            self.wi.container_top.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'container_bottom'):
            self.wi.container_bottom.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'left_grip'):
            self.wi.left_grip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, 'right_grip'):
            self.wi.right_grip.setGeometry(0, 0, 10, self.height() - 20)
