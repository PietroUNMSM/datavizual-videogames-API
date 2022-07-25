# main.py
# =============================================================================
# common
import os
import json
# requirements
from dotenv import load_dotenv
from fastapi import FastAPI
import pandas as pd

# -----------------------------------------------------------------------------

load_dotenv('./.env')

app = FastAPI()


# => routers
@app.get('/')
async def mainIndex() -> ...:
    return main_index()


@app.get('/console_serie/{console_serie}/years/{year}')
async def console_serieInfo(console_serie: str, year: int) -> ...:
    return console_serieInfo(console_serie, year)


# => functions
def main_index() -> dict:
    return {'message': 'use esta api para tu visualizacion'}


def console_serieInfo(console_serie: str, year: int) -> dict:
    host_data = os.environ['HOST_DATA']

    data_mapper = {
        'general': f'{host_data}/general.csv',
        'microsoft': f'{host_data}/microsoft.csv',
        'nintendo': f'{host_data}/nintendo.csv',
        'playstation': f'{host_data}/playstation.csv',
        'sega': f'{host_data}/sega.csv'
    }
    console_data = data_mapper[console_serie]

    df = pd.read_csv(console_data, sep=',', encoding='utf-8')
    subdf = df[df['Year_of_Release'] == int(year)]
    return json.loads(subdf.to_json(orient='records', date_format='iso'))