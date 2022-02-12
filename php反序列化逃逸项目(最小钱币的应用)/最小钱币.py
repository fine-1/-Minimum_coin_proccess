def mincoin(money,*coins):
    import copy
    def coin(res):
        return coin_num[res]

    def del_repeat0(lis):
        list_set = []
        for i in lis:
            # print(i)
            i.sort()
        for t in lis:
            t.remove(0)
            list_set.append(tuple(t))
            list_set = list(set(list_set))
        return list_set

    #coins = [3, 4]
    n = len(coins)
    # money=int(input(len('请输入逃逸字符串：')))
    #money = 62

    coin_num = []
    for q1 in range(money + 1):
        coin_num.append(999)
    coin_num[0] = 0

    coin_path = []
    for i in range(money + 1):
        coin_path.append([])
    coin_path[0] = [0]

    for i in range(1, money + 1):
        resMoney_list = []
        for j in range(n):
            resMoney = i - int(coins[j])
            if resMoney >= 0:
                resMoney_list.append(resMoney)
            else:
                resMoney_list.append(-1)

        for k in resMoney_list:
            if coin(k) == min(list(map(coin, resMoney_list))) and k != -1:

                for g in coin_path[k]:
                    coin_per_round_path = []
                    if type(g) == int:
                        coin_per_round_path.append(copy.deepcopy(g))
                    if type(g) != int:
                        coin_per_round_path += copy.deepcopy(g)
                    coin_per_round_path.append(i - k)
                    coin_path[i].append(coin_per_round_path)

        coin_num[i] = min(list(map(coin, resMoney_list))) + 1

    if coin_num[money] >= 999:
        print("此问题无解！")
    else:
        return del_repeat0(coin_path[money])