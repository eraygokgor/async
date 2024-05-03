from wb_data_fetcher import WorldBankAsyncDataFetcher, WorldBankSyncDataFetcher

# Define URLs for the World Bank API
BASE_URL = "https://api.worldbank.org/v2/country"
LA_URL = BASE_URL + "/all/indicators/AG.LND.TOTL.K2?date=2021"
POP_URL = BASE_URL + "/all/indicators/SP.POP.TOTL?date=2022"
MIL_EXP_URL = BASE_URL + "/all/indicators/MS.MIL.XPND.CD?date=2021"
MIL_PER_URL = BASE_URL + "/all/indicators/MS.MIL.TOTL.P1?date=2020"

# Define URLs and column renaming for each DataFrame
urls_dataframes = [
    {
        "url": BASE_URL,
        "rename_columns": {'capitalCity': 'capital_city'}
    },
    {
        "url": LA_URL,
        "rename_columns": {'countryiso3code': 'id', 'value': 'land_area'}
    },
    {
        "url": POP_URL,
        "rename_columns": {'countryiso3code': 'id', 'value': 'population'}
    },
    {
        "url": MIL_EXP_URL,
        "rename_columns": {'countryiso3code': 'id', 'value': 'military_expenditure'}
    },
    {
        "url": MIL_PER_URL,
        "rename_columns": {'countryiso3code': 'id', 'value': 'military_personnel'}
    }
]

# Create an instance of async fetcher
print("Async fetcher is running...")
fetcher_async = WorldBankAsyncDataFetcher(urls_dataframes)
fetcher_async.fetch_all_data(n=10)

# Create an instance of sync fetcher
print("Sync fetcher is running...")
fetcher_sync = WorldBankSyncDataFetcher(urls_dataframes)
fetcher_sync.fetch_all_data(n=10)
