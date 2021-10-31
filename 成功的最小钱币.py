import sys
import copy
max = sys.maxsize
def f(coinList,totalCoin):
    #min_coin_num记录最少硬币数
    min_coin_num = [[0 for i in range(totalCoin + 1)] for j in range(len(coinList) + 1)]
    #group记录最少硬币数时使用的硬币类型
    group = [[[] for i in range(totalCoin + 1)] for j in range(len(coinList) + 1)]#二维列表

    for j in range(totalCoin+1):#全部置最大值
            min_coin_num[0][j] = max
    for i in range(1,len(coinList)+1):#循环思路不变
        for j in range(1,totalCoin + 1):
            if j >= coinList[i-1]:
                if min_coin_num[i - 1][j]<min_coin_num[i][j - coinList[i - 1]]+1:
                    #更新最少硬币数
                    min_coin_num[i][j] = min_coin_num[i - 1][j]
                    #更新最少硬币数时使用的硬币类型
                    group[i][j]=copy.deepcopy(group[i - 1][j])
                elif min_coin_num[i - 1][j]==min_coin_num[i][j - coinList[i - 1]]+1:
                    #更新最少硬币数
                    min_coin_num[i][j] = min_coin_num[i - 1][j]
                    #更新最少硬币数时使用的硬币类型
                    cur = copy.deepcopy(group[i][j - coinList[i - 1]])
                    if cur == []:
                        group[i][j]=[[coinList[i - 1]]]
                    else:
                        for c in cur:
                            c.append(coinList[i - 1])
                        group[i][j]=cur
                    cur = copy.deepcopy(group[i - 1][j])
                    group[i][j].extend(cur)
                else:
                    #更新最少硬币数
                    min_coin_num[i][j] = min_coin_num[i][j - coinList[i - 1]]+1
                    #更新最少硬币数时使用的硬币类型
                    cur = copy.deepcopy(group[i][j - coinList[i - 1]])
                    if cur == []:
                        group[i][j]=[[coinList[i - 1]]]
                    else:
                        for c in cur:
                            c.append(coinList[i - 1])
                        group[i][j]=cur
            else:
                #更新最少硬币数时使用的硬币类型
                min_coin_num[i][j] = min_coin_num[i-1][j]
                #更新最少硬币数
                group[i][j] = copy.deepcopy(group[i-1][j])

    return group[i][j], min_coin_num[i][j]

print(f([3,4,5],16))