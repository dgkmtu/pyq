# 順位表折れ線グラフ作成モジュール
# 2019/11/5  ver1  新規作成
# 2019/11/8  ver2  GUI画面からのパラメータ受け取り対応

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import calc_rank
import team_color

def _update(frame, x, y, teams, section):

    # グラフ初期化
    plt.cla()

    # x, yの範囲指定
    plt.xlim(0, section+1)
    plt.ylim(19,0)

    # データを更新する
    x.append(frame)

    count = 0

    for team in teams:
        rank = calc_rank.calculation(frame, team)

        y[count].append(rank)
        TColor = team_color.color(team)

        # 折れ線グラフを再描写する
        plt.plot(x, y[count], color=TColor, label=team, marker=".")
        
        count += 1

    # 目盛りの設定
    plt.xlabel("節", fontsize=18)
    plt.ylabel("順位", fontsize=18)
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

    # 凡例の表示
    plt.legend(loc='lower right')

    # グリッドの表示
    plt.grid()

def main(section, teams, file_name):

    # チーム数のカウント
    count_teams = len(teams)
    
    # 描画領域
    fig = plt.figure(figsize=(10, 8))

    # パラメータ初期化
    x = []
    y = []
    for count in range(count_teams):
        y_dummy = []
        y.append(y_dummy)

    # パラメータ設定
    params = {
        'fig': fig,
        'func': _update,
        'fargs': (x, y, teams, section),
        'interval': 700,
        'frames': np.arange(1, section+1, 1),
        'repeat': False
        }

    anime = animation.FuncAnimation(**params)

    Ofile = file_name + '.gif'
    anime.save(Ofile, writer='pillow')

    result = "done"

    return result


if __name__ == '__main__':
    main()
