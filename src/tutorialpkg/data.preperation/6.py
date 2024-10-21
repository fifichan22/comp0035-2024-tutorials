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

# Convert 'start' and 'end' columns to datetime format with dayfirst=True
df_prepared['start'] = pd.to_datetime(df_prepared['start'], errors='coerce', dayfirst=True)
df_prepared['end'] = pd.to_datetime(df_prepared['end'], errors='coerce', dayfirst=True)

# Calculate the duration in days and add it at the end
df_prepared['duration'] = (df_prepared['end'] - df_prepared['start']).dt.days

# Fill NaN values in 'duration' with 0 and convert to integer
df_prepared['duration'] = df_prepared['duration'].fillna(0).astype(int)

# Print the resulting DataFrame
print(df_prepared)

# Define the path to save the prepared CSV file in the 'data' directory
output_csv_path = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_prepared.csv')

# Save the DataFrame to a CSV file without the index column
df_prepared.to_csv(output_csv_path, index=False)

