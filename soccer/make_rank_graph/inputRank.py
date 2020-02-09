# 順位表作成GUIモジュール
# 2019/11/6  ver1  新規作成
# 2019/11/7  ver2  画面調整
# 2019/11/8  ver3  パラメータ受け取り機能追加

import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import rank_animation

def error_section():
    Is1_entry.delete(0, END)
    Is1_entry.insert(END, "error")
    Is1_entry.config(fg="#F0F8FF")

# button1クリック時の処理
def button1_clicked():
    done  = True
    error = ""
    
    # 各入力値の受け取り
    # 節
    section = Is1.get()
    if not section:
        error += "節の入力がありません。\n"
        done  = False
        error_section()
        

    # 対象チーム
    teams = []
    if bln1.get():
        teams.append(Is_team1.get())

    if bln2.get():
        teams.append(Is_team2.get())

    if bln3.get():
        teams.append(Is_team3.get())

    if bln4.get():
        teams.append(Is_team4.get())

    if bln5.get():
        teams.append(Is_team5.get())

    # 出力ファイル名
    file_name   = Is4.get()
    if not file_name:
        error += "出力ファイル名の入力がありません。"
        done  = False

    if done == True:
        result = rank_animation.main(int(section), teams, file_name)

        if result == "done":
            text = "処理が完了しました！"
            messagebox.showinfo('info', text)
    else:
        messagebox.showerror('info', error)
        

if __name__ == '__main__':
    
    # rootの作成
    root = Tk()
    root.title('J1順位表作成ツール')
    root.resizable(False, False)
    root.geometry('270x300')
    
    # ラベルの作成
    # 「節」ラベルの作成
    s1 = StringVar()
    s1.set('節 >>')
    label1 = ttk.Label(textvariable=s1)
    label1.place(x=20, y=10)

    # 「節欄」エントリーの作成
    Is1   = StringVar()
    Is1_entry = ttk.Entry(textvariable=Is1, width=10)
    Is1_entry.place(x=60, y=10)

    # 「選択」ラベルの作成
    s2 = StringVar()
    s2.set('選択')
    label2 = ttk.Label(textvariable=s2)
    label2.place(x=20, y=40)

    # 「チーム名」ラベルの作成
    s3 = StringVar()
    s3.set('チーム名')
    label3 = ttk.Label(textvariable=s3)
    label3.place(x=60, y=40)

    # チェックボタンの設置１
    bln1 = BooleanVar()
    bln1.set(False)
    chk1 = ttk.Checkbutton(root, variable=bln1)
    chk1.place(x=25, y=60)

    # 「チーム名」エントリーの作成１
    Is_team1   = StringVar()
    Is_team1_entry = ttk.Entry(textvariable=Is_team1, width=30)
    Is_team1_entry.place(x=60, y=60)

    # チェックボタンの設置２
    bln2 = BooleanVar()
    bln2.set(False)
    chk2 = ttk.Checkbutton(root, variable=bln2)
    chk2.place(x=25, y=85)

    # 「チーム名」エントリーの作成２
    Is_team2   = StringVar()
    Is_team2_entry = ttk.Entry(textvariable=Is_team2, width=30)
    Is_team2_entry.place(x=60, y=85)

    # チェックボタンの設置３
    bln3 = BooleanVar()
    bln3.set(False)
    chk3 = ttk.Checkbutton(root, variable=bln3)
    chk3.place(x=25, y=110)

    # 「チーム名」エントリーの作成３
    Is_team3   = StringVar()
    Is_team3_entry = ttk.Entry(textvariable=Is_team3, width=30)
    Is_team3_entry.place(x=60, y=110)

    # チェックボタンの設置４
    bln4 = BooleanVar()
    bln4.set(False)
    chk4 = ttk.Checkbutton(root, variable=bln4)
    chk4.place(x=25, y=135)

    # 「チーム名」エントリーの作成４
    Is_team4   = StringVar()
    Is_team4_entry = ttk.Entry(textvariable=Is_team4, width=30)
    Is_team4_entry.place(x=60, y=135)

    # チェックボタンの設置５
    bln5 = BooleanVar()
    bln5.set(False)
    chk5 = ttk.Checkbutton(root, variable=bln5)
    chk5.place(x=25, y=160)

    # 「チーム名」エントリーの作成５
    Is_team5   = StringVar()
    Is_team5_entry = ttk.Entry(textvariable=Is_team5, width=30)
    Is_team5_entry.place(x=60, y=160)

    # 「ファイル名」ラベルの作成
    s4 = StringVar()
    s4.set('ファイル名 >>')
    label4 = ttk.Label(textvariable=s4)
    label4.place(x=20, y=190)

    # 「ファイル名」エントリーの作成
    Is4   = StringVar()
    Is4_entry = ttk.Entry(textvariable=Is4, width=25)
    Is4_entry.place(x=90, y=190)


    # startボタンの作成
    button1 = ttk.Button(text='作成', command=button1_clicked)
    button1.place(x=20, y=240)

    #Cancelボタンの作成
    button2 = ttk.Button(text='閉じる', command=quit)
    button2.place(x=120, y=240)



    root.mainloop()
