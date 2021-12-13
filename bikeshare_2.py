import time
import pandas as pd
import numpy as np



city_data_dictionary = {
    "chicago": r"E:\DATA ANALYSIS\Udacity\fwd-egypt\Data Analysis Professional Track\bike share project\chicago.csv",
    "new york city": r"E:\DATA ANALYSIS\Udacity\fwd-egypt\Data Analysis Professional Track\bike share project\new_york_city.csv",
    "washington": r"E:\DATA ANALYSIS\Udacity\fwd-egypt\Data Analysis Professional Track\bike share project\washington.csv"
}

pd.set_option("display.max_columns", None)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Welcome to egFWD - Data Professional Track - December 2021 Cohort')
    print('First Project:   Explore US Bikeshare')
    print('By AHMED ELSAWY, on 13-12-2021')
    print("#"*50)
    print('\nLet\'s explore some US bikeshare data concerning three cities: chicago, new york city and washington.\n')


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities_list = ['chicago', 'new york city', 'washington']
        city_input = input("Please, select a city:\n'chicago', 'new york city' or 'washington'\n=> ").lower()
        if city_input not in cities_list:
            print("Whoops! Invalid city!")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        months_list = ['January', 'February', 'March', 'April', 'May', 'June']
        month_input = input("Please, select a month or type 'all' to skip months filter:\n"
                            " 'january', 'february', 'march', 'april', 'may', 'june'\n=> ").capitalize()
        if month_input not in months_list and month_input != "All":
            print("Whoops! Invalid month!")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_input = input("Please, select a day or type 'all' to skip days filter:\n"
                          " 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'\n=> ").capitalize()
        if day_input not in days_list and day_input != "All":
            print("Whoops! Invalid day!")
        else:
            break

    print('-'*40)
    return city_input, month_input, day_input


def load_data(city_input, month_input, day_input):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city_input - name of the city to analyze
        (str) month_input - name of the month to filter by, or "all" to apply no month filter
        (str) day_input - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(city_data_dictionary[city_input])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month_input != "All":
        # filter by month to create the new dataframe
        df = df[df['month'] == month_input]

    # filter by day of week if applicable
    if day_input != "All":
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_input]  # capitalize first letter of input to match results obtained from line 77

    return df


def display_five_lines_of_raw_data(df):
    """
    According to the project rubric:
    Raw data is displayed upon request by the user in the following manner:
    -script should prompt the user if they want to see 5 lines of raw data,
    -Display that data if the answer is 'yes',
    -Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
    -Stop the program when the user says 'no' or there is no more raw data to display.
    -Tips: you can implement the while loop and track the row index in order to display the continuous raw data.
    """
    print("Great! raw data is ready according to your previous preferences.")
    print("If you wish to display 5 lines of the raw data, please let me know.")
    num_of_lines = 0
    while True:
        user_feedback = input("Display next 5 lines of raw data? type yes or no => ").lower()
        if user_feedback == "no":
            break
            #Stop the loop when the user says 'no'.

        if user_feedback != "no" and user_feedback != "yes":
            print("Whoops! Invalid Choice!")
            continue

        if user_feedback == "yes":
            print(df[num_of_lines:num_of_lines + 5])
            num_of_lines += 5

        if num_of_lines >= len(df.index): #or num_of_lines >= df.shape[0]:# Both are synonymous
            print("All lines already displayed.\nNo More Lines To Display.")
            break
            #Stop the loop when there is no more raw data to display.


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: ", df['month'].value_counts().idxmax())


    # display the most common day of week
    print("The most common day of week is: ", df['day_of_week'].value_counts().idxmax())



    # display the most common start hour
    print("The most common start hour is: ", df['Start Time'].dt.hour.value_counts().idxmax())


    print(f"\nThis calculation took {time.time() - start_time} seconds.")
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].value_counts().idxmax())


    # display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].value_counts().idxmax())


    # display most frequent combination of start station and end station trip
    df["Combination of Start and End Stations"] = df['Start Station'] + " => " + df['End Station']
    print(
        "The most frequent trip ( Start => End ) is : (",
        df["Combination of Start and End Stations"].value_counts().idxmax(), ")"
    )


    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time = ttt
    ttt_sec = df["Trip Duration"].sum()
    ttt_min = ttt_sec / 60
    ttt_hrs = ttt_min / 60
    ttt_days = ttt_hrs / 24
    print(f"Total Travel Time = {ttt_sec} seconds, "
          f"or about {ttt_min} minutes, or about {ttt_hrs} hours, or about {ttt_days} days.")



    # display mean travel time = mtt
    mtt_sec = df["Trip Duration"].mean()
    mtt_min = mtt_sec / 60
    mtt_hrs = mtt_min / 60
    mtt_days = mtt_hrs / 24
    print(f"Mean Travel Time = {mtt_sec} seconds, "
          f"or about {mtt_min} minutes, or about {mtt_hrs} hours, or about {mtt_days} days.")


    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types: ")
    print(df["User Type"].value_counts())
    print("-"*20)

    # Display counts of gender
    if "Gender" in df:
        print("Counts of gender: ")
        print(df["Gender"].value_counts())
        print("-" * 20)

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("Earliest year of birth: ", df["Birth Year"].min())
        print("Most recent year of birth: ", df["Birth Year"].max())
        print("Most common year of birth: ", df["Birth Year"].mode()[0])
        print("-" * 20)

    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-'*40)


def main():
    while True:
        city_input, month_input, day_input = get_filters()
        df = load_data(city_input, month_input, day_input)

        display_five_lines_of_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? type yes or no.\n=> ')
        if restart.lower() != 'yes':
            print("Thank You! See You In Next Projects *_*")
            break


if __name__ == "__main__":
    main()
