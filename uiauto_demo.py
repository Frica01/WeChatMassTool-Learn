import subprocess
import time

import uiautomation as auto

# 打开记事本
subprocess.Popen('notepad.exe')
time.sleep(1)  # 等待记事本打开

# 获取记事本窗口
window = auto.WindowControl(ClassName='Notepad')

# 检查窗口是否存在，传入参数都为0，表示仅检查窗口是否存在，不进行额外等待
if window.Exists(maxSearchSeconds=0, searchIntervalSeconds=0):
    # 激活窗口，是窗口成为活动窗口
    window.SetActive()

    # 将窗口置顶(在最前面)
    window.SetTopmost(True)

    # 窗口操作
    # 将窗口最大化
    window.Maximize()
    print('窗口最大化')
    time.sleep(1)

    # 恢复窗口
    window.Restore()
    print('窗口恢复')
    time.sleep(1)

    # 定位到文本框UI
    edit = window.DocumentControl()

    # 输入文本
    edit.SendKeys('测试输入文本内容！测试输入文本内容！')

    # 删除内容
    edit.SendKeys('{Ctrl}a{Delete}')
    time.sleep(0.5)

    # 定位到文件菜单并点击
    fileMenu = window.ButtonControl(Name='关闭')
    fileMenu.Click()

else:
    print("未能找到记事本窗口")
