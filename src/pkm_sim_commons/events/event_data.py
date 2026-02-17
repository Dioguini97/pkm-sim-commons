from dataclasses import dataclass, field
from typing import Any, List, Optional, Dict

# from src.models.move import Any
# from src.models.pokemon import Any
# from pkm_sim_commons import Status

@dataclass
class EventData:

    # Referencias principais
    pokemon: Any = None
    battle: Any = None

    # Dados especificos do move
    move: Any = None
    attacker: Any = None
    defender: Any | List[Any] = None
    target_slot: Optional[int] | List[int] = None

    # Dados de dano
    damage: int = 0
    original_damage: int = 0
    is_critical: bool = False
    effectiveness: float = 1.0

    # Dados de Status
    status: Optional[str] = None
    status_turn: int = 0

    # Dados de stats
    stat_name: Optional[str] = None
    stat_change: int = 0
    old_stage: int = 0
    new_stage: int = 0

    # Dados de field
    weather: Optional[str] = None
    terrain: Optional[str] = None
    weather_turns: int = 0
    terrain_turns: int = 0

    # Dados de item/ability
    item: Optional[str] = None
    ability: Optional[str] = None

    # Dados de switch
    pokemon_in: Any = None
    pokemon_out: Any = None
    slot_index: Optional[int] = None

    # Metadados
    turn_number: int = 0
    priority: int = 0
    success: bool = True

    # Dados extras flexíveis
    extra: Dict[str, Any] = field(default_factory=dict)

    # Flag de controle
    cancel: bool = False  # Se True, cancela a ação

