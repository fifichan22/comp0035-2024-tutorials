import pandas as pd
from pathlib import Path

if __name__ == '__main__':
    cols = ['country','type', 'year', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']
    raw_data_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')

    df_prepared = pd.read_csv(raw_data_csv, usecols=cols)
    '''print(df_selected_cols)'''

print(df_prepared.isnull())

'''print(df_prepared.dtypes())'''

df_prepared = df_prepared.drop(index=0).drop(index=17).drop(index=31)
df_prepared = df_prepared.reset_index(drop=True)

df_prepared['type'] = df_prepared['type'].str.strip().str.lower()

print(df_prepared)

missing_rows = df_prepared[df_prepared.isna().any(axis=1)]
print('rows:', missing_rows)


'''missing_columns = df_prepared.columns[df_prepared.isna().any(axis=0)]

print('rows:', missing_rows)
print('columns:', missing_columns)
'''
'''#missing_rows_fill = df_prepared[df_prepared.isna().any(axis=1)]
missing_columns_fill = df_prepared[df_prepared.isna().any(axis=0)]
print(missing_columns_fill)'''

print(df_prepared['type'].unique())
