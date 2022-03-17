import time
import pandas as pd
import numpy as np
from datetime import datetime as dt

CITY_DATA = { 'chicago': r'E:\00-FWD\Project 1 - Bikeshare\Project 1\chicago.csv', 
              'new york city': r'E:\00-FWD\Project 1 - Bikeshare\Project 1\new_york_city.csv',
              'washington': r'E:\00-FWD\Project 1 - Bikeshare\Project 1\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("please enter the city name: chicago, new york city or washington\n".lower())
    while True:
        if city not in ("chicago", "new york city", "washington"):
            print("please enter a valid city name.")
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("please enter Month: all, january, february, ... , june\n".lower())
    while True:
        if month not in ("january","february","march","april","may","june","all"):
            print("please enter a valid month.")
          
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("please enter required day: all, monday, tuesday, ... sunday\n".lower())
    while True:
        if day not in ("monday","tuesday","wednsday","thursday","friday","Saturday","sunday","all"):
            print("please enter a valid day.")
         else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start hour'] = df['Start Time'].dt.hour
    if month !='all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] ==  month]
        
        
    if day !='all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is :{}'.format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print('the most common day is :{}'.format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print('the most common hour is :{}'.format(df['start hour'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station is :{}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('the most commonly used end station is :{}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['route']=df['Start Station']+","+df['End Station']
    print('the most commonly used route is :{}'.format(df['route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is : ',(df['Trip Duration'].sum()).round())

    # TO DO: display mean travel time
    print('average travel time is : ',(df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())


    # TO DO: Display counts of gender
    if city != "washington":
        print(df['Gender'].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('the earliest year of Brith is : ',int(df['Birth year'].min()))
        print('the most recent year of Birth is : ',int(df['Birth year'].mode()[0]))  
        print('the most common year of Brith is : ',int(df['Birth year'].max()))
        
    else:
      
        print('no data avalible for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    
    main()
