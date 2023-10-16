# Selenium Scraper Demo -- ME369P
# simple tutorial reference: https://www.youtube.com/watch?v=UOsRrxMKJYk
# wikipedia scraping reference: https://www.youtube.com/watch?v=jdj6IC7Pi0I


# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import re
import matplotlib.pyplot as plt

def scrape():
    # create variables
    website_url = 'https://en.wikipedia.org/wiki/List_of_National_Basketball_Association_career_scoring_leaders'
    player_name = []
    total_points = []
    games_played = []
    points_per_game = []

    # create driver
    browser_options = Options()
    browser_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options =browser_options)
    driver.get(website_url)

    # maximize the chrome window
    driver.maximize_window()

    # create locators
    # xpath is the XML path on the wikipedia page where the element information is stored
    player_locator = driver.find_elements(By.XPATH, "//table[@class=\"wikitable sortable jquery-tablesorter\"]/tbody/tr/td[2]")
    total_points_locator = driver.find_elements(By.XPATH, "//table[@class=\"wikitable sortable jquery-tablesorter\"]/tbody/tr/td[5]")
    games_played_locator = driver.find_elements(By.XPATH, "//table[@class=\"wikitable sortable jquery-tablesorter\"]/tbody/tr/td[6]")
    ppg_locator = driver.find_elements(By.XPATH, "//table[@class=\"wikitable sortable jquery-tablesorter\"]/tbody/tr/td[7]")

    # convert data into a list
    for i in range(len(player_locator)):
        # use re to remove non-alphabetic symbols (ex: * and ^) from the data
        player_name.append(re.sub(r'[^a-zA-Z ]+', '', player_locator[i].text))
        # append the rest of the data
        total_points.append(total_points_locator[i].text)
        games_played.append(games_played_locator[i].text)
        points_per_game.append(ppg_locator[i].text)


    # create pandas dataframe
    df = pd.DataFrame()

    # insert lists as df columns
    df['Name'] = player_name
    df['Total Points'] = total_points
    df['Games Played'] = games_played
    df['Points Per Game'] = points_per_game

    # save df to csv
    df.to_csv('nba_scoring_leaders.csv', index=False)

    # plot data results
    display_data(df)

def display_data(df):
    # plot the top 10 scoring leaders by points
    plt.figure(1)
    plt.plot(df.Name)


if __name__ == "__main__":
    scrape()
