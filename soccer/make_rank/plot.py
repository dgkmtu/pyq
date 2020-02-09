import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import Jrank

def _update(frame, x, y, section):

    rank_j1 = Jrank.calc_rank(frame)

    # 描写するデータ（）
    plt_label = []
    plt_value = []
    colorlist = []

    for team in rank_j1:
        plt_label.append(team[0])
        plt_value.append(team[1])
        colorlist.append(team[5])
    plt_label.reverse()
    plt_value.reverse()
    colorlist.reverse()
    
    
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()

    plt.xlim(0, 60)
    plt.title('J1順位表 <第' + str(frame) + '節終了時点>')
    
    plt.barh(plt_label, plt_value ,color=colorlist, zorder=3)
    plt.xlabel("勝ち点")
    plt.grid(zorder=0)

def main():

    section = int(input('何節？=>'))

    # 描画領域
    fig = plt.figure(figsize=(10, 6))
    x = []
    y = []


    params = {
        'fig': fig,
        'func': _update,   # グラフを更新する関数
        'fargs': (x, y, section),   # 関数の引数（フレーム番号を除く）
        'interval': 700,    # 更新間隔（ミリ秒）
        'frames': np.arange(1, section+1, 1),   # フレーム番号を生成するイテレータ
        'repeat': False    # 繰り返さない
    }

    anime = animation.FuncAnimation(**params)

    anime.save('J1_rank.gif', writer='pillow')




if __name__ == '__main__':
    main()
