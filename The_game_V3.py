#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is another version of the game
# The author is tingyu_ from CSDN
# The original website is https://blog.csdn.net/tingyu_/article/details/104121974

import random  # 导包

print("********欢迎来到猜拳小游戏********")
while True:
    key = int(input("请输入您的出拳选项：1，剪刀。2，石头。3，布："))  # 从键盘上得到手势代号
    while key not in [1, 2, 3]:  # 判断当输入的手势代号是否符合要求，不符合要求时，重新输入
        print("您的输入有误，请重新输入")
        key = int(input("请输入您的出拳选项：1，剪刀。2，石头。3，布："))
    com_key = random.randint(1, 3)  # 利用随机函数随机生成1到3之间的整数
    if (key == 1 and com_key == 2) or (key == 2 and com_key == 3) or (key == 3 and com_key == 1):
        print("恭喜你啦，你赢了呦，加油！！！")
    elif key == com_key:
        print("此局是平局")
    else:
        print("真是遗憾呢，你输了。。。。")
    n = input("请输入n结束游戏或者输入其他字符继续游戏:")
    if n == "n":
        break
print("游戏结束")
