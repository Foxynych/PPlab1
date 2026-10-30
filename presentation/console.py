from application.music_service import MusicService


class ConsoleApp:
    """Ввод и вывод: здесь нет бизнес-правил и работы с JSON."""

    def __init__(self, service: MusicService):
        self.service = service

    def run(self) -> None:
        while True:
            print("\n=== МУЗЫКАЛЬНЫЙ РЕДАКТОР ===")
            print("1. Показать треки")
            print("2. Добавить трек")
            print("3. Воспроизвести трек")
            print("4. Добавить в избранное")
            print("5. Удалить трек")
            print("0. Выход")
            choice = input("Выберите действие: ").strip()
            try:
                if choice == "1":
                    self._show_tracks()
                elif choice == "2":
                    self._add_track()
                elif choice == "3":
                    track = self.service.play_track(int(input("ID трека: ")))
                    print(f"Играет: {track.artist} — {track.title}")
                elif choice == "4":
                    track = self.service.like_track(int(input("ID трека: ")))
                    print(f"В избранном: {track.title}")
                elif choice == "5":
                    self.service.delete_track(int(input("ID трека: ")))
                    print("Трек удалён")
                elif choice == "0":
                    print("До свидания!")
                    return
                else:
                    print("Неизвестная команда")
            except ValueError as error:
                print(f"Ошибка: {error}")
            except (EOFError, KeyboardInterrupt):
                print("\nВыход")
                return

    def _show_tracks(self) -> None:
        tracks = self.service.list_tracks()
        if not tracks:
            print("Треков пока нет")
            return
        for track in tracks:
            mark = "♥" if track.liked else " "
            print(
                f"{track.id}. [{mark}] {track.artist} — {track.title} "
                f"({self._fmt(track.duration)}, прослушиваний: {track.play_count})"
            )

    def _add_track(self) -> None:
        title = input("Название: ")
        artist = input("Исполнитель: ")
        duration = int(input("Длительность в секундах: "))
        track = self.service.add_track(title, artist, duration)
        print(f"Добавлен трек #{track.id}")

    @staticmethod
    def _fmt(seconds: int) -> str:
        return f"{seconds // 60}:{seconds % 60:02d}"