# 用amount记录方案的数量，并初始化为0
amount = 0
# 假如100文钱全买公鸡只能买20只，并且必须最少要买一只
for i in range(1, 20):
    # 假如100文钱全买母鸡最多能买33只，并且必须最少要买一只
    for j in range(1, 33):  
         # 假如100文钱全买小鸡最多98只，并且小鸡的数量必须是3的倍数，要保证所有类型的鸡全部都有
        for k in range(3, 99, 3): 
            # 判断公鸡母鸡小鸡总数是否有100只并且随需费用加起来是否为100文钱
            if i + j + k == 100 and i * 5 + j * 3 + k // 3 == 100:  
                # 方案数加1
                amount += 1  
                # 输出方案的详细买法
                print("方案", amount, "：公鸡", i, "只，母鸡", j, "只,小鸡", k, "只。")
# 输出符合要求的方案数量
print("一共", amount, "种方案。")
