# guess number
# import random
#
# num = random.randint(1, 10)  # 随机生成1－10之间的数字
# answer = int(input('猜个数字: '))  # 将用户输入的字符转成整数
# if answer > num:
#     print('猜大了')
# elif answer < num:
#     print('猜小了')
# else:
#     print('猜对了')
#
# print('正确答案是:', num)



#1+2+3...+100
# n=1
# count=0
# while n<=100:
#     count=count+n
#     n=n+1
# print(count)

# for i in range(1,101):
#     count+=i
# print(count)
#
# print(sum(range(1,101)))


# rolling game
# 掷两个骰子（1-6）
# 玩游戏要有金币
# 玩游戏增金币1枚，充值获取金币
# 充值金额需要是10元的倍数
# 玩游戏消耗金币5
# 猜大小：猜对奖励金币2枚，猜错没有奖励 （超出6点为大，否则小）
# 游戏结束：1.主动退出  2.没有金币退出
# 退出需打印金币数和游戏局数

# import random
# # 初始金币数和游戏次数
# coins = 0
# count = 0
# if coins < 5:
#     print('金币余额不足，请充值')
#     while True:
#         charge = int(input('请输入充值金额：'))
#         if charge % 10 == 0:
#             coins = coins + charge
#             print(f'充值成功，当前金币余额为{coins}。')
#             join = input('是否参加游戏？（y/n）:')
#             while join == 'y' and coins > 5:
#                 coins -= 5
#                 coins += 1
#                 ran1 = random.randint(1,6)
#                 ran2 = random.randint(1, 6)
#                 answer = str(input('请问猜大还是小？'))
#                 if (ran1+ran2>6 and answer =='大') or (ran1+ran2<=6 and answer =='小'):
#                     print('恭喜，猜对了！')
#                     coins += 2
#                 else:
#                     print('抱歉，猜错了。')
#                 count += 1
#                 join = input('是否继续游戏？（y/n）:')
#             print(f'金币余额{coins}, 共参加了{count}局游戏。')
#             break
#         else:
#             print("请充值10元的倍数")


# 定义一个函数，用于执行基本的数学运算
# def calculate(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         return num1 / num2
#     else:
#         return None
#
# # 主程序
# flag = 'y'
# while flag.upper() == ('Y'):
#     # 获取用户输入的数值和运算符
#     num1 = float(input("请输入第一个数："))
#     operator = input("请输入运算符号（+、-、*、/）：")
#     num2 = float(input("请输入第二个数："))
#
#     # 调用calculate函数执行运算，并输出结果
#     result = calculate(num1, num2, operator)
#     if result is not None:
#         print("计算结果为：", result)
#     else:
#         print("输入的运算符号不正确，请重新输入！")
#
#     # 询问用户是否继续运算
#     flag = input("是否继续运算？（y/n）")

# def my_sum_function(*args):
#     print(sum(args))

# def self_defined_function(*args, **kwargs):
#     if "denominator" not in kwargs:
#         print(sum(args))
#     else:
#         # 注意：kwargs的类型是字典
#         denominator = kwargs["denominator"]
#         print(sum(args) / denominator)
#
# # 没有denominator时，打印几个数的和
# self_defined_function(1, 2, 3)
# # 有denominator时，先求几个数的和，再除以denominator
# self_defined_function(1, 2, 3, denominator=3)

# csv文件操作
# import csv
#
# # 读取
# with open("data/students.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#     # rows = [row for row in reader]
#
# # 写入
# data = [
#     ('name', 'age', 'gender'),
#     ('Jane', '16', 'F'),
#     ('Tom', '14', 'M'),
#     ('Leon', '15', 'M'),
# ]
#
# # 覆盖写入
# with open('data/student-1.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
#
# # 追加写入
# with open('data/students.csv', 'a', newline='') as f:
#     writer = csv.writer(f,)
#     writer.writerows(data)







