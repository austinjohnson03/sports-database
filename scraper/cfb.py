from scraper import SRS
from file_util import create_path
from util import sleep_scraper

def get_cfb_results(year: int) -> None:
    cfb_range = range(1869, 2025)

    if year not in cfb_range or year == 1871:
        raise ValueError(
            f"Invalid parameter: {year}\n"
            f"Year must be in the range 1869, 1870, 1872-2024."
        )

    url = f"https://www.sports-reference.com/cfb/years/{year}-schedule.html"

    dir_name = f"../docs/cfb/{year}"
    create_path(dir_name)
    filename = dir_name + f"/results-{year}.csv"

    s = SRS(url)
    s.scrape_schedule()
    df = s.clean_cfb_schedule()

    df.to_csv(filename, index=False)
    print(f"File saved to {filename}")

