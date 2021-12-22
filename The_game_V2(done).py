#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ！！！写在前面：！！！
# 请不要轻易删除空行或增添空行，容易产生弱警告，在如下版本：
# PyCharm 2021.3 (Professional Edition)
# Build #PY-213.5744.248, built on November 30, 2021
# 中，按照此缩进及空行的个数来看，并无任何弱警告以及红色警告，请勿随意修改，以保证程序的完美运行以及看起来的完美。
import random
# 导入random ‘随机’函数，用于增添人机随机输出‘石头，剪刀，布’的操作。
import sys
# 导入sys模块，负责与 Python 解释器进行交互，该模块提供了一系列用于控制 Python 运行环境的函数和变量。
option = 0
# 设定一个名为option的空变量，该变量用于控制下方的人机猜拳游戏整体流程及下一步去向。


class Analyse:
    # 定义一个分析游戏的类，名为Analyse，用于分析人类和机器人猜拳的输入值，并且输出一个结果
    def __init__(self, bot, human):
        # 添加一个构造方法(构造函数)，该方法是一个特殊的类实例方法
        # 该方法用于创建对象时使用，每当创建一个类的实例对象时，Python 解释器都会自动调用它。
        self.bot_choice = bot
        # 定义一个self变量，接受机器人猜拳的输入值
        self.human_choice = human
        # 定义一个self变量，接受人类猜拳的输入值

    def get_the_result(self):
        # 编写一个方法，用于分析&计算人机猜拳的结果。
        if self.bot_choice == self.human_choice:
            # 在人类和机器人出拳一致的情况下
            print('-' * 25 + f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局平局！\n' + '-' * 25)
            # 输出人类和机器人的猜拳输入值，并且输出结果（平局）
        elif self.bot_choice == '石头' and self.human_choice == '剪刀':
            # 在人类出剪刀，机器人出石头的情况下
            print('-' * 25 + f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局机器人赢！\n' + '-' * 25)
            # 输出人类和机器人的猜拳输入值，并且输出结果（机器人赢）
        elif self.bot_choice == '石头' and self.human_choice == '布':
            # 在人类出布，机器人出石头的情况下
            print('-' * 25 + f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局人类赢！\n' + '-' * 25)
            # 输出人类和机器人的猜拳输入值，并且输出结果（人类赢）
        elif self.bot_choice == '剪刀' and self.human_choice == '石头':
            # 在人类出石头，机器人出剪刀的情况下
            print('-' * 25 + f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局人类赢！\n' + '-' * 25)
            # 输出人类和机器人的猜拳输入值，并且输出结果（人类赢）
        elif self.bot_choice == '剪刀' and self.human_choice == '布':
            # 在人类出布，机器人出剪刀的情况下
            print('-' * 25 + f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局机器人赢！\n' + '-' * 25)
            # 输出人类和机器人的猜拳输入值，并且输出结果（机器人赢）
        elif self.bot_choice == '布' and self.human_choice == '石头':
            # 在人类出石头，机器人出布的情况下
            print('-' * 25 + f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局机器人赢！\n' + '-' * 25)
            # 输出人类和机器人的猜拳输入值，并且输出结果（机器人赢）
        elif self.bot_choice == '布' and self.human_choice == '剪刀':
            # 在人类出剪刀，机器人出布的情况下
            print('-' * 25 + f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局人类赢！\n' + '-' * 25)
            # 输出人类和机器人的猜拳输入值，并且输出结果（人类赢）


def final():
    # 添加一个def封装函数，名为final，涵盖如下内容：
    # 人类的输入值，用名为run的对象名称调用Analyse类，并调用Analyse类里名为get_the_result的方法
    human_input = input('*' * 25 + '\n      请输入要猜的拳：\n    剪刀，石头，还是布？\n' + '*' * 25)
    # 此时输入一个人类猜拳的输入值，即你猜的拳
    run = Analyse(random.choice(('石头', '剪刀', '布')), human_input)
    # 用名为run的对象调用Analyse类，并在括号内输入机器人和人类的猜拳输入值
    # 机器人的猜拳输入值为：在‘石头’，‘剪刀’，‘布’中随机选择一项
    # 人类的猜拳输入值为：在上方的human_input中输入的即为人类的猜拳输入值
    # 在输入人类和机器人的猜拳输入值后，中间要加入‘，’(逗号)作为分隔，
    # 如果不想出现弱警告，则要在逗号后补充一个空格
    run.get_the_result()
    # 用对象名称加‘.’(点)的方式调用类内的方法，即class内的def封装函数
    # 在此处调用的是Analyse类里的get_the_result方法，
    # 该方法(get_the_result)的作用：分析人类和机器人的猜拳，输出结果


def circle_the_game():
    # 添加一个def封装函数，用于循环游戏内容，直至玩家自行选择退出
    global option
    # 将option这个变量设为全局变量，否则会有一个弱警告，提示为“从外部范围隐藏名称‘option’”
    option = input('请输入你的选项：\n[1]开始猜拳\n[2]退出')
    # 设置option为该游戏的循环选项，用option这个变量来控制游戏流程走向
    while True:
        # 开始一直循环
        if option == '1':
            # 当option这个选项为1的时候，即游戏流程为双分支的一支时
            final()
            # 运行final这个封装函数
            circle_the_game()
            # 运行circle_the_game封装函数
            # 如果不添加这一封装函数，程序走到这一单分支时不会返回主函数
            # 即:程序会一直让玩家与机器人猜拳，不会返回游戏主界面，不能选择退出。
        elif option == '2':
            # 当option这个选项为2的时候，即游戏流程为双分支的另一分支时
            sys.exit()
            # 调用sys模块中的exit方法，退出该程序


circle_the_game()
# 在此调用circle_the_game封装函数
# 即调用游戏主程序，开始进行人机猜拳游戏。
