
def color(team):
    Ifile_color = "C:\\Users\\yinag\AppData\\Local\\Programs\\Python\\Python37\\work\\soccer\\data\\color_j1.txt"
    with open(Ifile_color, mode='r', encoding='utf-8-sig') as f:
        for row in f:
            columns = row.rstrip().split(',')
            if columns[0] == team:
                team_color = columns[1]
    return team_color
