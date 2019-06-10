import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Set up code checking
print("Setup Complete")



def RunExercise():
    print("Reading Spotify CSV data")
    # Path of the file to read
    spotify_filepath = "../../../../Data/Kaggle/DataSets/spotify.csv"
    # Read the file into a variable spotify_data
    spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)


    # Examine Data
    # Print the first 5 rows of the data
    print(spotify_data.head())


    # Print the last five rows of the data
    print(spotify_data.tail())


    # Chart 1
    # Line chart showing daily global streams of each song 
    # Set the width and height of the figure
    print("Plot 1")
    plt.figure(figsize=(16,6))
    sns.lineplot(data=spotify_data)
    plt.show()



    # Chart 2
    # Set the width and height of the figure
    print("Plot 2")
    plt.figure(figsize=(14,6))
    # Add title
    plt.title("Daily Global Streams of Popular Songs in 2017-2018")

    # Line chart showing daily global streams of each song 
    sns.lineplot(data=spotify_data)
    plt.show()



    # List
    print(list(spotify_data.columns))


    # Chart 3
    # Set the width and height of the figure
    print("Plot 3")
    plt.figure(figsize=(14,6))
    # Add title
    plt.title("Daily Global Streams of Popular Songs in 2017-2018")
    # Line chart showing daily global streams of 'Shape of You'
    sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")
    # Line chart showing daily global streams of 'Despacito'
    sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
    # Add label for horizontal axis
    plt.xlabel("Date")
    plt.show()

