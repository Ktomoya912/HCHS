from typing import Literal


class EffectType:
    """
    キャラクターのステータスの種類を表すクラス

    CTとは、Currentの略で、現在のステータスを表す。
    """

    MAX_HP = "max_hp"
    DAMAGE = "damage"
    DEFENSE = "defense"
    SPEED = "speed"
    MP = "mp"
    CRITICAL_CHANCE = "critical_chance"
    CRITICAL_DAMAGE = "critical_damage"

    CT_HP = "current_hp"
    CT_DAMAGE = "current_damage"
    CT_DEFENSE = "current_defense"
    CT_SPEED = "current_speed"
    CT_MP = "current_mp"
    CT_CRITICAL_CHANCE = "current_critical_chance"
    CT_CRITICAL_DAMAGE = "current_critical_damage"


class Target:
    """
    スキルの対象を表すクラス

    Parameters
    ----------
    SELF : str
        自分自身
    ENEMY : str
        敵 (単体)
    ALLY : str
        味方 (単体)
    ALL_ALLIES : str
        味方 (全体)
    ALL_ENEMIES : str
        敵 (全体)
    """

    SELF = "self"
    ENEMY = "enemy"
    ALLY = "ally"
    ALL_ALLIES = "all_allies"
    ALL_ENEMIES = "all_enemies"


class Skill:
    def __init__(
        self,
        name: str,
        effect_type: EffectType,
        target: Literal["self", "enemy", "ally", "all_allies", "all_enemies"],
        value: int,
        cost: int,
        hit_rate: float = 1,
        duration: int = 0,
    ):
        """スキルの情報を保持するクラス

        Parameters
        ----------
        name : str
            スキルの名前
        effect_type : str
            スキルの効果の種類
        target : Literal["self", "enemy", "ally", "all_allies", "all_enemies"]
            スキルの対象
        value : int
            スキルの効果量
        cost : int
            スキルのコスト
        hit_rate : float, optional
            スキルの命中率, by default 1
        duration : int, optional
            スキルの効果の持続ターン数, by default 0
        """
        self.name = name
        self.effect_type = effect_type
        self.target = target
        self.value = value
        self.cost = cost
        self.hit_rate = hit_rate
        self.duration = duration


fireball = Skill("Fireball", EffectType.CT_HP, Target.ENEMY, 10, 5)
mini_heal = Skill("Mini Heal", EffectType.CT_HP, Target.SELF, 5, 3)
shield = Skill("Shield", EffectType.CT_DEFENSE, Target.SELF, 5, 3, duration=3)
poison = Skill("Poison", EffectType.CT_HP, Target.ENEMY, 3, 3, duration=3)
regen = Skill("Regen", EffectType.CT_HP, Target.SELF, 2, 2, duration=3)
thunder = Skill("Thunder", EffectType.CT_HP, Target.ALL_ENEMIES, 5, 5)
take_down = Skill("Take Down", EffectType.CT_HP, Target.ENEMY, 20, 10, hit_rate=0.7)
dragon_breath = Skill("Dragon Breath", EffectType.CT_HP, Target.ALL_ENEMIES, 15, 10)
