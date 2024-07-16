import random

import skill


class Character:
    def __init__(
        self,
        name,
        hp,
        damage,
        skills: list[skill.Skill],
        defence=0,
        critical_chance=0.1,
        critical_damage=2,
        is_enemy=False,
    ):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.damage = damage
        self.skills = skills
        self.defence = defence
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.is_enemy = is_enemy

    def __str__(self):
        return f"{self.name} has {self.current_hp} hp and {self.damage} damage"

    def attack(self, other_character: "Character"):
        if random.random() < self.critical_chance:
            damage = self.damage * self.critical_damage
            print(f"{self.name} attacked {other_character.name} with critical hit")
        else:
            damage = self.damage

        other_character.recieve_damage(damage)

    def recieve_damage(self, damage: int):
        damage = max(0, damage - self.defence)
        self.current_hp -= damage
        print(f"{self.name} recieved {damage} damage")

    def get_status(self):
        print(f"{self.name} has {self.current_hp} left")

    @property
    def is_alive(self):
        return self.current_hp > 0


class Hero(Character):
    def __init__(
        self, name, hp, damage, defence=0, critical_chance=0.1, critical_damage=2
    ):
        super().__init__(name, hp, damage, defence, critical_chance, critical_damage)


class Monster(Character):
    def __init__(
        self, name, hp, damage, defence=0, critical_chance=0.1, critical_damage=2
    ):
        super().__init__(
            name, hp, damage, defence, critical_chance, critical_damage, is_enemy=True
        )
