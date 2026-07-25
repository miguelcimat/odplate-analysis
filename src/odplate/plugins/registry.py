from __future__ import annotations
from collections.abc import Callable
from typing import Any

class Registry:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._items: dict[str, Any] = {}

    def register(self, obj=None, *, name: str | None = None):
        def decorator(value):
            key = name or getattr(value, '__name__', value.__class__.__name__)
            if key in self._items and self._items[key] is not value:
                raise ValueError(f"Ya existe {key!r} en el registro {self.nombre}.")
            self._items[key] = value
            return value
        return decorator(obj) if obj is not None else decorator

    def get(self, name: str):
        try:
            return self._items[name]
        except KeyError as exc:
            disponibles=', '.join(sorted(self._items)) or 'ninguno'
            raise KeyError(f"No existe {name!r} en {self.nombre}. Disponibles: {disponibles}.") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._items))

metric_registry = Registry('métricas')
model_registry = Registry('modelos')
plot_registry = Registry('gráficas')
ranking_registry = Registry('criterios de ranking')

registrar_metrica = metric_registry.register
registrar_modelo = model_registry.register
registrar_grafica = plot_registry.register
registrar_criterio = ranking_registry.register
