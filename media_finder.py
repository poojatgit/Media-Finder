

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
    
    def test_media(self):
        """
        this will test the class and make sure that it is running smoothly 
        """