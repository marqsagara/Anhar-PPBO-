from abc import ABC, abstractmethod

# 1. Buat kelas abstrak (tidak bisa langsung digunakan)
class Hero(ABC):
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp

    @abstractmethod
    def active_skill(self):
        pass

    @abstractmethod
    def passive_skill(self):
        pass

    @abstractmethod
    def ulti(self):
        pass

# 2. Buat subclass yang mengimplementasikan semua metode abstrak
class Marksman(Hero):
    def active_skill(self):
        print(f"{self.name} menyerang dengan serangan jarak jauh!")

    def passive_skill(self):
        print(f"{self.name} mendapatkan efek critical damage!")

    def ulti(self):
        print(f"{self.name} mengeluarkan tembakan mematikan!")

# 3. Buat objek dari subclass
layla = Marksman("Layla", 210, 1600)

# 4. Gunakan objek tersebut
layla.active_skill()
layla.passive_skill()
layla.ulti()
