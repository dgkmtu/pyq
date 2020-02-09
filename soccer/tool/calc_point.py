

def calculation(section, team):

    Ifile_result = "C:\\Users\\yinag\AppData\\Local\\Programs\\Python\\Python37\\work\\soccer\\data\\result.txt"

    point = 0
    
    with open(Ifile_result, mode='r', encoding='utf-8-sig') as f:
        for row in f:
            columns = row.rstrip().split(',')

            # 節 判定
            if section >= int(columns[0]):
                
                # ホーム戦 結果判定
                if columns[2] == team:
                    if columns[4] > columns[5]:
                        point += 3
                    elif columns[4] == columns[5]:
                        point += 1

                # アウェイ戦 結果判定
                elif columns[3] == team:
                    if columns[4] < columns[5]:
                        point += 3
                    elif columns[4] == columns[5]:
                        point += 1
    return point

def main():
    point = calculation(5, '鹿島')
    print(point)


if __name__ == '__main__':
    main()
