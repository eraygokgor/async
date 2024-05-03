import asyncio

import pandas as pd
import requests
from aiohttp import ClientSession

from utils import function_timer


class WorldBankAsyncDataFetcher:
    def __init__(self, urls_dataframes: list[dict]) -> None:
        self.urls_dataframes = urls_dataframes
        self.data_frames = []

    @staticmethod
    async def fetch_data(session: ClientSession, url: str) -> list[dict]:
        data = []
        page = 1
        is_not_finished = True

        while is_not_finished:
            params = {
                "format": "json",
                "page": page
            }
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    result = await response.json()
                    data += result[1]
                    is_not_finished = result[0]['pages'] > result[0]['page']
                    page += 1
                else:
                    raise Exception(f"Request error: {response.status}")

        return data

    async def fetch_all(self) -> None:
        async with ClientSession() as session:
            tasks = [self.fetch_data(session, data['url']) for data in self.urls_dataframes]
            results = await asyncio.gather(*tasks)
            self.data_frames = [pd.DataFrame(result) for result in results]

    def process_data_frames(self) -> None:
        for idx, data in enumerate(self.urls_dataframes):
            df = self.data_frames[idx]
            # Rename columns as specified in the data dictionary
            df.rename(columns=data['rename_columns'], inplace=True)

    @function_timer
    def fetch_all_data(self) -> list:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.fetch_all())
        self.process_data_frames()
        return self.data_frames

########################################################################################################################


class WorldBankDataFetcher:
    def __init__(self, urls_dataframes: list) -> None:
        self.urls_dataframes = urls_dataframes
        self.data_frames = []

    @staticmethod
    def fetch_data(url: str, rename_columns: dict) -> pd.DataFrame:
        data = []
        page = 1
        is_not_finished = True

        while is_not_finished:
            params = {
                "format": "json",
                "page": page
            }
            res = requests.get(url, params=params)

            if res.status_code == 200:
                result = res.json()
                is_not_finished = result[0]['pages'] > result[0]['page']
                data += result[1]
                page += 1
            else:
                raise Exception(f"Request error: {res.status_code}")

        df = pd.DataFrame(data)
        df.rename(columns=rename_columns, inplace=True)
        return df

    @function_timer
    def fetch_all_data(self) -> list:
        for data in self.urls_dataframes:
            df = self.fetch_data(data['url'], data['rename_columns'])
            self.data_frames.append(df)
        return self.data_frames
