from random import randint
import random


class Unit:
    def __init__(self, hp, dmg, dodge, name):
        self.__hp = hp
        self.__dmg = dmg
        self.__dodge = dodge
        self.__name = name
    
    

    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, hp):
        self.__hp = hp
        return self.__hp

    @property
    def dmg(self):
        return self.__dmg
    
    @dmg.setter
    def dmg(self, dmg):
        self.__dmg = dmg
        return self.__dmg
    
    @property
    def dodge(self):
        return self.__dodge 

    @dodge.setter
    def dodge(self, dodge):
        self.__dodge = dodge
        return self.__dodge  

    
    # def show_info(self):
    #     print("HP: ", self.__hp, "\nDmg: ",
    #           self.__dmg, "\nDodge: ", self.__dodge) 

class Swordsman(Unit):
    def __init__(self, hp = 15, dmg = 5, dodge = 60, name = "Swordsman"):
        self.hp = int(hp)
        self.dmg = int(dmg)
        self.dodge = int(dodge)
        self.name = str(name)

class Archer(Unit):
    def __init__(self, hp = 12, dmg = 4, dodge = 40, name = "Archer"):
        self.hp = int(hp)
        self.dmg = int(dmg)
        self.dodge = int(dodge)
        self.name = str(name)

class Mage(Unit):
    def __init__(self, hp = 8, dmg = 10, dodge = 30, name = "Mage"):
        self.hp = int(hp)
        self.dmg = int(dmg)
        self.dodge = int(dodge)
        self.name = str(name)



def main():
    # print("Create team")
    alliance = []
    orcs = []
    
    for i in range(3):
        x = random.randint(0, 2)
        if x == 0:
            alliance.append(Swordsman())
        elif x == 1:
            alliance.append(Archer())
        elif x == 2:
            alliance.append(Mage())
    # print("alliance", alliance)
    
    for j in range(3):
        x = random.randint(0, 2)
        if x == 0:
            orcs.append(Swordsman())
        elif x == 1:
            orcs.append(Archer())
        elif x == 2:
            orcs.append(Mage())
    # print("orcs", orcs)
    return alliance, orcs

def start():
    opponents = main()
    alliance = opponents[0]
    orcs = opponents[1]
    hp_alliance = alliance[0].hp + alliance[1].hp + alliance[2].hp
    hp_orcs= orcs[0].hp + orcs[1].hp + orcs[2].hp
    print("War start")
    print("Light forces - Alliance: ", hp_alliance, "\nDark forces - Orcs: ", hp_orcs)


    while hp_alliance > 0 and hp_orcs > 0:
        choice_first = random.randint(0, 1)
        choice_warrior_attack = random.randint(0, 2)
        choice_warrior_protection = random.randint(0, 2)
        if choice_first == 0:
            print("\nAttacks alliance")
            input("\nPress enter to continue")
            if choice_warrior_attack == 0:
                attacks = alliance[0]
            elif choice_warrior_attack == 1:
                attacks = alliance[1]
            elif choice_warrior_attack == 2:
                attacks = alliance[2]

            if choice_warrior_protection == 0:
                protected = orcs[0]
            elif choice_warrior_protection == 1:
                protected = orcs[1]
            elif choice_warrior_protection == 2:
                protected = orcs[2]
            
            
            print(attacks.name, "Alliance attacks the", protected.name, "Orcs")
            fortune = randint(1, 100)
            if fortune > protected.dodge:
                print("The attack succeeded")
                print(protected.name, "lost", attacks.dmg, "life")
                hp_orcs = hp_orcs - attacks.dmg
                print("Light forces - Alliance: ", hp_alliance, "\nDark forces - Orcs: ", hp_orcs)
                print("**********************************")
            else:
                print("The attack failed. Defended Dodge")
                print("**********************************")


        else:
            print("\nAttacks orcs")
            input("\nPress enter to continue")
            if choice_warrior_attack == 0:
                attacks = orcs[0]
            elif choice_warrior_attack == 1:
                attacks = orcs[1]
            elif choice_warrior_attack == 2:
                attacks = orcs[2]

            if choice_warrior_protection == 0:
                protected = alliance[0]
            elif choice_warrior_protection == 1:
                protected = alliance[1]
            elif choice_warrior_protection == 2:
                protected = alliance[2]
            
            print(attacks.name, "Orcs attacks the", protected.name, "Alliance")
            fortune = randint(1, 100)
            if fortune > protected.dodge:
                print("The attack succeeded")
                print(protected.name, "lost", attacks.dmg, "life")
                hp_alliance = hp_alliance - attacks.dmg
                print("Light forces - Alliance: ", hp_alliance, "\nDark forces - Orcs: ", hp_orcs)
                print("**********************************")
            else:
                print("The attack failed. Defended Dodge")
                print("**********************************")

        

    if hp_alliance == 0:
        print("======= Game over ===========")
        print("!!!! Win Dark forces - Orcs !!!!")
    else:
        print("======= Game over ===========")
        print("!!!! Win Light forces - Alliance !!!!")

exit = False
while not exit:
    print("+++++++++++++++ ALLIANCE VS ORCS +++++++++++++++++++++++++++++")
    try:
        choise = int(input(" 1. Start the game\n 0. exit\n"))
        if choise == 1:
           main() 
           start()
                  
                     
        elif choise == 0:
            exit = True
        else:
            print("read manual")
    except Exception as error:
        print("ERROR ===> ", error)