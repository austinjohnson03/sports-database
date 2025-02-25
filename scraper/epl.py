from scraper import SRS
from file_util import create_path
import time
import random

def get_fixtures_results(start_year: int, num_of_seasons: int) -> None:
    if not all(isinstance(arg, int) for arg in [start_year, num_of_seasons]):
        raise ValueError(
            "Both parameters 'start_year' and 'num_of_seasons' " 
            "must be of type: int."
        )

    for year in range(start_year, start_year - num_of_seasons, -1):
        url = (
                f"https://fbref.com/en/comps/9/{year}-{year + 1}/schedule/"
                f"{year}-{year + 1}-Premier-League-Scores-and-Fixtures"
        )

        save_dir = f"../docs/soccer/epl/{year}"
        create_path(save_dir)

        filename = save_dir + f"/epl-fixtures-{year}.csv"

        s = SRS(url)
        s.scrape_schedule_no_months()
        df = s.clean_premier_league_fixtures()

        df.to_csv(filename, index=False)

        print(f"File written to '{filename}'.")

        if num_of_seasons > 1:
            time.sleep(random.uniform(12, 19))

if __name__ == "__main__":
    get_fixtures_results(1938, 1938-1888 )
