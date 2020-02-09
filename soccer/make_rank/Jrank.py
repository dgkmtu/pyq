import os
from operator import itemgetter
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np


def calc_point(columns, rank_j1):
    I_homeT   = columns[2]
    I_awayT   = columns[3]
    I_homeG   = int(columns[4])
    I_awayG   = int(columns[5])

    if   I_homeG > I_awayG:
        for team in rank_j1:
            if I_homeT == team[0]:
                team[1] += 3                # 勝ち点
                team[2] += I_homeG          # 得点
                team[3] += I_awayG          # 失点
                team[4] = team[2] - team[3] # 得失点

            if I_awayT == team[0]:
                team[2] += I_awayG          # 得点
                team[3] += I_homeG          # 失点
                team[4] = team[2] - team[3] # 得失点

                
    elif I_homeG < I_awayG:
        for team in rank_j1:
            if I_awayT == team[0]:
                team[1] += 3                # 勝ち点
                team[2] += I_awayG          # 得点
                team[3] += I_homeG          # 失点
                team[4] = team[2] - team[3] # 得失点

            if I_homeT == team[0]:
                team[2] += I_homeG          # 得点
                team[3] += I_awayG          # 失点
                team[4] = team[2] - team[3] # 得失点           
    else:
        for team in rank_j1:
            if I_homeT == team[0]:
                team[1] += 1                # 勝ち点
                team[2] += I_homeG          # 得点
                team[3] += I_awayG          # 失点
                team[4] = team[2] - team[3] # 得失点

            if I_awayT == team[0]:
                team[1] += 1                # 勝ち点
                team[2] += I_awayG          # 得点
                team[3] += I_homeG          # 失点
                team[4] = team[2] - team[3] # 得失点

    return rank_j1

def calc_rank(section):
    
    Ifile_teams  = "C:\\Users\\yinag\\AppData\\Local\\Programs\\Python\\Python37\\work\\soccer\\data\\teams_j1.txt"
    Ifile_result = "C:\\Users\\yinag\AppData\\Local\\Programs\\Python\\Python37\\work\\soccer\\data\\result.txt"

    rank_j1 = []

    with open(Ifile_teams, mode='r', encoding='utf-8-sig') as f:
        for row in f:
            result_team = []
        
            columns = row.rstrip().split(',')
        
            I_point      = int(columns[1])
            I_getGoals   = int(columns[2])
            I_givenGoals = int(columns[3])
            I_difGoals   = int(columns[4])

            result_team.append(columns[0])
            result_team.append(I_point)
            result_team.append(I_getGoals)
            result_team.append(I_givenGoals)
            result_team.append(I_difGoals)
            result_team.append(columns[5])
        
            rank_j1.append(result_team)

    with open(Ifile_result, mode='r', encoding='utf-8-sig') as f:
        for row in f:
            columns = row.rstrip().split(',')
            if int(columns[0]) <= section:
                rank_j1 = calc_point(columns, rank_j1)


    rank_j1.sort(key=itemgetter(2), reverse = True)
    rank_j1.sort(key=itemgetter(4), reverse = True)
    rank_j1.sort(key=itemgetter(1), reverse = True)

    return rank_j1

def plot_rank(rank, section):
    
    plt_label = []
    plt_value = []
    colorlist = []
    
    for team in rank:
        plt_label.append(team[0])
        plt_value.append(team[1])
        colorlist.append(team[5])
    plt_label.reverse()
    plt_value.reverse()
    colorlist.reverse()

    plt.figure() # 初期化
    plt.xlim(0, 50)
    plt.title('J1順位表 <第' + str(section) + '節終了時点>')
    
    plt.barh(plt_label, plt_value ,color=colorlist, zorder=3)
    plt.xlabel("勝ち点")
    plt.grid(zorder=0)
    plt.savefig('C:\\Users\\yinag\\AppData\\Local\\Programs\\Python\\Python37\\work\\soccer\\fig\\figure_'+str(section)+'.png')
    plt.close('all')

def main():
    section = int(input('何節？=>'))
    for i in range(1,section+1):
        rank_j1 = calc_rank(i)
        plot_rank(rank_j1, i)
        print(i)

if __name__ == '__main__':
    main()

