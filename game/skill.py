from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .game import Character


class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def __str__(self):
        return f"{self.name}: Damage {self.damage}, Cost {self.cost}"

    def use(self, user: "Character", target: "Character" = None):
        if user.current_hp < self.cost:
            print(f"{user.name} は {self.name} を使うのにコストが足りない！")
            return
        user.current_hp -= self.cost
        if not target:
            result = -self.damage
            user.current_hp += result
            print(f"{user.name} は {self.name} を使い {result} 回復した！")
        else:
            result = target.damaged(self.damage)
            print(
                f"{user.name} は {self.name} を使い {target.name} に {result} ダメージを与えた！"
            )


skills = [
    Skill("Fire", 5, 1),
    Skill("Ice", 10, 2),
    Skill("Thunder", 15, 3),
    Skill("Explosion", 20, 5),
    Skill("Heal", -10, 3),
]
