from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from typing import List
import re
import numpy as np

#TODO: Normalize names across each database

class Scraper:
    def __init__(self, url: str):
        self._url = url
        self._matrix = None

    @property 
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        self._url = value
    
    def get_html(self) -> str: 
        try:
            r = requests.get(self._url, timeout=10)
            r.raise_for_status()
            return r.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {self._url}: {e}")
            return ""

    def get_soup(self) -> BeautifulSoup:
        html = self.get_html()
        if html:
            return BeautifulSoup(html, "html.parser")
        return None

class SRS(Scraper):
    def __init__(self, url):
        super().__init__(url)

    def scrape_schedule_no_months(self) -> None: 
        soup = self.get_soup()
        tbody = soup.find("tbody")
        tr = tbody.find_all("tr")
        result = []
        for row in tr:
            header = row.find("th")
            cells = row.find_all("td")
            new_row = []
            new_row.append(header.get_text(strip=True))
            for cell in cells:
                new_row.append(cell.get_text(strip=True))
            
            if not new_row:
                continue
            result.append(new_row)

        self._matrix = result



    def clean_cfb_schedule(self) -> pd.DataFrame:
        if len(matrix[0]) == 9:
            columns = [
                "Week", "Date", "Day", "Away", "Away Pts", "N", "Home", "Home Pts", "Notes"
            ]

        else:
            columns = [
                "Week", "Date", "Time", "Day", "Away", "Away Pts", "N", "Home", "Home Pts", "Notes"
            ]

        df = pd.DataFrame(matrix, columns=columns)

        # Change columns from Winner/Loser to Away/Home with the correct team.
        df.loc[df['N'] == "", ["Home", "Away"]] = df.loc[df['N'] == "", ["Away", "Home"]].values
        df.loc[df['N'] == "", ["Home Pts", "Away Pts"]] = df.loc[df['N'] == "", ["Away Pts", "Home Pts"]].values
        df['N'] = df['N'].replace('@', '')

        # Remove ranking strs 
        df['Home'] = df['Home'].apply(self.remove_ranking)
        df['Away'] = df['Away'].apply(self.remove_ranking)

        return df

    def remove_ranking(self, value: str) -> str:
        return re.sub(r"\(\d+\)", "", value).strip()

    def clean_nfl_schedule(self) -> pd.DataFrame:
        if len(self._matrix[0]) == 13:
            columns = [
                "Day", "Date", "Time", "Away", "N", "Home",
                "Boxscore", "Away Pts", "Home Pts", "Home Yds", "Home TOs", 
                "Away Yds", "Away TOs"
            ]
        
        df = pd.DataFrame(self._matrix, columns=columns)

        df.loc[df['N'] == '', ["Home", "Away"]] = df.loc[df['N'] == "", ["Away", "Home"]].values
        df.loc[df['N'] == '', ["Home Pts", "Away Pts"]] = df.loc[df['N'] == "", ["Away Pts", "Home Pts"]].values
        df.loc[df['N'] == '', ["Home Yds", "Away Yds"]] = df.loc[df['N'] == "", ["Away Yds", "Home Yds"]].values
        df.loc[df['N'] == '', ["Home TOs", "Away TOs"]] = df.loc[df['N'] == "", ["Away TOs", "Home TOs"]].values
        df['N'] = df['N'].replace('@', '')

        df = df[df['Away'].notna()]  # Remove rows without date

        df = df.drop(columns=["Boxscore"])
        
        return df

    def clean_premier_league_fixtures(self) -> pd.DataFrame:
        if len(self._matrix[0]) == 14:
            columns = [
                "week", "day", "date", "time", "home", "home xG", 
                "score", "away xG", "away", "attendance", "venue",
                "referee", "match report", "notes"
            ]
        elif len(self._matrix[0]) == 12:
            columns = [
                "week", "day", "date", "time", "home",
                "score", "away", "attendance", "venue",
                "referee", "match report", "notes"
            ]


        df = pd.DataFrame(self._matrix, columns=columns)

        df = df[df["week"].notna() & (df["week"] != "")]

        df = df.dropna(subset=["week"])

        df['score'] = df['score'].astype(str).replace([np.nan, ''], '-')

        df['score'] = df['score'].str.replace('–', '-', regex=False)

        df[["home score", "away score"]] = df["score"].str.split('-', n=1, expand=True)
        
        
        if len(self._matrix[0]) == 14:
            df = df.drop(["home xG", "away xG", "match report", "score"], axis=1)
        elif len(self._matrix[0]) == 12:
            df = df.drop(["match report", "score"], axis=1)

        return df



if __name__ == "__main__":
    s = SRS("https://fbref.com/en/comps/9/2023-2024/schedule/2023-2024-Premier-League-Scores-and-Fixtures")
    s.scrape_schedule_no_months()
    df = s.clean_premier_league_fixtures()
    print(df.columns)
