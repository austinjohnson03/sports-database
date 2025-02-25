from scraper import SRS
from file_util import create_path
from util import sleep_scraper

def get_nba_results(year: int) -> None:
    months = [
        "october", "november", "december", 
        "january", "february", "march", 
        "april", "may", "june"
    ]

    month_table = {
        2024: months[ :6],
        2021: months[2:] + ["july"],
        2020: [
        "october-2019", "november", "december", "january",
        "february", "march", "july", "august", "september", "october-2020"
        ],
        2012: months[2:],
        2006: months[1:],
        2005: months[1:],
        2000: months[1:],
        1999: months[4:],
        1997: months[1:],
        1996: months[1:],
        1995: months[1:],
        1994: months[1:],
        1993: months[1:],
        1992: months[1:],
        1991: months[1:],
        1990: months[1:],
        1989: months[1:],
        1988: months[1:],
        1983: months[:-1],
        1981: months[:-1],
        1980: months[:-1],
        1975: months[:-1],
        1974: months[:-1],
        1973: months[:-1],
        1972: months[:-1],
        1971: months[:-2],
        1970: months[:-1],
        1969: months[:-1],
        1968: months[:-1],
        1967: months[:-2],
        1966: months[:-2],
        1965: months[:-2],
        1964: months[:-2],
        1963: months[:-2],
        1962: months[:-2],
        1961: months[:-2],
        1960: months[:-2],
        1959: months[:-2],
        1958: months[:-2],
        1957: months[:-2],
        1956: months[1:-2],
        1955: months[:-2],
        1954: months[:-2],
        1953: months[:-2],
        1952: months[1:-2],
        1951: months[:-2],
        1950: months[:-2],
        # Start BAA 
        1949: months[1:-2],
        1948: months[1:-2],
        1947: months[1:-2]
    }
    
    months_in_season = []

    if year in month_table:
        months_in_season = month_table[year]

    else:
        months_in_season = months

    dir_name = f"../docs/nba/{year}"
    create_path(dir_name)

    for month in months_in_season:
        if year < 1949:
            url = f"https://www.basketball-reference.com/leagues/BAA_{year}_games-{month}.html"
        else:
            url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html"

        filename = dir_name + f"/results-{month}-{year}.csv"

        s = SRS(url)
        s.scrape_schedule()
        df = s.clean_nba_schedule()

        df.to_csv(filename, index=False)
        print(f"File saved to {filename}")
        sleep_scraper()

