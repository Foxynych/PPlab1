import json
from pathlib import Path

from domain.repository import TrackRepository
from domain.track import Track


class JsonTrackRepository(TrackRepository):
    """Реализация хранения треков в JSON-файле."""

    def __init__(self, path: Path):
        self.path = path

    def get_all(self) -> list[Track]:
        if not self.path.exists():
            return []
        
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [Track(**item) for item in data]

    def save_all(self, tracks: list[Track]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = [
            dict(
                id=t.id,
                title=t.title,
                artist=t.artist,
                duration=t.duration,
                liked=t.isLiked,
            )
            for t in tracks
        ]

        self.path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
