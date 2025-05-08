import pandas as pd

class MediaItem:
    """
    Represents a media item (a movie or tv show)

    Attributes:
        title (str): The title of the media.
        genre (str): The genre of the media.
        platform (str): The streaming service where the media is available.
    """

    def __init__(self, title, genre, platform):
        self.title = title

        if genre:
            self.genre = genre
        else:
            self.genre = "Unknown"

        self.platform = platform

    def __repr__(self):
        return f"{self.title} on {self.platform}\nGenre:{self.genre}"
        
class MediaManager:
    """ 
    Manages the watchlist and completed items using MediaItem objects

    Attributes:
    watchlist (dict): users watchlist filled with MediaItem objects
    completed (dict): users completed movies/shows filled with MediaItem objects
    
    """
    def __init__(self):
        self.watchlist = {}
        self.completed = {}

    def mark_completed(self, title, platform):
        """
        adds completed media into a dictionary to keep track

        Args:
        title (str): title of the movie/show
        platform (str): platform of the movie/show
        """
        title = title.strip().lower()
        platform = platform.strip().lower()

        df = None
        if platform == "netflix":
            df = pd.read_csv("Netflix.csv")

        elif platform == "prime":
            df = pd.read_csv("Prime.csv")

        else:
            print("Platform not available. Use 'Netflix' or 'Prime'")
            return
        
        match = df[df['title'].lower() == title]
        counter = 1
        if not match.empty:
            specific_row = match.iloc[0]
            media = MediaItem(specific_row['title'], specific_row['Genre'], platform)
            self.completed[counter] = media 
            counter += 1
            print(f"{specific_row['title']} marked as completed!")

        else:
            print(f"{title} not found in {platform}")
            #Added an option were they can enter movie themselves manually
            manual = input("Do you want to add it manually? (yes/no): ").strip().lower()
            if manual == "yes":
                genre = input("Enter genre: ").strip()
                media = MediaItem(title, platform, genre)
                self.completed[counter] = media
                print(f"{title} manually marked completed!")
            
            else:
                print("Manual entry skipped")


    def where_to_watch(self, title):
        """
        finds the platform where the media located, then adds to watchlist

        Args:
        title (str): title of the movie/show
        """
        title = title.strip().lower()
        source = ""
        media = None
    
        df_n = pd.read_csv("Netflix.csv")
        match = df_n[df_n['title'].lower() == title]
        if not match.empty:
            specific_row = match.iloc[0]
            source = "Netflix"
            media = MediaItem(specific_row['title'], specific_row['Genre'], source)
        
        else:
            df_p = pd.read_csv("Prime.csv")
            match = df_p[df_p['title'].lower() == title]
            if not match.empty:
                specific_row = match.iloc[0]
                source = "Prime"
                media = MediaItem(specific_row['title'], specific_row['Genre'], source)


        if media:
            print(f"Found: {media}")
            should_add = input("Do you want to add this to your watchlist? (yes/no): ").strip().lower()
            
            if should_add == "yes":
                self.watchlist[title] = media
                print(f"{title} added to watchlist!")           

        else:
                print(f"{title} is not found.")       



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
    def __init__(self):
        self.watchlist = []
    
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
        

class Input:
    """
    A class to handle user input for media tracking and filtering.

    Attributes:
        title (str): The title of the media.
        genre (str): The genre of the media.
        platform (str): The streaming platform where the media is available.
        status (str): The completion status of the media ('completed' or 'not completed').
        year_range (tuple): A tuple containing the start and end years for filtering.
    """

    def __init__(self):
        """
        Initializes the Input object with default values.
        """
        pass

    def get_title(self):
        """
        Prompts the user to input the title of the media.
        """
        pass

    def get_genre(self):
        """
        Prompts the user to input the genre of the media.
        """
        pass

    def get_platform(self):
        """
        Prompts the user to input the streaming platform of the media.
        """
        pass

    def get_status(self):
        """
        Prompts the user to input the completion status of the media.
        """
        pass

    def get_year_range(self):
        """
        Prompts the user to input the start and end years for filtering.
        """
        pass


      
