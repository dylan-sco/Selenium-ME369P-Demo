# ME369P Selenium Demonstration

## Setup Instructions
1. Download the latest chromedriver for your operating system [here](https://chromedriver.chromium.org/downloads)
2. Clone this repository with `git clone https://github.com/dylan-sco/Selenium-ME369P-Demo`
3. Install the required python packages: selenium, pandas, matplotlib
4. Run the `scrape.py` file

## How does it work?
The python script opens a [wikipedia page](https://en.wikipedia.org/wiki/List_of_National_Basketball_Association_career_scoring_leaders) for the NBA's career scoring leaders. 
Next, selenium navigates to the scoring leaders table and scrapes the following attributes: Player Name, Total points, Games played, and Points per game.

The data is saved into a pandas dataframe and displayed in plots via matplotlib.
