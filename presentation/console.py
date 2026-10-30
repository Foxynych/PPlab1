from application.music_service import MusicService


class ConsoleApp:
    """Ввод и вывод: здесь нет бизнес-правил и работы с JSON."""

    def __init__(self, service: MusicService):
        self.service = service

    def run(self) -> None:
        while True:
            print("\n=== МУЗЫКАЛЬНЫЙ РЕДАКТОР ===")
            print("1. Показать треки")
            print("2. Показать избранные треки")
            print("3. Добавить трек")
            print("4. Воспроизвести трек")
            print("5. Добавить/удалить избранные")
            print("6. Удалить трек")
            print("0. Выход")
            choice = input("Выберите действие: ").strip()

            try:
                if choice == "1":
                    self.show_tracks()
                elif choice == "2":
                    self.show_liked_tracks()
                elif choice == "3":
                    self.add_track()
                elif choice == "4":
                    track = self.service.play_track(int(input("ID трека: ")))
                    print(f"Играет: {track.artist} — {track.title}")
                elif choice == "5":
                    track = self.service.un_like_track(int(input("ID трека: ")))
                elif choice == "6":
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

    def show_tracks(self) -> None:
        tracks = self.service.list_tracks()

        if not tracks:
            print("Треков пока нет")
            return
        
        for track in tracks:
            mark = "♥" if track.liked else " "
            print(
                f"{track.id}. [{mark}] {track.artist} — {track.title} "
                f"({self._fmt(track.duration)})"
            )

    def show_liked_tracks(self) -> None:
        tracks = self.service.list_tracks()
        flag = True

        if not tracks:
            print("Треков пока нет")
            return
        
        for track in tracks:
            if track.isLiked:
                flag = False

                print(
                    f"{track.id}. ♥ {track.artist} — {track.title} "
                    f"({self._fmt(track.duration)})"
                )

        if flag:
            print("Избранных треков пока нет =(")

    def add_track(self) -> None:
        try:
            title = input("Название: ")
            artist = input("Исполнитель: ")
            duration = int(input("Длительность в секундах: "))
            track = self.service.add_track(title, artist, duration)
            print(f"Добавлен трек #{track.id}")

        except ValueError as Error:
            print(f"Ошибка {Error}")

    @staticmethod
    def _fmt(seconds: int) -> str:
        return f"{seconds // 60}:{seconds % 60:02d}"
