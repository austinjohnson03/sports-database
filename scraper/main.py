from util import sleep_scraper
import nba

if __name__ == "__main__":
    for year in range(2021, 1999, -1):
        nba.get_nba_results(year)
        sleep_scraper()



