import random
import sys
option = 0


class Analyse:
    def __init__(self, bot, human):
        self.bot_choice = bot
        self.human_choice = human

    def get_the_result(self):
        if self.bot_choice == self.human_choice:
            print('-'*25+f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局平局！\n'+'-'*25)
        elif self.bot_choice == '石头' and self.human_choice == '剪刀':
            print('-'*25+f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局机器人赢！\n'+'-'*25)
        elif self.bot_choice == '石头' and self.human_choice == '布':
            print('-'*25+f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局人类赢！\n'+'-'*25)
        elif self.bot_choice == '剪刀' and self.human_choice == '石头':
            print('-'*25+f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局人类赢！\n'+'-'*25)
        elif self.bot_choice == '剪刀' and self.human_choice == '布':
            print('-'*25+f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局机器人赢！\n'+'-'*25)
        elif self.bot_choice == '布' and self.human_choice == '石头':
            print('-'*25+f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局机器人赢！\n'+'-'*25)
        elif self.bot_choice == '布' and self.human_choice == '剪刀':
            print('-'*25+f'\n人类的出拳是:{self.human_choice}\n机器人的出拳是:{self.bot_choice}\n这局人类赢！\n'+'-'*25)


def final():
    human_input = input('*' * 25 + '\n      请输入要猜的拳：\n    剪刀，石头，还是布？\n' + '*' * 25)
    run = Analyse(random.choice(('石头', '剪刀', '布')), human_input)
    run.get_the_result()


def circle_the_game():
    global option
    option = input('请输入你的选项：\n[1]开始猜拳\n[2]退出')
    while True:
        if option == '1':
            final()
            circle_the_game()
        elif option == '2':
            sys.exit()


circle_the_game()
