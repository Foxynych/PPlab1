from domain.repository import TrackRepository
from domain.track import Track


class MusicService:
    """Бизнес-правила музыкального редактора."""

    def __init__(self, repository: TrackRepository):
        self.repository = repository

    def list_tracks(self) -> list[Track]:
        return self.repository.get_all()

    def add_track(self, title: str, artist: str, duration: int) -> Track:
        title = title.strip()
        artist = artist.strip()

        if not title:
            raise ValueError("Название трека не может быть пустым")
        if not artist:
            raise ValueError("Исполнитель не может быть пустым")
        if duration <= 0:
            raise ValueError("Длительность должна быть положительной")
        
        tracks = self.repository.get_all()
        next_id = max((track.id for track in tracks), default=0) + 1
        track = Track(id=next_id, title=title, artist=artist, duration=duration)
        tracks.append(track)
        
        self.repository.save_all(tracks)
        return track

    def play_track(self, track_id: int) -> Track:
        tracks = self.repository.get_all()
        for track in tracks:
            if track.id == track_id:
                track.play_count += 1
                self.repository.save_all(tracks)
                return track
            
        raise ValueError(f"Трек с ID {track_id} не найден")

    def un_like_track(self, track_id: int) -> Track:
        tracks = self.repository.get_all()
        for track in tracks:
            if track.id == track_id:
                if track.isLiked:
                    track.isLiked = False
                    self.repository.save_all(tracks)
                    print("Трек удалён из избранных")
                    return track
                    
                else: 
                    track.isLiked = True
                    self.repository.save_all(tracks)
                    print("Трек добавлен в избранные")
                    return track
            
        raise ValueError(f"Трек с ID {track_id} не найден")

    def show_liked_tracks(self) -> None:
        tracks = self.repository.get_all()

        for track in tracks:
            if track.isLiked:
                print(track.title)

    def delete_track(self, track_id: int) -> None:
        tracks = self.repository.get_all()
        remaining = [track for track in tracks if track.id != track_id]

        if len(remaining) == len(tracks):
            raise ValueError(f"Трек с ID {track_id} не найден")
        
        self.repository.save_all(remaining)
