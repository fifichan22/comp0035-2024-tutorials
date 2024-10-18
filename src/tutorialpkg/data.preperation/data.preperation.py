if __name__ == '__main__':
    import pandas as pd
    from pathlib import Path

    # Use the correct file name
    project_root = Path(__file__).parent.parent
    csv_file = project_root.joinpath('data', 'paralympics_events_raw.csv')
    csv_file2= project_root.joinpath('data', 'paralympics_all_raw.xlsx')
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    #print no of rows and columns
    print('shape')
    print(df.shape)

    df['start'] = pd.to_datetime(df['start'], format='%d/%m/%Y')
    df['end'] = pd.to_datetime(df['end'], format='%d/%m/%Y')


    # Set pandas option to display all columns when printing a DataFrame
    print(pd.set_option("display.max_columns", None))

    df2 = pd.read_excel(csv_file2,sheet_name=0)
    df3 = pd.read_excel(csv_file2,sheet_name= 'medal_standings')
# Print column labels
    print("Column Labels:")
    print(df.columns)

    # Print column data types
    print("\nColumn Data Types:")
    print(df.dtypes)
    print(df2.head())
    print('metal standings',df3)

'''    # Print DataFrame Information
    print("DataFrame Information:")
    print(df.info())

    print(df.describe())

    # Optionally print the first few rows of the data to see what it looks like
    print("\nSample Data:")
    print(df.head(32))

    print("\nSample Excel:")
    print(df2.head(32))'''
    
columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']




def winner(column_name):
        """Find the smallest value in a specific column.

        Parameters:
        column_name (str): The name of the column to find the smallest value in.
        
        Returns:
        Value: The smallest value in the specified column.
        """
        # Check if the column exists in the DataFrame
        if column_name in df.columns:
            # Find the smallest value in the specified column
            smallest_value = df[column_name].min()
            print(f"The smallest value in the column '{column_name}' is: {smallest_value}")
            return smallest_value
        else:
            print(f"Column '{column_name}' does not exist in the DataFrame.")
            return None

    # Call the winner function, for example, to find the smallest value in the 'Year' column
'''    winner('year')'''