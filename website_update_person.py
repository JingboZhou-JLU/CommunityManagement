import time
import tkinter as tk
from tkinter import ttk, messagebox as msg

import pykeyboard
import pymouse
import pyperclip
import pandas as pd
from openpyxl import load_workbook
import copy
import csv
import re

# 创建用户窗口
mainForm = tk.Tk()
mainForm.title('黎明社区自动导入住户系统')
mainForm.resizable(0, 0)

# 坐标信息
mouseClickAddXY = (392, 735)
mouseClickHousePosXY = (685, 390)
mouseClickWrongXY = (984, 230)
mouseClickHouseCharaXY = (813, 384)
mouseClickHouseSourXY = (1122, 392)
mouseClickBlankXY = (1075, 268)


def confirm_position(string):
    r = string.split('-')
    return r[0], r[1], r[2]


def onClickStartButton():
    global mouseClickHouseCharaXY, mouseClickBlankXY, mouseClickHousePosXY, mouseClickAddXY, mouseClickHouseSourXY
    global person_info

    # 开始执行
    if not msg.askokcancel('提示', '开始执行，在执行完毕前请勿移动鼠标'):
        return
    m = pymouse.PyMouse()  # 获取鼠标对象
    k = pykeyboard.PyKeyboard()  # 获取键盘对象

    # m.click(mouseClickAddXY[0], mouseClickAddXY[1])
    # time.sleep(0.5)

    for person in person_info:
        m.click(mouseClickHousePosXY[0], mouseClickHousePosXY[1])
        time.sleep(1)
        house, unit, home = confirm_position(person[0])
        if house[0:2] == '水岸':
            m.click(625, 331)
            time.sleep(0.5)
            if house[2] == '1':
                m.click(642, 351)
                time.sleep(0.5)
                if unit == '1':
                    m.click(662,373)
                    time.sleep(0.5)
                    base = (720,390)
                    home = int(home)
                    if home <=502:
                        bias = home - 101
                        m.click(base[0],bias[1]+(home//100)*80+(home%100)*20)
                        time.sleep(0.5)

                elif unit == '2':
                    m.click(660,391)
                    time.sleep(0.5)
                else:
                    m.click(662,408)
                    time.sleep(0.5)
            elif house[2] == '2':
                m.click(642, 373)
                time.sleep(0.5)
                if unit == '1':
                    m.click(662,393)
                    time.sleep(0.5)
                elif unit == '2':
                    m.click(660,413)
                    time.sleep(0.5)
                else:
                    m.click(662,433)
                    time.sleep(0.5)
            else:
                m.click(642, 390)
                time.sleep(0.5)
                if unit == '1':
                    m.click(662,410)
                    time.sleep(0.5)
                elif unit == '2':
                    m.click(660,430)
                    time.sleep(0.5)
                else:
                    m.click(662,450)
                    time.sleep(0.5)

        m.click(mouseClickWrongXY[0], mouseClickWrongXY[1])
        time.sleep(0.5)


        # m.click(mouseClickHouseSourXY[0], mouseClickHouseSourXY[1])
        # k.press_key(k.down_key)
        # k.release_key(k.down_key)
        # k.tap_key(k.enter_key)
        # time.sleep(0.5)
        #
        # m.click(mouseClickHouseCharaXY[0], mouseClickHouseCharaXY[1])
        # time.sleep(0.5)
        #
        # m.click(mouseClickBlankXY[0], mouseClickBlankXY[1])
        # time.sleep(0.5)
        #
        # for i in range(0, 13):
        #     k.press_key(k.down_key)
        #     k.release_key(k.down_key)


# 楼号	房屋来源	户主	与户主关系	姓名	身份证号	性别	出生年月	民族	宗教信仰	学历	政治面貌	单位	身份类别	特殊人员	婚姻状况	联系电话

# 读取csv文件
person_info = []
filename = 'data/add_person.csv'
with open(filename, encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        person_info.append(row)

startButton = ttk.Button(mainForm, text='启动', width=50, command=onClickStartButton)
startButton.grid(row=3, padx=5, pady=5)

mainForm.mainloop()
