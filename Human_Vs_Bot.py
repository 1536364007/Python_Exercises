#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


# 调用random随机模块


class HumanBeing:
    # 定义一个玩家的类，用于导入和分析玩家的出拳
    def process(self):
        # 定义一个方法，用于导入玩家的出拳
        while True:
            # 设定一个循环
            h_choice = input('-' * 25 + '\n人机猜拳游戏开始！\n·请输入你的选项(输入序号即可)：\n[1]石头\n[2]剪刀\n[3]布\n' + '-' * 25)
            # 将玩家的出拳赋值给h_choice这个变量
            if h_choice.isdigit():
                # 如果h_choice这个变量是数字的话，则执行以下操作
                h_choice = int(h_choice)
                # 将h_choice变量里的数字转换为整形
                if h_choice == 1:
                    # 当该变量为1时
                    print('人类的出拳是：石头')
                    # 输出玩家的猜拳
                    break
                    # 跳出循环
                elif h_choice == 2:
                    # 当该变量为2时
                    print('人类的出拳是：剪刀')
                    # 输出玩家的猜拳
                    break
                    # 跳出循环
                elif h_choice == 3:
                    # 当该变量为3时
                    print('人类的出拳是：布')
                    # 输出玩家的猜拳
                    break
                    # 跳出循环
                else:
                    print('输入错误，请重新输入！')
                    # 如果输入的不是上述数字（1，2,3），则要求重新输入，直至输入1,2,3中的任意一个。
            else:
                print('输入错误，请重新输入！')
                # 当玩家输入的不是数字时，则要求重新输入，直至输入数字。
        return h_choice
        # 返回玩家猜拳的输入值


class Bot:
    # 定义一个机器人的类，用于获取随机值并进行分析。
    def stochastic(self):
        # 定义一个分析随机值的方法
        b_choice = random.randint(1, 3)
        # 给予b_choice这个变量一个从1,2,3中的随机值
        if b_choice == 1:
            # 如果该变量为1
            print('机器人的出拳为：石头')
            # 则输出机器人的猜拳
        elif b_choice == 2:
            # 如果该变量为2
            print('机器人的出拳为：剪刀')
            # 则输出机器人的猜拳
        else:
            # 剩下一种情况，给予的随机值为3
            print('机器人的出拳为：布')
            # 输出机器人的猜拳
        return b_choice
        # 返回机器人猜拳的输入值


class Operation:
    # 定义一个操作的类，用于对玩家和机器人的猜拳输入值进行分析，并得出结论。
    h_number_of_wins = 0
    # 定义一个玩家获胜次数的变量
    b_number_of_wins = 0
    # 定义一个机器人获胜次数的变量
    no_wins = 0
    # 定义一个平局变量
    rounds = 0

    # 定义一个总游戏次数的变量

    def game_on(self):
        # 定义一个开始游戏的方法
        global result
        # 将result(结果)设置为全局变量，如若不然，则会在使用.format函数调用时产生警告
        # 并提示“局部变量‘result’可能在赋值前引用”，故在此将result设为全局变量
        human = HumanBeing()
        # 将玩家的类用名为human的对象来调用
        bot = Bot()
        # 将机器人的类用名为bot的对象来调用
        while True:
            # 设定一个循环，运行游戏主程序
            h_result = human.process()
            # 用“对象名.方法名”（在此之前需使用“对象名=类名()”来调用类）的方法调用玩家的猜拳，得到玩家的猜拳
            b_result = bot.stochastic()
            # 用“对象名.方法名”（在此之前需使用“对象名=类名()”来调用类）的方法调用机器人的猜拳，得到机器人的猜拳
            if h_result == b_result:
                # 开始进行多判断分支中的一支：当玩家和机器人出拳相同时
                self.no_wins += 1
                # 平局次数加一
                self.rounds += 1
                # 游戏次数加一
                print('-' * 25 + f'哦，无人胜出！这是第{self.no_wins}次平局.')
                # 输出游戏结果（平局，平局次数）
            elif b_result == 1 and h_result == 2 or \
                    b_result == 2 and h_result == 3 or \
                    b_result == 3 and h_result == 1:
                # 开始进行多判断分支中的一支：当机器人胜过玩家时：
                self.b_number_of_wins += 1
                # 机器人获胜次数加一
                self.rounds += 1
                # 游戏次数加一
                print('-' * 25 + f'抱歉，机器人赢了!这是机器人第{self.b_number_of_wins}次胜利.')
                # 输出游戏结果（机器人获胜，机器人获胜次数）
            elif b_result == 1 and h_result == 3 or \
                    b_result == 2 and h_result == 1 or \
                    b_result == 3 and h_result == 2:
                # 开始进行多判断分支中的一支：当玩家胜过机器人时：
                self.h_number_of_wins += 1
                # 玩家获胜次数加一
                self.rounds += 1
                # 游戏次数加一
                print(f'真幸运，人类获胜！这是人类第{self.h_number_of_wins}次胜利.')
                # 输出游戏结果（玩家获胜，玩家获胜次数）
            if input('-' * 25 + "\n请问，是否需要继续进行游戏呢？\n输入'N'来结束游戏。\n输入其他字符以继续游戏.\n" + '-' * 25).capitalize() == 'N':
                # 当一局游戏结束时，设定程序询问是否需要继续游戏，输入大写/小写'N‘来退出游戏并显示最终统计数据，输入其他字符则继续游戏。
                break
                # 跳出循环
        if self.h_number_of_wins > self.b_number_of_wins:
            # 开始进入多分支判断的一支：如果整场游戏中玩家获胜次数大于机器人获胜次数：
            result = '人类胜场较多，人类获胜。'
            # 则定义一个result参数来传入人机猜拳游戏结果（玩家获胜）
        elif self.b_number_of_wins > self.h_number_of_wins:
            # 开始进入多分支判断的一支：如果整场游戏中机器人获胜次数大于玩家获胜次数：
            result = '机器人胜场较多，机器人获胜。'
            # 则定义一个result参数来传入人机猜拳游戏结果（机器人获胜）
        elif self.b_number_of_wins == self.h_number_of_wins:
            # 开始进入多分支判断的一支：如果整场游戏中玩家获胜次数等于机器人获胜次数：
            result = '该次游戏平局！'
            # 则定义一个result参数来传入人机猜拳游戏结果（平局）
        h_percentage = round(self.h_number_of_wins / self.rounds * 10 ** 2, 2)
        # 定义一个h_percentage的变量来传入玩家的获胜概率（用round()函数来对数字进行取小数点后两位操作，避免显示百分率的数字过长）
        b_percentage = round(self.b_number_of_wins / self.rounds * 10 ** 2, 2)
        # 定义一个b_percentage的变量来传入机器人的获胜概率（用round()函数来对数字进行取小数点后两位操作，避免显示百分率的数字过长）
        n_percentage = round(self.no_wins / self.rounds * 10 ** 2, 2)
        # 定义一个n_percentage的变量来传入平局概率（用round()函数来对数字进行取小数点后两位操作，避免显示百分率的数字过长）
        print("\n人机猜拳游戏结束\n结果为：\n一共比赛{0}次\n玩家获胜{1}次,获胜概率为{2}%"
              "\n机器人获胜{3}次,获胜概率为{4}%"
              "\n平局{5}次,平局概率为{6}\n\n结局为{7}".format(self.rounds, self.h_number_of_wins, h_percentage,
                                                   self.b_number_of_wins,
                                                   b_percentage, self.no_wins, n_percentage,
                                                   result))
        # 最终输出游戏结果及整场游戏统计数据（玩家获胜次数，玩家获胜概率，机器人获胜次数，机器人获胜概率，平局次数，平局概率，最终获胜者）


The_game = Operation().game_on()
# 用名为The_game的对象调用实例化Operation类(游戏本体)和其中的game_on方法(开始游戏，并进行数据分析)
# 如果此处不用对象调用实例化类和其中的方法，也可以正常运行，并且可以减少一个弱警告。
# 所以主程序的最后一行名为“The_game"的对象名可以删掉，也可以保留，如若要删除，记得删掉'='和它前后的空格，以保证缩进无误。
