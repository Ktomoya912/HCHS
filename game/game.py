import random
from random import Random


class Character:
    def __init__(self, name, hp, damage, defense=0, critical=10):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.damage = damage
        self.defense = defense
        self.critical = critical

    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = value
        if self._current_hp > self.max_hp:
            self._current_hp = self.max_hp
        elif self._current_hp < 0:
            self._current_hp = 0

    def attack(self, target: "Character"):
        gain = random.randint(0, 100)
        damage = self.damage
        if gain < self.critical:
            damage *= 2
            print("クリティカルヒット！")
        result = target.damaged(damage)
        print(f"{self.name} は {target.name} に {result} ダメージを与えた！")

    def damaged(self, damage: int):
        gain = max(1, damage - self.defense)
        self.current_hp -= gain
        print(f"{self.name} は {gain} ダメージを受けた！")
        print(self)
        return gain

    @property
    def is_dead(self):
        return self.current_hp <= 0

    def __str__(self):
        bar_length = 10
        damage_rate = self.current_hp / self.max_hp
        bar = "#" * int(damage_rate * bar_length) + "-" * (
            bar_length - int(damage_rate * bar_length)
        )
        return f"{self.name}: {self.current_hp}/{self.max_hp} [{bar}]"


enemies = [
    Character("Slime", 5, 1),
    Character("Metal Slime", 10, 2, 20),
    Character("Goblin", 10, 2),
    Character("Orc", 20, 5),
    Character("Troll", 50, 10, 5),
    Character("Dragon", 100, 20, 10),
]

player = Character("Hero", 100, 10, 5, 50)

if __name__ == "__main__":
    while True:
        enemy = random.choice(enemies)
        print(f"{enemy.name}が現れた！")
        while True:
            player.attack(enemy)
            if enemy.is_dead:
                print(f"{enemy.name} を倒した！")
                break
            enemy.attack(player)
            if player.is_dead:
                print(f"{player.name} は死んでしまった！")
                break
        if player.is_dead:
            break
        input("Press Enter to continue...")
