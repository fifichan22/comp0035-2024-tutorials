import pandas as pd
from pathlib import Path

if __name__ == '__main__':
    cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']
    raw_data_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df_selected_cols = pd.read_csv(raw_data_csv, usecols=cols)
    print(df_selected_cols)

    df_result = df_selected_cols.drop(columns=['MyCol2', 'MyCol4'], axis=1)