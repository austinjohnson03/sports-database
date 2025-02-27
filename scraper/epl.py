from scraper import SRS
from file_util import create_path
from util import sleep_scraper

def get_fixtures(year: int) -> None:
    epl_range = range(1888, 2025)
    epl_exclusion_range = range(1940, 1946)

    if year not in epl_range or year in epl_exclusion_range:
        raise ValueError(
            f"Invalid parameter: {year}"
            f"Year must be in the range 1888-2024. (1940-1945 Excluded)"
        )

    url = (
        f"https://fbref.com/en/comps/9/{year}-{year + 1}/schedule/"
        f"{year}-{year + 1}-Premier-League-Scores-and-Fixtures"
    )

    save_dir = f"../docs/soccer/epl/{year}"
    create_path(save_dir)

    filename = save_dir + f"/epl-fixtures-{year}.csv"

    s = SRS(url)
    s.scrape_schedule()
    df = s.clean_premier_league_fixtures()

    df.to_csv(filename, index=False)
    print(f"{year} EPL Results/Fixtures written to '{filename}'")

