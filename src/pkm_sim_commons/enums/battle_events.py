from enum import Enum


class BattleEvent(Enum):

    # ===== TURN EVENTS ===== #
    TURN_START = 'turn_start'
    TURN_END = 'turn_end'

    # ===== MOVE EVENTS ===== #
    BEFORE_MOVE = "before_move"  # Antes de executar o movimento (pode cancelar)
    AFTER_MOVE = "after_move"  # Depois de executar o movimento
    MOVE_FAILED = "move_failed"  # Quando movimento falha
    MOVE_HIT = "move_hit"  # Quando movimento acerta
    MOVE_MISSED = "move_missed"  # Quando movimento erra
    MOVE_CRITICAL = "move_critical"  # Quando é crítico

    # ===== DAMAGE EVENTS =====
    BEFORE_DAMAGE = "before_damage"  # Antes de aplicar dano (pode modificar/cancelar)
    DAMAGE_CALCULATED = "damage_calculated"  # Dano calculado (pode modificar)
    AFTER_DAMAGE = "after_damage"  # Depois de aplicar dano

    # ===== HO EVENTS =====
    HP_CHANGED = "hp_changed"  # Sempre que HP muda (dano ou cura)
    HP_HEALED = "hp_healed"  # Quando cura HP
    FAINTED = "fainted"  # Quando Pokémon desmaia
    HP_LOWER_50_PERC = 'hp_lower_50_perc'
    HP_LOWER_33_PERC = 'hp_lower_33_perc'

    # ===== STATUS EVENTS =====
    STATUS_APPLIED = "status_applied"  # Quando status é aplicado
    STATUS_REMOVED = "status_removed"  # Quando status é removido
    STATUS_TICK = "status_tick"  # A cada turno com status (burn damage, etc)
    STATUS_PREVENTED = "status_prevented"  # Quando status é prevenido

    # ===== STATS EVENTS =====
    STAT_STAGE_CHANGED = "stat_stage_changed"  # Quando stages mudam
    STAT_STAGE_MAXED = "stat_stage_maxed"  # Quando atinge +6 ou -6

    # ===== SWITCH EVENTS =====
    SWITCH_IN = "switch_in"  # Pokémon entra em campo
    SWITCH_OUT = "switch_out"  # Pokémon sai de campo
    FORCED_SWITCH = "forced_switch"  # Switch forçado (Roar, Dragon Tail, etc)

    # ===== ITEMS EVENTS =====
    ITEM_USED = "item_used"  # Quando item é usado
    ITEM_CONSUMED = "item_consumed"  # Quando item é consumido
    BERRY_CONSUMED = "berry_consumed"  # Especificamente berries
    ITEM_ACTIVATED = "item_activated"  # Quando efeito do item ativa

    # ===== ABILITY EVENTS =====
    ABILITY_ACTIVATED = "ability_activated"  # Quando ability ativa
    ABILITY_SUPPRESSED = "ability_suppressed"  # Quando ability é suprimida
    ABILITY_CHANGED = "ability_changed"  # Quando ability muda (Skill Swap, etc)

    # ===== EVENTOS DE FIELD =====
    WEATHER_CHANGED = "weather_changed"  # Quando clima muda
    WEATHER_TICK = "weather_tick"  # A cada turno com clima
    WEATHER_ENDED = "weather_ended"  # Quando clima acaba

    TERRAIN_CHANGED = "terrain_changed"  # Quando terreno muda
    TERRAIN_TICK = "terrain_tick"  # A cada turno com terreno
    TERRAIN_ENDED = "terrain_ended"  # Quando terreno acaba

    TRICK_ROOM_START = "trick_room_start"
    TRICK_ROOM_END = "trick_room_end"

    GRAVITY_START = "gravity_start"
    GRAVITY_END = "gravity_end"

    # ===== EVENTOS DE HAZARDS =====
    HAZARD_SET = "hazard_set"  # Stealth Rock, Spikes, etc
    HAZARD_REMOVED = "hazard_removed"  # Rapid Spin, Defog
    HAZARD_TRIGGERED = "hazard_triggered"  # Quando Pokémon entra e toma dano

    # ===== EVENTOS DE SCREENS =====
    SCREEN_SET = "screen_set"  # Reflect, Light Screen
    SCREEN_ENDED = "screen_ended"

    # ===== EVENTOS DE VOLATILES =====
    CONFUSED = "confused"
    CONFUSION_ENDED = "confusion_ended"
    FLINCHED = "flinched"
    SEEDED = "seeded"
    TRAPPED = "trapped"

    # ===== EVENTOS DE BATALHA =====
    BATTLE_START = "battle_start"
    BATTLE_END = "battle_end"
    TEAM_PREVIEW = "team_preview"