from dataclasses import dataclass


@dataclass
class Track:
    id: int
    title: str
    artist: str
    duration: int          # секунды
    play_count: int = 0
    isLiked: bool = False