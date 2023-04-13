import time
import tkinter as tk
from tkinter import ttk, messagebox as msg


import pykeyboard
import pymouse
import pyperclip

# 创建用户窗口
mainForm = tk.Tk()
mainForm.title('黎明社区自动迁出住户系统')
mainForm.resizable(0, 0)

# 输入框，用于输入要删除的住户
nameText = tk.Text(mainForm, height=40, width=50)
nameText.insert(0.0, "在此处键入需要迁出的住户的姓名:")
nameText.grid(row=0, padx=5, pady=5)

# 位置初始化
mouseSearchXY = (-1, -1)
mouseClick1XY = (-1, -1)
mouseClick2XY = (-1, -1)
mouseClick3XY = (-1, -1)
mouseClick4XY = (-1, -1)
mouseClick5XY = (-1, -1)
mouseClick6XY = (-1, -1)
mouseClick7XY = (-1, -1)
mouseClick8XY = (-1, -1)


def onClickMouseButton():
    # 将鼠标位置声明为全局变量
    global mouseSearchXY, mouseClick1XY, mouseClick2XY, mouseClick3XY, mouseClick4XY
    global mouseClick5XY, mouseClick6XY, mouseClick7XY, mouseClick8XY
    m = pymouse.PyMouse()
    msg.showinfo('提示', '请在点击确认后2秒内将鼠标移动到“姓名”的输入框位置')
    time.sleep(2)
    mouseSearchXY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后10秒内将鼠标移动到按键“查询”的位置')
    time.sleep(10)
    mouseClick1XY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后2秒内将鼠标移动到按键“折叠”的位置')
    time.sleep(2)
    mouseClick2XY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后3秒内将鼠标移动到按键“迁出”的位置')
    time.sleep(3)
    mouseClick3XY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后3秒内将鼠标移动到按键“迁出时间”的位置')
    time.sleep(3)
    mouseClick4XY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后3秒内将鼠标移动到按键“今天”的位置')
    time.sleep(3)
    mouseClick5XY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后3秒内将鼠标移动到按键“保存”的位置')
    time.sleep(3)
    mouseClick6XY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后3秒内将鼠标移动到按键“确定”的位置')
    time.sleep(3)
    mouseClick7XY = m.position()

    msg.showinfo('成功', '成功，请在点击确认后3秒内将鼠标移动到按键“展开”的位置')
    time.sleep(3)
    mouseClick8XY = m.position()

    msg.showinfo('成功', '成功完成')


mouseButton = ttk.Button(mainForm, text='点击获取鼠标位置', width=50, command=onClickMouseButton)
mouseButton.grid(row=2, padx=5, pady=5)


def onClickStartButton():
    # 判断是否已经读取鼠标位置
    if mouseSearchXY == (-1, -1) or mouseClick1XY == (-1, -1) or mouseClick2XY == (-1, -1) or mouseClick3XY == (
            -1, -1) or mouseClick4XY == (-1, -1) or mouseClick5XY == (-1, -1) or mouseClick6XY == (
            -1, -1) or mouseClick7XY == (
            -1, -1) or mouseClick8XY == (-1, -1):
        msg.showerror('错误', '请先获取鼠标位置')
        return

    # 判断输入框有没有内容
    nameContent = nameText.get(0.0, tk.END).rstrip()
    if nameContent == '在此处键入需要迁出的住户的姓名:' or nameContent == '':
        msg.showerror('错误', '请先输入需要迁出的住户的姓名')
        return

    # 开始执行
    if not msg.askokcancel('提示', '开始执行，在执行完毕前请勿移动鼠标'):
        return

    m = pymouse.PyMouse()  # 获取鼠标对象
    k = pykeyboard.PyKeyboard()  # 获取键盘对象
    lst = nameContent.split()  # 获取需要删除的住户列表

    cnt = 1
    for i in lst:
        """
        1.姓名
        """
        m.click(mouseSearchXY[0], mouseSearchXY[1])  # 点击
        time.sleep(1)

        if cnt >= 2:
            k.press_key(k.backspace_key)
            k.release_key(k.backspace_key)
            k.press_key(k.backspace_key)
            k.release_key(k.backspace_key)
            k.press_key(k.backspace_key)
            k.release_key(k.backspace_key)

        pyperclip.copy(i)  # 复制内容

        k.press_key(k.control_key)  # 粘贴内容
        k.tap_key('v')
        k.release_key(k.control_key)

        time.sleep(1)

        # k.tap_key(k.enter_key)

        """
        2.查询
        """
        m.click(mouseClick1XY[0], mouseClick1XY[1])  # 点击
        time.sleep(5)  # 搜索的时间

        """
        3.折叠
        """
        m.click(mouseClick2XY[0], mouseClick2XY[1])  # 点击
        time.sleep(0.5)

        """
        4.迁出
        """
        m.click(mouseClick3XY[0], mouseClick3XY[1])  # 点击
        time.sleep(1)

        """
        5.迁出时间
        """
        m.click(mouseClick4XY[0], mouseClick4XY[1])  # 点击
        time.sleep(0.5)

        """
        6.今天
        """
        m.click(mouseClick5XY[0], mouseClick5XY[1])  # 点击
        time.sleep(0.5)

        """
        7.保存
        """
        m.click(mouseClick6XY[0], mouseClick6XY[1])  # 点击
        time.sleep(3)

        """
        8.确定
        """
        m.click(mouseClick7XY[0], mouseClick7XY[1])  # 点击
        time.sleep(10)

        """
        9.展开
        """
        m.click(mouseClick8XY[0], mouseClick8XY[1])  # 点击
        time.sleep(1)

        time.sleep(0.5)
        cnt = cnt + 1
    msg.showinfo('提示', '任务成功完成！')


startButton = ttk.Button(mainForm, text='启动', width=50, command=onClickStartButton)
startButton.grid(row=3, padx=5, pady=5)

mainForm.mainloop()
