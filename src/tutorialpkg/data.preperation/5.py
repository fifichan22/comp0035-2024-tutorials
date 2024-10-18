from pathlib import Path
import pandas as pd

project_root = Path(__file__).parent.parent

csv_file1 = project_root.joinpath('data', 'npc_codes.csv')
csv_file2 = project_root.joinpath('data_db_activity', 'paralympics_events.csv')


df1 = pd.read_csv(csv_file1,  encoding_errors='ignore')
df2 = pd.read_csv(csv_file2, encoding_errors='ignore')

col_1 = pd.read_csv(csv_file1, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])
col_2 = pd.read_csv(csv_file2, encoding='utf-8', encoding_errors='ignore', usecols=['country'])


'''print(col_1)
print(col_2)
'''
df_merged = pd.read_csv(csv_file1, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])
print (col_2.join(col_1, on=None, how='left', lsuffix='', rsuffix='', sort=False, validate=None))

