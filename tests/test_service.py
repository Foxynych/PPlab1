import unittest

from application.music_service import MusicService
from domain.repository import TrackRepository
from domain.track import Track


class InMemoryRepository(TrackRepository):
    def __init__(self):
        self.tracks = []

    def get_all(self) -> list[Track]:
        return [
            Track(t.id, t.title, t.artist, t.duration, t.isLiked)
            for t in self.tracks
        ]

    def save_all(self, tracks: list[Track]) -> None:
        self.tracks = [
            Track(t.id, t.title, t.artist, t.duration, t.isLiked)
            for t in tracks
        ]


class MusicServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = MusicService(InMemoryRepository())

    def test_add_and_play(self):
        track = self.service.add_track("Bohemian Rhapsody", "Queen", 354)
        self.assertEqual(track.id, 1)

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            self.service.add_track("  ", "Queen", 200)

    def test_empty_artist_is_rejected(self):
        with self.assertRaises(ValueError):
            self.service.add_track("Song", "  ", 200)

    def test_non_positive_duration_is_rejected(self):
        with self.assertRaises(ValueError):
            self.service.add_track("Song", "Artist", 0)

    def test_delete(self):
        track = self.service.add_track("Удалить меня", "Artist", 100)
        self.service.delete_track(track.id)
        self.assertEqual(self.service.list_tracks(), [])

    def test_delete_missing_track(self):
        with self.assertRaises(ValueError):
            self.service.delete_track(42)


if __name__ == "__main__":
    unittest.main()
