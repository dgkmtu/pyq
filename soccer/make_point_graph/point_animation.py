import numpy as np
from matplotlib import pyplot as plt
import japanize_matplotlib
from matplotlib import animation

import calc_point
import team_color

def _update(frame, x, y, teams, section):

    # グラフ初期化
    plt.cla()
    # x,yの範囲指定
    plt.xlim(0, section+1)
    plt.ylim(0, 60)

    # データを更新する    
    x.append(frame)

    count = 0
    for team in teams:
        point = calc_point.calculation(frame, team)
        
        y[count].append(point)
        TColor = team_color.color(team)

        # 折れ線グラフを再描写する
        plt.plot(x, y[count], color=TColor, label=team, marker=".")

        count += 1
    # 目盛りの設定
    plt.xlabel("節", fontsize=18)
    plt.ylabel("勝ち点", fontsize=18)
        
    # 凡例の表示
    plt.legend(loc='lower right')

    # グリッドの表示
    plt.grid()

def main():
    teams = []
    
    # 入力情報
    section = int(input('何節？ =>'))
    count_teams = int(input('チーム数？ =>'))
    for count in range(count_teams):
        team    = str(input('チーム名？ =>'))
        teams.append(team)
    file_name = str(input('ファイル名？ =>'))

    # 描画領域
    fig = plt.figure(figsize=(10, 6))
    # パラメータ初期化
    x = []
    y = []
    for count in range(count_teams):
        y_dummy = []
        y.append(y_dummy)

    params = {
        'fig': fig,
        'func': _update, # グラフを更新する関数
        'fargs': (x, y, teams, section), # 関数の引数(フレーム番号を除く)
        'interval': 700, # 更新間隔(ミリ秒)
        'frames': np.arange(1, section+1, 1), # フレーム番号更新
        'repeat': False  # 繰り返さない
    }

    anime = animation.FuncAnimation(**params)

    Ofile = file_name + '.gif'
    anime.save(Ofile, writer='pillow')

if __name__ == '__main__':
    main()
