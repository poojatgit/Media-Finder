import unittest
from media_finder import MediaItem, MediaManager, MediaTracker, Filters

class TestMediaManager(unittest.TestCase):
    """ Purpose: These are the tests for the MediaManager class. After prompting the return should be "OK" if it runs properly. """
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
    """ Purpose: These are the tests for the MediaTracker class. The return should be "OK" if it runs properly. """
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

class TestFilters(unittest.TestCase):
    """ Purpose: These are the tests for the Filters class. After prompting the return should be "OK" if it runs properly. """
    def setUp(self):
        self.media = MediaManager()
        self.filter = Filters(self.media, "netflix", self.media.watchlist)

    def test_filter_by_genre(self):
        print("\n                  * * * * * * *              ")
        print("\n                  FILTERS TEST")
        print("\nFilter by Genre: ")
        filtered = self.filter.filter_by_genre("Action")
        self.assertTrue(len(filtered) > 0)

    def test_filter_by_status(self):
        print("\nFilter by Status: ")
        self.media.mark_completed("Bridgerton", "Netflix")
        completed = self.filter.filter_by_status("completed")
        self.assertEqual(completed[0].title, "Bridgerton")

if __name__ == "__main__":
    unittest.main()
        


    


    