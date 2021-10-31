#coins[]=[3，4，5],money=10,n=3,有n种不同面值的硬币，还需要记录路径
import copy
#获取当前的硬币数量，配合map使用
def coin(res):
    return coin_num[res]

#对最终结果进行去重和取零
def del_repeat0(lis):
    list_set = []
    for i in lis:  # 去重思路：先给每一项排序再转换为元组，利用集合去重
        # print(i)
        i.sort()
    for t in lis:
        t.remove(0)
        list_set.append(tuple(t))
        list_set = list(set(list_set))
    return list_set

coins=input('请输入硬币的各面值：').split(',')
n=int(input('请输入硬币的面值种类：'))
money=int(input('请输入总钱数：'))#使用money作为硬币个数的标记


#初始化数组，将所有小于money的序列(coin_num)分别记录需要999张
coin_num=[]
for q1 in range(money+1):
    coin_num.append(999)
coin_num[0] = 0#记录初始值数量状态
#print(coin_num)#[0, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]


#初始化数组，将所有小于money的序列(coin_path)先不设置记录需要的面额张数
coin_path=[]
for i in range(money+1):
    coin_path.append([])
#print(coin_path)
coin_path[0] = [0]#记录初始值路径状态


for i in range(1,money+1):#从凑1元开始，一直算到money元为止。
    #print(i,'*******')#配合下面注释的print一类，可以清晰的看到程序运行的流程，省得debug后忘记了前面的
    resMoney_list=[]#把所有 i减去coin[j]后剩下的面额 记录到列表中
    for j in range(n):#循环对比得出硬币数量的最小情况
        resMoney=i-int(coins[j])#求出 i减去coin[j]后剩下的面额
        #排除负数干扰的判断
        if resMoney>=0:
            resMoney_list.append(resMoney)
        else:
            resMoney_list.append(-1)
    #print(resMoney_list)


    #对最小硬币数量下的每一种 相同硬币数量的 进行处理（记录数量、记录路径）
    for k in resMoney_list:
        if coin(k)==min(list(map(coin,resMoney_list))) and k!=-1:#判断最小与合法
            #print(coin_path[k])

            #记录路径
            for g in coin_path[k]:#对同一resMoney下的不同情况(例如8[3,5],[4,4],[5,3])进行遍历记录。备注：最后去重
                coin_per_round_path = []
                #排除合法
                if type(g)==int:
                    coin_per_round_path.append(copy.deepcopy(g))
                if type(g)!=int:
                    coin_per_round_path+=copy.deepcopy(g)
                coin_per_round_path.append(i-k)#每一轮都加
                coin_path[i].append(coin_per_round_path)
    #print(coin_path[i])

    #记录数量
    coin_num[i] = min(list(map(coin, resMoney_list))) + 1
    #print(coin_num)

#print(coin_num)
#print(coin_path)
if coin_num[money]>=999:
    print("此问题无解！")
else:
    print("需要的硬币个数为：",coin_num[money])
    print("所需的硬币面值分别为：",del_repeat0(coin_path[money]))#取最终的结果输出