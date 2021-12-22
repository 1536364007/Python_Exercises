import random

human_option = 0
bot_option = 0
human_input = input('*' * 25 + '\n      请输入要猜的拳：\n    剪刀，石头，还是布？\n' + '*' * 25)


class Game:
    class Bot:
        def __init__(self, output):
            self.bot_choice = output

        def bot_turn(self):
            self.bot_choice = random.choice(['石头', '剪刀', '布'])

    class Human:
        def __init__(self, out):
            self.human_choice = out

        def human_turn(self):
            self.human_choice = human_input

    class Analyse(Bot, Human):
        def output_the_result(self):
            global human_option, bot_option
            if self.human_choice == self.bot_choice:
                human_option = 1
                bot_option = 1
                print(f'人类的选择是{self.human_choice}\n机器人的选择是{self.bot_choice}\n该次游戏平局.')
            elif self.human_choice == '石头' and self.bot_choice == '剪刀':
                human_option = 1
                bot_option = 0
                print(f'人类的选择是{self.human_choice}\n机器人的选择是{self.bot_choice}\n该次游戏人类赢!')
            elif self.human_choice == '石头' and self.bot_choice == '布':
                human_option = 0
                bot_option = 1
                print(f'人类的选择是{self.human_choice}\n机器人的选择是{self.bot_choice}\n该次游戏机器人赢!')
            elif self.human_choice == '剪刀' and self.bot_choice == '石头':
                human_option = 0
                bot_option = 1
                print(f'人类的选择是{self.human_choice}\n机器人的选择是{self.bot_choice}\n该次游戏机器人赢!')
            elif self.human_choice == '剪刀' and self.bot_choice == '布':
                human_option = 1
                bot_option = 0
                print(f'人类的选择是{self.human_choice}\n机器人的选择是{self.bot_choice}\n该次游戏人类赢!')
            elif self.human_choice == '布' and self.bot_choice == '石头':
                human_option = 1
                bot_option = 0
                print(f'人类的选择是{self.human_choice}\n机器人的选择是{self.bot_choice}\n该次游戏人类赢!')
            elif self.human_choice == '布' and self.bot_choice == '剪刀':
                human_option = 0
                bot_option = 1
                print(f'人类的选择是{self.human_choice}\n机器人的选择是{self.bot_choice}\n该次游戏机器人赢!')


def final_result():
    bot = Game.Bot(random.choice(['石头', '剪刀', '布']))
    human = Game.Human(human_input)
    result = Game.Analyse()
    # 第59行有报错,括号内缺少名为output的变量


final_result()
# The finished version is released and it is called 'The_game_V2(finished).py'.
# Maybe you can go and have a look of that file.
