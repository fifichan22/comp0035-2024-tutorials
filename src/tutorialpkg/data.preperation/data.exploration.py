import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

if __name__ == '__main__':
    project_root = Path(__file__).parent.parent
    csv_file = project_root.joinpath('data', 'paralympics_events_raw.csv')
    csv_file2= project_root.joinpath('data', 'paralympics_all_raw.xlsx')
    df = pd.read_excel(csv_file2)
    columns_to_plot_1 = df['participants_m']
    columns_to_plot_2 = df['participants_f']
    columns_to_plot_1.hist()
    columns_to_plot_2.hist()
    plt.show()
    # Filter the DataFrame to select only rows where 'type' is 'summer'
    # syntax: df = df[df['column_name'] == filter_value]
    summer_df = df[df['type'] == 'summer']
    summer_df.hist()
    plt.show()
    winter_df = df[df['type'] == 'winter']
    summer_df.hist()
    plt.show()
    df = df.fillna(0)
'''   df[columns_to_plot_1] = df[columns_to_plot_1].astype(int)
    

    # Plot individual box plots for specified columns
    df.select_dtypes(include='number').plot.box()
    plt.suptitle('Combined Box Plot for All Numeric Columns')
    plt.show()'''

df.groupby("type").plot(x="start", y="participants")
plt.show()