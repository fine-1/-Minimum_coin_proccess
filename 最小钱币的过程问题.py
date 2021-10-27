#coins[]=[3，4，5],money=10,n=3,有n种不同面值的硬币，还需要记录路径
coins=[3,4,5]
n=3
money=12#使用money作为硬币个数的标记
#初始化数组，将所有小于money的序列(coin_num)分别记录需要999张
coin_num=[]
for q1 in range(money+1):
    coin_num.append(999)
coin_num[0] = 0#记录初始值状态
#print(coin_num)#[0, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]
#初始化数组，将所有小于money的序列(coin_path)先不设置记录需要的面额张数
coin_path=[]
for i in range(money+1):
    coin_path.append([])
#print(coin_path)#[[], [], [], [], [], [], [], [], [], [], []]
"""
coin_and_path=[]
for i in range(money+1):
    coin_and_path.append([])
"""

for i in range(1,money+1):#从凑1元开始，一直算到money元为止。
    print(i,'*******')
    resMoney_list = []
    resMoney_coin_list = []
    resMoney_min_coin_list = []
    resMoney_min_coin_que_list = []  # 记录最小钱币数量对应的剩余面额
    # 循环对比得出硬币数量的最小情况
    for j in range(n):
        if i-coins[j]>=0:
            resMoney_list.append(i-coins[j])
        else:
            resMoney_list.append(-1)
    print('resMoney_list:',resMoney_list)
    for r in resMoney_list:
        resMoney_coin_list.append(coin_num[r])
    #采用min最小比较的模式，然后遍历所有resMoney，如果它的coin_num也等于min就把它记录下来
    flag_1=0
    for resM_coin in resMoney_coin_list:#利用该方式得到并记录所有最小硬币数量的情况
        flag_1 += 1#利用标识记录每种情况对应的resmoney的列表值
        if resM_coin==min(resMoney_coin_list):
            resMoney_min_coin_list.append(resM_coin)
            resMoney_min_coin_que_list.append(resMoney_list[flag_1-1])#记录最小钱币数对应的resmoney
    print("resMoney_min_coin_list：",resMoney_min_coin_list)
    print("resMoney_min_coin_que_list:",resMoney_min_coin_que_list)
    #当下就获得了硬币数量最小且相等的（如果存在，不存在也无妨）剩余面额
    for resM_min_coin in resMoney_min_coin_list:
        coin_num[i] = resM_min_coin + 1  # 分别记录resMoney_min_coin_list硬币数量+1为该面额最小硬币数量
        #创建可以记录每一个resMoney的表
    print(coin_num[i])
    flag_2=0#同一i下存在几种情况
    for resMoney_que in range(len(resMoney_min_coin_que_list)):#对resMoney_min_coin_que_list中每一种相同的情况来说
        # 要保存一情况下的情况，而且可能存在多种情况！！！！！
        #coin_num_moment=resMoney_coin_list[resMoney_que]#因为resMoney_min_coin_list的序列和resMoney_min_coin_que_list是相对应的，所以该取法可以确认对应情况的coin_num
        #resMoney_que为0即取第一种情况，为1即取第二种情况
        #coin_path[i] = []
        coin_path[i] += coin_path[resMoney_min_coin_que_list[resMoney_que]]  # 在去前情况剩余值的时候没有取其一所以失败了，例如[4, 3, 3, 4]这是7的情况，所以只要取其2即可，或许我需要一个三维列表
        #coin_path[i].append(resMoney_min_coin_que_list[resMoney_que])#直接记录剩余的面额，最后再去遍历路径 # 此后所有的情况都是两两成对的
        coin_path[i].append(i - resMoney_min_coin_que_list[resMoney_que])  # coins[j]=i-resMoney
        #路径使用coin_path调用之前的路径，使用coin_and_path记录相同的情况
        flag_2+=1
    print(coin_path)
    """尝试过的相同情况分离方式
    flag_3 = 0
    list_1 = []
    for location in coin_path[i]:
        #print(location)
        flag_3+=1
        list_1.append(location)
        if flag_3==2:
            print(list_1)
            list_1 = []
            flag_3 = 0
"""


"""原始思路
        resMoney=i-coins[j]#求出减去当前面额j后的剩余面额
        if coin_num[resMoney]+1<coin_num[i]:#记录减去当前面额j后的剩余面额的数量
            coin_num[i]=coin_num[resMoney]+1 #记录当前硬币数量为该面额最小硬币数量
            # 将先前的路径和随后的coins[j]合并
            coin_path[i] += coin_path[resMoney]
            coin_path[i].insert(len(coin_path[i]),coins[j])#最佳方法为替换才正确，而不是把所有的都加进来
        #if coin_path[i] != []:
            #coin_path[i].pop(-len(coin_path[resMoney]))
        if coin_num[resMoney] + 1 == coin_num[i]:
 """
print(coin_num)
print(coin_path)
if coin_num[money-1]==999:
    print("此问题无解！")
else:
    print("需要的硬币个数为：",coin_num[money])
    print("所需的硬币面值分别为：",coin_path[money])#取最终的结果输出