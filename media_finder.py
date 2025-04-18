

class MediaItem:
    """
    A class representing a media item such as a movie or TV show and updating the status of them.

    Attributes:
        title (str): The title of the media.
        genre (str): The genre of the media.
        status (str): The completion status, either 'not completed' or 'completed'.
        platform (str): The streaming service where the media is available.
    """

    def __init__(self, title, genre, platform):
        pass

    def mark_completed(self):
        """
        Marks the media item as completed or not completed
        """
        pass

    def where_to_watch(self):
        """
        finds the platform where the media is and returns where it can be watched
        """
        pass

    def __repr__(self):
        """
        show the user a readable verision of the attributes 
        """
        pass
    
    def test_media(self):
        """
        this will test the class and make sure that it is running smoothly 
        """
        pass

class MediaTracker:
    """
    A class representing tracking of a user's watchlist by giving reccommendations and filtering

    Attributes:
        watchlist (list): The list of MediaItem objects added by the user. 
    """

    def __init__(self):
        pass

    def add_title(self, title, genre, platform):
        """
        lets user add new watch item to watchlist
        """
        pass

    def generate_recommendations(self):
        """
        generates reccommended titles based on the titles in the user watchlist
        """
        pass

    def get_similar_titles(self, genre):
        """
        returns list of titles in watchlist that match given genre
        """
        pass

class Filters():
    """
    A class representing filtering functions according to the user's inputted watchlist.

    Attributes:
        watchlist (list of str): List of strings representing MediaItem objects. 
    """

    def filter_by_genre (self, genre):
        """
        Filters media by specified genre.

        Args:
            genre (str): Genre user wants to filter by.

        Returns: 
            list: A list representation of MediaItem instances that matches genre for user.
        """
        pass

    def filter_by_status (self, ):
        """
        Filters media based on inputted completion status.

        Args:
            status (str): The status to filter the media accordingly. 

        Returns:
            list: A list representation of MediaItem instances that matches status for user. 
        """
        pass