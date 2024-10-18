import pandas as pd
from pathlib import Path

if __name__ == '__main__':
    cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']
    raw_data_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')

    df_prepared = pd.read_csv(raw_data_csv, usecols=cols)
    '''print(df_selected_cols)'''


'''print(df_prepared.dtypes())'''

missing_rows = df_prepared[df_prepared.isna().any(axis=1)]
missing_columns = df_prepared.columns[df_prepared.isna().any(axis=0)]
print('rows:', missing_rows)
print('columns:', missing_columns)
