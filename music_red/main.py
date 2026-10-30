from pathlib import Path

from application.music_service import MusicService
from infrastructure.json_repository import JsonTrackRepository
from presentation.console import ConsoleApp


def main() -> None:
    repository = JsonTrackRepository(Path(__file__).parent / "tracks.json")
    service = MusicService(repository)
    app = ConsoleApp(service)
    app.run()


if __name__ == "__main__":
    main()
