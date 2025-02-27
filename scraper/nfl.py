
from scraper import SRS
from file_util import create_path

def get_results(year: int) -> None:
    nfl_range = range(1920, 2025)
    if year not in nfl_range:
        raise ValueError(
            f"Invalid paramter '{year}'. Years must be in the range 1920-2024"
        )
    
    if year > 1922:
        url = f"https://www.pro-football-reference.com/years/{year}/games.htm"
    else:
        url = f"https://www.pro-football-reference.com/years/{year}_APFA/games.htm"

    dir_name = f"../docs/nfl/{year}"
    create_path(dir_name)
    filename = dir_name + f"/results-{year}.csv"

    s = SRS(url)
    s.scrape_schedule()
    df = s.clean_nfl_schedule()

    df.to_csv(filename, index=False)
    print(f"{year} NFL Results/Schedule written to '{filename}'")
