class Hero:
    def stroke(self):
        pass

class Chengyaojin(Hero):
    def stroke(self):
        print("回血加攻击力")

class Xiangyu(Hero):
    def stroke(self):
        print("推人")


hero_index = input("请输入您要选择的英雄：")
hero = None
if hero_index == "1":
    hero = Chengyaojin()
else:
    hero = Xiangyu()

skill = input("请输入您的技能：")
if skill == "3":
    hero.stroke()