# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/6/2 下午11:25
# @Name   : view_main.py

from PySide6.QtCore import (QTimer, Qt, QEvent, QPoint, QParallelAnimationGroup, QPropertyAnimation)
from PySide6.QtGui import (QIcon, QColor)
from PySide6.QtWidgets import (QMainWindow, QPushButton, QGraphicsDropShadowEffect, QSizeGrip, QWidget)

from config import (DarkThemeConfig, WidgetConfig)
from views.ui_components import create_width_animation
from views.ui_designs import Ui_MainWindow
from views.widgets import CustomGrip


class ViewMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #
        self.is_maximum_size = bool(0)
        # 初始化移动位置，初始值为 (0, 0)
        self.move_position: QPoint = QPoint(0, 0)
        # 记录当前选中的按钮
        self.current_selected_menu_btn: str = 'btn_page_home'
        # 设置可调节边框
        self.left_grip = None
        self.right_grip = None
        self.top_grip = None
        self.bottom_grip = None
        self.sizegrip = None
        # 保存动画对饮的列表
        self.animation: QPropertyAnimation = None
        self.animation_group: QParallelAnimationGroup = None
        # 初始化界面
        self.init_view()
        self.setup_connections()

    def init_view(self):
        """初始化视图"""
        # 无边框
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 半透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置默认的菜单栏按钮样式
        self.toggle_menu_btn_style()
        # 添加阴影
        self.set_window_shadow()
        # 添加QSizeGrip
        self.add_size_grip()

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
        # 动画事件绑定(分别为 菜单栏、左侧设置面板、右上设置面板)
        self.btn_menu_toggle.clicked.connect(self.toggle_width_animation)
        self.btn_left_settings.clicked.connect(self.toggle_width_animation)
        self.btn_top_settings.clicked.connect(self.toggle_width_animation)

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
            # 设置菜单栏的样式
            self.current_selected_menu_btn = selected_btn_name  # 记录当前选中的按钮
            self.toggle_menu_btn_style()
            # 切换页面
            QTimer.singleShot(150, lambda: self.stacked_widget.setCurrentWidget(page))
        print(f'Button "{selected_btn_name}" pressed!')

    def toggle_menu_btn_style(self):
        """切换菜单栏按钮样式"""
        # 循环取 frame_menu 下面所有的按钮控件
        for widget in self.frame_menu.findChildren(QPushButton):
            widget: QPushButton
            # 检查按钮是否是当前选中的按钮
            if widget.objectName() == self.current_selected_menu_btn:
                # 为选中的按钮添加选中样式，直接将样式追加到控件上
                widget.setStyleSheet(widget.styleSheet() + DarkThemeConfig.MENU_SELECTED_STYLESHEET)
            else:
                # 移除其他按钮的选中样式，替换原有的选中样式
                widget.setStyleSheet(widget.styleSheet().replace(DarkThemeConfig.MENU_SELECTED_STYLESHEET, ''))

    def toggle_width_animation(self):
        """切换面板宽度动画"""
        # 按钮与面板对应的宽度配置
        btn_widget_width_map = {
            'btn_menu_toggle': WidgetConfig.MENU_WIDTHS,
            'btn_left_settings': WidgetConfig.CONFIG_WIDTHS,
            'btn_top_settings': WidgetConfig.CONFIG_WIDTHS
        }

        # 按钮与控件
        btn_widget_map = {
            'btn_menu_toggle': self.frame_menu_left_box,
            'btn_left_settings': self.frame_left_settings_box,
            'btn_top_settings': self.frame_right_settings_box
        }

        # 按钮与颜色
        btn_color_map = {
            'btn_left_settings': DarkThemeConfig.BTN_LEFT_SETTING_COLOR,
            'btn_top_settings': DarkThemeConfig.BTN_RIGHT_SETTING_COLOR
        }

        # 当前点击按钮
        widget: QPushButton = self.sender()
        object_name: str = widget.objectName()
        width_map = btn_widget_width_map.get(object_name)
        box_widget: QWidget = btn_widget_map.get(object_name)

        # 获取面板应该设置的宽度
        max_width = width_map.get('MAX')
        default_width = width_map.get('DEFAULT')
        target_width = max_width if box_widget.width() == default_width else default_width

        # 设置按钮颜色
        if color := btn_color_map.get(object_name):
            if target_width:
                widget.setStyleSheet(widget.styleSheet() + color)
            else:
                widget.setStyleSheet(widget.styleSheet().replace(color, ''))

        # 创建并启动动画
        self.animation = create_width_animation(box_widget, target_width)
        self.animation.start()

    def maximize_restore_window(self):
        """最大化窗口和还原"""
        if not self.is_maximum_size:
            self.showMaximized()
            self.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
            self.app_margins.setContentsMargins(0, 0, 0, 0)
            self.btn_maximize_and_restore.setToolTip("Restore")
            self.btn_maximize_and_restore.setIcon(QIcon(u":/icons/icons/icon_restore.png"))
        else:
            self.showNormal()
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
            self.app_margins.setContentsMargins(10, 10, 10, 10)
            self.btn_maximize_and_restore.setToolTip("Maximize")
            self.btn_maximize_and_restore.setIcon(QIcon(u":/icons/icons/icon_maximize.png"))
        self.is_maximum_size = not self.is_maximum_size

    def double_click_maximize_restore(self, event):
        """双击控件事件"""
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, self.maximize_restore_window)

    def set_window_shadow(self):
        """设置窗口阴影"""
        shadow_effect = QGraphicsDropShadowEffect(self.bgApp)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setXOffset(0)
        shadow_effect.setYOffset(0)
        # 表示一个黑色，并且有一定程度的透明度
        shadow_effect.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(shadow_effect)

    def add_size_grip(self):
        """设置可调节边框"""
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)
        # 为右下角的抓手frame添加一个样式
        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

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

    def resizeEvent(self, event):
        """处理窗口大小调整事件"""
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
