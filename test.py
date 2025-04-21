import unittest
from media_finder import MediaItem, MediaTracker, Filters, Input

class TestMediaItem(unittest.TestCase):
    def test_mark_completed(self):
        media = MediaItem("Barbie", "Comedy/Fantasy", "Netflix")
        self.assertIsNone(media.mark_completed())

    def test_where_to_watch(self):
        media = MediaItem("Barbie", "Comedy/Fantasy", "Netflix")
        self.assertIsNone(media.where_to_watch())

class TestMediaTracker(unittest.TestCase):
    def test_add_title(self):
        tracker = MediaTracker("Barbie", "Comedy/Fantasy", "Netflix")
        self.assertIsNone(tracker.add_title("Barbie", "Comedy/Fantasy", "Netflix"))

    def test_generate_recommendations(self):
        media = MediaItem("Barbie", "Comedy/Fantasy", "Netflix")        
        self.assertIsNone(media.generate_recommendations())

    def test_get_similar_titles(self):
        tracker = MediaTracker("Barbie", "Comedy/Fantasy", "Netflix")
        self.assertIsNone(tracker.get_similar_titles("Comedy/Fantasy"))

class TestFilters(unittest.TestCase):
    def test_filter_by_genre(self):
        media = MediaItem("Barbie", "Comedy/Fantasy", "Netflix")        
        self.assertIsNone(media.filter_by_genre("Comedy/Fantasy"))

    def test_filter_by_status(self):
        media = MediaItem("Barbie", "Comedy/Fantasy", "Netflix")        
        self.assertIsNone(media.filter_by_status())

class TestInput(unittest.TestCase):
    def test_get_title(self):
        input = Input()
        self.assertIsNone(input.get_title())


    def test_get_genre(self):
        input = Input()
        self.assertIsNone(input.get_genre())

    def test_get_platform(self):
        input = Input()
        self.assertIsNone(input.get_platform())

    def test_get_status(self):
        input = Input()
        self.assertIsNone(input.get_status())

    def test_get_year_range(self):
        input = Input()
        self.assertIsNone(input.get_year_range())

if __name__ == "__main__":
    unittest.main()
        


    


    