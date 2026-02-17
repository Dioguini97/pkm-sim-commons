from typing import Callable, Dict, List

from .event_data import EventData
from ..enums.battle_events import BattleEvent


class EventBus:

    def __init__(self, enable_logging: bool = False):
        self._handlers: Dict[BattleEvent, List[Callable]] = {}

        self._priority_handlers: Dict[BattleEvent, List[tuple[ int, Callable]]] = {}

        self.enable_logging = enable_logging
        self._event_log: List[tuple[BattleEvent, EventData]] = []

    def subscribe(self, event: BattleEvent, handler: Callable[[EventData], None], priority: int = 0):
        """
            Registra um handler para um evento

            Args:
                event: Tipo de evento a escutar
                handler: Função que será chamada quando evento ocorrer
                priority: Prioridade de execução (maior = primeiro)
                         0 = prioridade normal
                         >0 = alta prioridade (abilities que cancelam, etc)
                         <0 = baixa prioridade (logging, etc)

            Example:
                def on_damage(event_data):
                    print(f"Dano: {event_data.damage}")

                event_bus.subscribe(BattleEvent.AFTER_DAMAGE, on_damage)
        """
        if priority == 0:
            if event not in self._handlers:
                self._handlers[event] = []
            self._handlers[event].append(handler)
        else:
            if event not in self._priority_handlers:
                self._priority_handlers[event] = []
            self._priority_handlers[event].append((priority, handler))

            self._priority_handlers[event].sort(
                key=lambda x: x[0],
                reverse=True
            )

    def unsubscribe(self, event: BattleEvent, handler: Callable):
        """
            Remove um handler específico de um evento

            Args:
                event: Tipo de evento
                handler: Função handler a remover
        """

        if event in self._handlers and handler in self._handlers[event]:
            self._handlers[event].remove(handler)

            if not self._handlers[event]:
                del self._handlers[event]

        if event in self._priority_handlers:
            self._priority_handlers[event] = [
                (p, h) for p, h in self._priority_handlers[event] if h != handler
            ]

            if not self._priority_handlers[event]:
                del self._priority_handlers[event]

    def unsubscribe_all(self, event: BattleEvent):
        """Remove TODOS os handlers de um evento"""
        if event in self._handlers:
            del self._handlers[event]
        if event in self._priority_handlers:
            del self._priority_handlers[event]

    def emit(self, event: BattleEvent, event_data: EventData) -> EventData:
        """
        Dispara um evento e executa todos os handlers registrados

        Args:
            event: Tipo de evento
            event_data: Dados do evento

        Returns:
            O mesmo event_data (possivelmente modificado pelos handlers)

        Flow:
            1. Executa handlers com alta prioridade primeiro
            2. Se algum handler cancelar (event_data.cancel = True), para
            3. Executa handlers normais
            4. Loga evento se logging estiver ativo
            5. Retorna event_data modificado
        """

        if self.enable_logging:
            self._event_log.append((event, event_data))

        if event in self._priority_handlers:
            for priority, handler in self._priority_handlers[event]:
                try:
                    handler(event_data)
                except Exception as e:
                    print(f"❌ Error in priority handler for {event.value}: {e}")

                if event_data.cancel:
                    return event_data

        if event in self._handlers:
            for handler in self._handlers[event]:
                try:
                    handler(event_data)
                except Exception as e:
                    print(f"❌ Error in handler for {event.value}: {e}")

                if event_data.cancel:
                    return event_data

        return event_data