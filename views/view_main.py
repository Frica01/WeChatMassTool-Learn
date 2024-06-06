# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/6/2 下午11:25
# @Name   : view_main.py

from PySide6.QtCore import (QTimer, Qt, QEvent, QPoint)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

from views.ui_designs import Ui_MainWindow


class ViewMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #
        self.is_maximum_size = bool(0)
        # 初始化移动位置，初始值为 (0, 0)
        self.move_position: QPoint = QPoint(0, 0)
        #
        # 初始化界面
        self.init_view()
        self.setup_connections()

    def init_view(self):
        """初始化视图"""
        # 无边框
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 半透明
        self.setAttribute(Qt.WA_TranslucentBackground)

    def setup_connections(self):
        # 页面切换事件绑定
        self.btn_page_home.clicked.connect(self.switch_page)
        self.btn_page_pending.clicked.connect(self.switch_page)
        self.btn_page_msg.clicked.connect(self.switch_page)
        # 最小化、最大化&恢复、关闭窗口按钮事件绑定
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_maximize_and_restore.clicked.connect(self.maximize_restore_window)
        self.btn_close.clicked.connect(self.close)
        # 标题栏事件
        self.label_title.mouseMoveEvent = self.move_window
        self.label_title.mouseDoubleClickEvent = self.double_click_maximize_restore

    def switch_page(self):
        """切换页面"""
        page_map = {
            'btn_page_home': self.home,
            'btn_page_pending': self.page_friend,
            'btn_page_msg': self.wechat
        }
        selected_btn = self.sender()
        selected_btn_name: str = selected_btn.objectName()
        if page := page_map.get(selected_btn_name):
            if page == self.stacked_widget.currentWidget():
                return
            # 切换页面
            QTimer.singleShot(150, lambda: self.stacked_widget.setCurrentWidget(page))
        print(f'Button "{selected_btn_name}" pressed!')

    def maximize_restore_window(self):
        """最大化窗口和还原"""
        if not self.is_maximum_size:
            self.showMaximized()
            self.app_margins.setContentsMargins(0, 0, 0, 0)
            self.btn_maximize_and_restore.setToolTip("Restore")
            self.btn_maximize_and_restore.setIcon(QIcon(u":/icons/icons/icon_restore.png"))
        else:
            self.showNormal()
            self.app_margins.setContentsMargins(10, 10, 10, 10)
            self.btn_maximize_and_restore.setToolTip("Maximize")
            self.btn_maximize_and_restore.setIcon(QIcon(u":/icons/icons/icon_maximize.png"))
        self.is_maximum_size = not self.is_maximum_size

    def double_click_maximize_restore(self, event):
        """双击控件事件"""
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, self.maximize_restore_window)

    def move_window(self, event=None):
        """窗口拖动,当鼠标左键按下并移动时，计算新的窗口位置并移动窗口。"""
        if event.buttons() == Qt.LeftButton:
            # 计算新位置：当前鼠标位置 - 初始点击位置
            self.move(event.globalPos() - self.move_position)
            event.accept()

    def mousePressEvent(self, event):
        """鼠标点击事件,当鼠标左键点击时，记录初始点击位置。"""
        if event.button() == Qt.LeftButton:
            # 记录点击位置相对于窗口左上角的偏移
            self.move_position = event.globalPosition().toPoint() - self.pos()
            event.accept()
