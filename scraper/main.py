from util import sleep_scraper
import nba
import nfl 
import cfb 
import epl

if __name__ == "__main__":
    for year in range(2024, 1999, -1):
        nba.get_results(year)
        sleep_scraper()
        nfl.get_results(year)
        sleep_scraper()
        epl.get_fixtures(year)
        sleep_scraper()
        cfb.get_results(year)
        sleep_scraper()





