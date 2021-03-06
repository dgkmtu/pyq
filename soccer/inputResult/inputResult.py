
import os, sys
import re
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from registerCsv import registerCsv

def resultRead(event):
    print("done")

def resultList(event):
    sub_win = Toplevel()
    sub_win.title('試合結果')

    # subframe1の作成
    subframe1 = ttk.Frame(sub_win, padding=10)
    subframe1.grid(row=0, column=0, sticky=W)

    # 「年度」ラベルの作成
    sub_year_label = ttk.Label(subframe1, text='年度　＞＞')
    sub_year_label.pack(side=LEFT)

    # 「年度」エントリーの作成
    subentry1 = StringVar()
    sub_year_entry = ttk.Entry(subframe1, textvariable=subentry1, width=10)
    sub_year_entry.pack(side=LEFT)

    # 「節」ラベルの作成
    sub_section_label = ttk.Label(subframe1, text=' 節　＞＞')
    sub_section_label.pack(side=LEFT)

    # 「節」エントリーの作成
    subentry2 = StringVar()
    sub_section_entry = ttk.Entry(subframe1, textvariable=subentry2, width=5)
    sub_section_entry.pack(side=LEFT)

    # 実行ボタンの設置
    button1 = ttk.Button(subframe1, text='実行')
    button1.bind("<Button-1>", resultRead)
    button1.pack(side=LEFT)

def conductMain(event):
    # 入力項目の格納
    section = section_entry.get()
    year  = year_entry.get()
    month = month_entry.get()
    day   = day_entry.get()
    Hteam = Hteam_entry.get()
    H1stGoal = H1stGoal_entry.get()
    H2ndGoal = H2ndGoal_entry.get()
    Ateam = Ateam_entry.get()
    A1stGoal = A1stGoal_entry.get()
    A2ndGoal = A2ndGoal_entry.get()

    # 初期設定
    text = ''

    # 入力日付の形式チェック
    date = year + '/' + month + '/' + day
    rep = '^\d{4}/\d{1,2}/\d{1,2}$'
    isDate = re.match(rep, date)

    if not isDate:
        text += '日付に誤りがあります。\n'

    # ホームチームの入力チェック
    if not Hteam or not H1stGoal or not H2ndGoal:
        text += 'HOMEチームの入力に誤りがあります。\n'
    # アウェイチームの入力チェック
    if not Ateam or not A1stGoal or not A2ndGoal:
        text += 'AWAYチームの入力に誤りがあります。\n'

    if text:
        messagebox.showerror('error', text)


    # 試合結果の計算
    # ホームチームの得点計算
    HtotalGoal = int(H1stGoal) + int(H2ndGoal)
    # アウェイチームの得点計算
    AtotalGoal = int(A1stGoal) + int(A2ndGoal)

    # 入力情報の格納
    inputData = []

    inputData.append(section)
    inputData.append(date)
    inputData.append(Hteam)
    inputData.append(Ateam)
    inputData.append(str(HtotalGoal))
    inputData.append(str(AtotalGoal))
    inputData.append(H1stGoal)
    inputData.append(H2ndGoal)
    inputData.append(A1stGoal)
    inputData.append(A2ndGoal)

    state = registerCsv(inputData)

    if state == True:
        text = '登録完了しました。'

        messagebox.showinfo('info', text)

        # 入力項目の削除
        Hteam_entry.delete(0, tkinter.END)
        H1stGoal_entry.delete(0, tkinter.END)
        H2ndGoal_entry.delete(0, tkinter.END)
        Ateam_entry.delete(0, tkinter.END)
        A1stGoal_entry.delete(0, tkinter.END)
        A2ndGoal_entry.delete(0, tkinter.END)
        
if __name__ == '__main__':

    # rootの作成
    root = Tk()
    root.title('試合結果登録画面')

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=0, sticky=W)

    # 「節」ラベルの作成
    section_label = ttk.Label(frame1, text='節　＞＞')
    section_label.pack(side=LEFT)

    # 「節」エントリーの作成
    entry1 = StringVar()
    section_entry = ttk.Entry(frame1, textvariable=entry1, width=5)
    section_entry.pack(side=LEFT)

    
    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=1, column=0, sticky=W)

    # 「年月日」ラベルの作成
    ymd_label = ttk.Label(frame2, text='試合日＞＞')
    ymd_label.pack(side=LEFT)

    # 「年」エントリーの作成
    entry2 = StringVar()
    year_entry = ttk.Entry(frame2, textvariable=entry2, width=10)
    year_entry.pack(side=LEFT)

    # 「年」ラベルの作成
    year_label = ttk.Label(frame2, text='年')
    year_label.pack(side=LEFT)

    # 「月」エントリーの作成
    entry3 = StringVar()
    month_entry = ttk.Entry(frame2, textvariable=entry3, width=5)
    month_entry.pack(side=LEFT)

    # 「月」ラベルの作成
    month_label = ttk.Label(frame2, text='月')
    month_label.pack(side=LEFT)

    # 「日」エントリーの作成
    entry4 = StringVar()
    day_entry = ttk.Entry(frame2, textvariable=entry4,  width=5)
    day_entry.pack(side=LEFT)

    # 「日」ラベルの作成
    day_label = ttk.Label(frame2, text='日')
    day_label.pack(side=LEFT)


    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=2, column=0, sticky=W)

    # 「ホームチーム名」ラベルの作成
    Hteam_label = ttk.Label(frame3, text='ホームチーム名  ＞＞')
    Hteam_label.pack(side=LEFT)

    # 「ホームチーム名」エントリーの作成
    entry5 = StringVar()
    Hteam_entry = ttk.Entry(frame3, textvariable=entry5, width=10)
    Hteam_entry.pack(side=LEFT)

    # 「前半得点」ラベルの作成
    H1stGoal_label = ttk.Label(frame3, text='前半得点:')
    H1stGoal_label.pack(side=LEFT)

    # 「前半得点」エントリーの作成
    entry6 = StringVar()
    H1stGoal_entry = ttk.Entry(frame3, textvariable=entry6, width=5)
    H1stGoal_entry.pack(side=LEFT)

    # 「後半得点」ラベルの作成
    H2ndGoal_label = ttk.Label(frame3, text='後半得点')
    H2ndGoal_label.pack(side=LEFT)

    # 「後半得点」エントリーの作成
    entry7 = StringVar()
    H2ndGoal_entry = ttk.Entry(frame3, textvariable=entry7, width=5)
    H2ndGoal_entry.pack(side=LEFT)


    # Frame4の作成
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=3, column=0, sticky=W)

    # 「アウェイチーム名」ラベルの作成
    Ateam_label = ttk.Label(frame4, text='アウェイチーム名＞＞')
    Ateam_label.pack(side=LEFT)

    # 「アウェイチーム名」エントリーの作成
    entry8 = StringVar()
    Ateam_entry = ttk.Entry(frame4, textvariable=entry8, width=10)
    Ateam_entry.pack(side=LEFT)

    # 「前半得点」ラベルの作成
    A1stGoal_label = ttk.Label(frame4, text='前半得点:')
    A1stGoal_label.pack(side=LEFT)

    # 「前半得点」エントリーの作成
    entry9 = StringVar()
    A1stGoal_entry = ttk.Entry(frame4, textvariable=entry9, width=5)
    A1stGoal_entry.pack(side=LEFT)

    # 「後半得点」ラベルの作成
    A2ndGoal_label = ttk.Label(frame4, text='後半得点')
    A2ndGoal_label.pack(side=LEFT)

    # 「後半得点」エントリーの作成
    entry10 = StringVar()
    A2ndGoal_entry = ttk.Entry(frame4, textvariable=entry10, width=5)
    A2ndGoal_entry.pack(side=LEFT)


    # Frame5の作成
    frame5 = ttk.Frame(root, padding=10)
    frame5.grid(row=4, column=0, sticky=E)

    # 実行ボタンの設置
    button1 = ttk.Button(frame5, text='実行')
    button1.bind("<Button-1>", conductMain)
    button1.pack(side=LEFT)

    # キャンセルボタンの設置
    button2 = ttk.Button(frame5, text=('キャンセル'), command=quit)
    button2.pack(side=LEFT)

    # 試合一覧ボタンの設置
    button2 = ttk.Button(frame5, text='試合結果')
    button2.bind("<Button-1>", resultList)
    button2.pack(side=LEFT)

    root.mainloop()
