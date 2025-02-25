from scraper import SRS
from file_util import create_path

def get_fixtures_results(start_year: int, num_of_seasons: int) -> None:
    if not all(isinstance(arg, int) for arg in [start_year, num_of_seasons]):
        raise ValueError(
            "Both parameters 'start_year' and 'num_of_seasons' " 
            "must be of type: int."
        )

    if num_of_seasons == 1:
        url = f"https://fbref.com/en/comps/9/{start_year}-{start_year + 1}/schedule/" / 
            f"{start_year}-{start_year + 1}-Premier-League-Scores-and-Fixtures"

    else:
        for year in range(start_year, start_year - num_of_seasons - 1, -1):

            url = (
                    f"https://fbref.com/en/comps/9/{year}-{year + 1}/schedule/"
                    f"{year}-{year + 1}-Premier-League-Scores-and-Fixtures"
            )


