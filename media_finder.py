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
            # Added an option were they can enter movie themselves manually
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
        self.watchlist= []

    def add_title(self, title, genre, platform):
        """
        lets user add new watch item to watchlist

        Args:
            title (str): title of media
            genre (str): genre of media 
            platform (str): platform of media
        """
        media = MediaItem(title, genre, platform)

        self.watchlist.append(media) # adds new media item to watchlist
        print(f"New media item added to watchlist: {media}")

    def generate_recommendations(self):
        """
        generates reccommended titles based on the titles in the user watchlist
        """
        # notify user when watchlist empty
        if not self.watchlist:
            print("Your watchlist is empty. Please add some titles.")
            return []

        # read netflix.csv and prime.csv
        netflix_df = pd.read_csv("Netflix.csv")
        prime_df = pd.read_csv("Prime.csv")
        
        # combine dataframes
        combined_df = pd.concat([netflix_df, prime_df], ignore_index=True)

        # find common genres
        common_genre = {}
        for item in self.watchlist:
            genre = item.genre.lower()
            common_genre[genre] = common_genre.get(genre, 0) + 1

        most_common_genre = max(common_genre, key=common_genre.get)

        genre_recs = combined_df[combined_df["Genre"].str.contains(most_common_genre, case=False)]

        # list top 5 recommendations based on watchlist
        print(f"Based on your interest in {most_common_genre}, here are some recommendations:")
        print(genre_recs[["title", "Genre"]].head(5).to_string(index=False))

    def get_similar_titles(self, genre):
        """
        returns list of titles in watchlist that match given genre
        """
        # list of media items in watchlist that match given genre
        match_genre = [item for item in self.watchlist if genre in item.genre]

        # print matches if found
        if match_genre:
            num = len(match_genre)
            print(f"Found {num} in genre '{genre}':")
            for item in match_genre:
                print(f"{item.title} ({item.platform})")

        else:
             # if no matching titles were found, tell user
            print(f"There were no titles found in genre '{genre}'")

        # return list
        return match_genre

class Filters():
    """
    A class representing filtering functions according to the user's inputted watchlist and Netflix CSV file.

    Attributes:
        watchlist (list of str): List of strings representing MediaItem objects. 
    """
    def __init__(self, media_manager, platform, watchlist):
        self.media_manager = media_manager
        self.platform = platform.strip().lower()
        self.watchlist = watchlist

        if self.platform == "netflix":
            self.movies = pd.read_csv("Netflix.csv")
        elif self.platform == "prime":
            self.movies = pd.read_csv("Prime.csv")
    
    def filter_by_genre (self, genre):
        """
        Filters media by specified genre.

        Args:
            genre (str): Genre user wants to filter by.

        Returns: 
            dataframe: A pandas dataframe representation of MediaItem instances that matches genre for user.
        """
        filtered = self.movies[self.movies["Genre"].str.contains(genre, case=False)]
        if len(filtered) >=1:
            return filtered # returns movies from CSV filtered by inputted genre
        else:
            return "We have found no media in this genre."


    def filter_by_status (self, status):
        """
        Filters media based on inputted completion status.

        Args:
            status (str): The status to filter the media accordingly. 

        Returns:
            list: A list representation of MediaItem instances that matches status for user. 
        """
        status = status.strip().lower() 
        completed_filter = [] # list for completed media items
        incompleted_filter = [] # list for incompleted media items
        
        for media in self.watchlist.values():
            if media.status.lower() == "completed":
                completed_filter.append(media) 
            else:
                incompleted_filter.append(media)

        # sorts lists by movie title
        completed_filter.sort(key=lambda x: x.title) 
        incompleted_filter.sort(key=lambda x: x.title)    

        # returning sorted lists based off user input
        if (len(completed_filter) == 0) and (len(incompleted_filter) == 0):
            return "There is no media inputted."
        elif status == "completed": 
            return completed_filter + incompleted_filter
        elif status == "not completed":
            return incompleted_filter + completed_filter       
        
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
    def show_welcome(self):
        """
        Displays a welcome message and explains available features.
        """
        print("\nWelcome to Media Finder!")
        print("You can filter recommendations, get personalized suggestions, and build your watchlist.")
        print("Let's get started!\n")

    def questions(self):
        """
        Prompts the user to input the title, genre, platform, and status of the media

        Returns:
            tuple - consisting of the title, genre, platform, and status
        """
        title = input("Enter the movie/show title: ").strip()
        genre = input("Enter the genre (or press Enter to skip): ").strip()
        platform = input("Enter the platform (Netflix or Prime): ").strip().capitalize()
        status = input("Enter status (Watched/Unwatched): ").strip().capitalize()
        return title, genre, platform, status
    
    def option(self):
        """
        Asks user what actions they want to do

        Returns:
            int - represents the function they want to do 
        """
        print("What would you like to do today?")
        pick = input("(1)Filter Recommendations, (2)Personalized Suggestions, (3)Find Movies/Tv Shows, (4)Quit: (1/2/3/4) ")
        while (pick != "1") and (pick != "2") and (pick != "3") and (pick != "4"):
            pick = input("Try Again!\nMake sure to enter 1,2,3, or 4 as your option! ")

        if pick == "4":
            quit 

        return pick

    def get_rec_genre(self): 
        """
        Prompts the user to input a genre.
        """
        genre = input("Enter genre for recommendations or press Enter to skip: ")

        if genre:
            return genre
        else:
            return None
        
    def get_status_filter(self):
        """
        Prompts the user to input status to filter by.
        """
        filter_status = input("Enter 'completed' or 'not completed' " \
        "to filter your watchlist or press Enter to skip: ")

        if filter_status:
            return filter_status
        else:
            return None

def main():
    """
    Calls different classes with required inputs.
    """
    user_input = Input()
    user_input.show_welcome()
    title, genre, platform, status = user_input.questions()
    user_input.option()
    
    rec_genre = user_input.get_rec_genre() # pulls genre input

    media_manager = MediaManager()
    watchlist = media_manager.watchlist 

    filter = Filters(media_manager, platform, watchlist)
    # if genre inputted, call filters to filter by genre
    if rec_genre:
        print(filter.filter_by_genre(rec_genre))

    MediaItem(title, rec_genre, platform) 

    filters = Filters(media_manager, platform, watchlist)

    # if user wants to add media to completed list 
    # ask user what title and platform they want
    # then call the method
    media_manager.mark_completed(title, platform)

    # if user want to find a movie or tv show
    # ask them to enter a title 
    # then call the method 
    # this method will find which platform the media is in and ask if they want to add to watchlist
    media_manager.where_to_watch(title)

    status = user_input.get_status_filter() # pulls status input
    # if status inputted, call filters to filter by status
    if status:
        print(filters.filter_by_status(status))

if __name__ == "__main__":
    main()      

     
