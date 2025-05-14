import unittest
import pandas as pd
from media_finder import MediaItem, MediaManager, MediaTracker, Filters, Input

class TestMediaManager(unittest.TestCase):
    def setUp(self):
        self.media = MediaManager()

    def test_mark_completed_found(self):
        print("\n               MEDIA MANAGER TEST")
        print("\nFound in mark_completed:")
        self.assertIsNone(self.media.mark_completed("Bridgerton", "Netflix"))

    def test_mark_completed_notfound(self):
        print("\nNot Found in mark_completed: ")
        self.assertIsNone(self.media.mark_completed("Barbie", "Netflix"))

    def test_where_to_watch_found(self):
        print("\nFound in where_to_watch: ")
        self.assertIsNone(self.media.where_to_watch("Bridgerton"))

    def test_where_to_watch_notfound(self):
        print("\nNot Found in where_to_watch: ")
        self.assertIsNone(self.media.where_to_watch("Barbie"))

class TestMediaTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = MediaTracker()

    def test_add_title(self):
        print("\n                  * * * * * * *              ")
        print("\n               MEDIA TRACKER TEST")
        print("\nAdd Title: ")
        self.tracker.add_title("Barbie", "Fantasy", "Netflix")
        self.assertEqual(len(self.tracker.watchlist), 1)
        self.assertEqual(self.tracker.watchlist[0].title, "Barbie")

    def test_generate_recommendations(self):
        print("\nGenerate Recommendations: ")
        self.tracker.watchlist = [MediaItem("Barbie", "Fantasy", "Netflix")]
        self.assertIsNone(self.tracker.generate_recommendations())

    def test_get_similar_titles(self):
        print("\nSimilar Titles: ")
        self.tracker.watchlist = [MediaItem("Barbie", "Fantasy", "Netflix"), MediaItem("The Boys", "Action", "Prime")]
        similar = self.tracker.get_similar_titles("Fantasy")
        self.assertEqual(len(similar), 1)
        self.assertEqual(similar[0].title, "Barbie")

# class TestFilters(unittest.TestCase):
#     def test_filter_by_genre(self):
#         media = MediaManager("Barbie", "Comedy/Fantasy", "Netflix")
#         filter = Filters(media, "netflix", media.watchlist)        
#         self.assertIsNone(media.filter_by_genre("Comedy/Fantasy"))

#     def test_filter_by_status(self):
#         media = MediaItem("Barbie", "Comedy/Fantasy", "Netflix")        
#         self.assertIsNone(media.filter_by_status())

# class TestInput(unittest.TestCase):
#     def test_get_title(self):
#         input = Input()
#         self.assertIsNone(input.get_title())


#     def test_get_genre(self):
#         input = Input()
#         self.assertIsNone(input.get_genre())

#     def test_get_platform(self):
#         input = Input()
#         self.assertIsNone(input.get_platform())

#     def test_get_status(self):
#         input = Input()
#         self.assertIsNone(input.get_status())

#     def test_get_year_range(self):
#         input = Input()
#         self.assertIsNone(input.get_year_range())

if __name__ == "__main__":
    unittest.main()
        


    


    