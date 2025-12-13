# Templatenya
class Hero:
    def __init__(self,inputNama,inputanHealth,inputanPower,inputanArmor):
        self.name = inputNama
        self.health = inputanHealth
        self.power = inputanPower
        self.armor = inputanArmor

hero1 = Hero("Sniper",100,12,20)
hero2 = Hero("Bambang",200,300,0)
hero3 = Hero("Ucup",1000,1000,1000)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)