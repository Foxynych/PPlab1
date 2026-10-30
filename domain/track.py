from dataclasses import dataclass


@dataclass
class Track:
    id: int
    title: str
    artist: str
    duration: int
    isLiked: bool = False
