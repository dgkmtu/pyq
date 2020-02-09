
# 節とチーム名を受け取り順位を受け取るモジュール
## 2019/11/5  ver1 新規作成

import sys
sys.path.append("C:\\Users\\yinag\\AppData\\Local\\Programs\\Python\\Python37\\work\\soccer\\tool") 

import calc_Jrank

def calculation(section, team):

    J1rank = calc_Jrank.calc_rank(section)

    Wrank = 1

    for teamRank in J1rank:
        if team == teamRank[0]:
            rank = Wrank
        Wrank += 1
    
    Orank = int(rank)
    return Orank

def main():
    section = 20
    team = '鹿島'
    rank = calculation(section, team)

    print(rank)

if __name__ == '__main__':
    main()
