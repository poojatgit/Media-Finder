# Media Finder
 Welcome to Media Finder - a terminal-based tool where you can add shows or movies to your watchlist, mark them as completed, and get personalized recommendations!

    How to Run:
        Open your terminal and run -  python3 media_finder.py

        You will be prompted to chose an option:
        (1) - Filtered Recommendations
        (2) - Personalied Suggestions
        (3) - Add to Watchlist/Completed
        (4) - Quit

        Start with Option 3:
            Using option 3 will build your watchlist and completed list, ensuring other features work properly

            You will be guided through some questions. Here is some example entries:

                Title: Bridgerton
                Genre: Romantic
                Platform: Netflix
                Status: (whatever you choose: watched or unwatched)

                Title: Cobra Kai
                Genre: Action 
                Platform Netflix
                Status: (whatever you choose: watched or unwatched)

            **Genres are case-sensitive, make sure they match the spelling in the CSV files exactly


        Option 1:
            Filters suggestions based on genre or completion status
                **works best after you add entries using option 3


        Option 2:
            Get recommendations based on a movie or show you've already seen
            Enter one of the movies in the csv file, make sure to enter the correct spelling for genres
        

        Option 4:
            Exits the Media Finder

        
Reminders:
    - Make sure you add things into the watchlist and completed list before asking for filter options
    - Genres as case sensitive, so make sure you spell out the name of the genre like in the csv files 
 

Data:
    - Prime.csv - Data from Kaggle: https://www.kaggle.com/datasets/dhruvjha/amazon-prime-series?resource=download
    - Netflix.csv - Data from Kaggle: https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization