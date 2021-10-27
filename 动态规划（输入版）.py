#coins[]=[3，4，5],money=10,n=3,有n种不同面值的硬币，还需要记录路径
coins=input('请输入硬币的各面值：').split(',')
n=int(input('请输入硬币的面值种类：'))
money=int(input('请输入总钱数：'))#使用money作为硬币个数的标记
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

for i in range(1,money+1):#从凑1元开始，一直算到money元为止。
    #print(i,'*******')
    for j in range(n):#循环对比得出硬币数量的最小情况
        resMoney=i-int(coins[j])#求出减去当前面额j后的剩余面额
        if coin_num[resMoney]+1<coin_num[i]:#记录减去当前面额j后的剩余面额的数量
            coin_num[i]=coin_num[resMoney]+1 #记录当前硬币数量为该面额最小硬币数量
            # 将先前的路径和随后的coins[j]合并
            coin_path[i]+=coin_path[resMoney]
            coin_path[i].append(coins[j])
    #print(coin_num[i])
    #print(coin_path[i])

#print(coin_num)
#print(coin_path)
if coin_num[money-1]==999:
    print("此问题无解！")
else:
    print("需要的硬币个数为：",coin_num[money])
    print("所需的硬币面值分别为：",coin_path[money][-coin_num[money]:])#取最终的结果输出