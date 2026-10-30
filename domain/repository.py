from abc import ABC, abstractmethod

from domain.track import Track


class TrackRepository(ABC):
    """Контракт хранения треков. Бизнес-логика не знает о JSON."""

    @abstractmethod
    def get_all(self) -> list[Track]:
        pass

    @abstractmethod
    def save_all(self, tracks: list[Track]) -> None:
        pass
