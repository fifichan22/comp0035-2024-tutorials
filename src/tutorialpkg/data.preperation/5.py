from pathlib import Path
import pandas as pd

project_root = Path(__file__).parent.parent

csv_file1 = project_root.joinpath('data', 'npc_codes.csv')
csv_file2 = project_root.joinpath('data', 'paralympics_events_raw.csv')


df1 = pd.read_csv(csv_file1,  encoding_errors='ignore')
df2 = pd.read_csv(csv_file2, encoding_errors='ignore')

col_1 = pd.read_csv(csv_file1, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])
col_2 = pd.read_csv(csv_file2, encoding='utf-8', encoding_errors='ignore', usecols=['country'])


left_df=col_2.merge(col_1, how='left', left_on='col_1', right_on='col_2')

