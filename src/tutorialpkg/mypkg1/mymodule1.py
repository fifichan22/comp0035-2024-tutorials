
from pathlib import Path 
import pandas as pd

if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.

    # Use the correct file name
    project_root = Path(__file__).parent.parent
    csv_file = project_root.joinpath('data', 'tutorialpkg')
''
'''    from tutorialpkg.mypkg2.mymodule2_2 import fetch_user_data
    from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle


    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")
    # Mock database (you can replace this with the actual database later)
    mock_database = {
        42: {"name": "Tobi Oshodi", "email": "tobi@example.com"},
        43: {"name": "Jane Doe", "email": "jane@example.com"}
    }
''
    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))'''

paralympics_datafile_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')
# Print the path of the located file
print(f"Data file path: {paralympics_datafile_csv}")

# Check if the file exists
if paralympics_datafile_csv.exists():
    print(f"CSV file found: {paralympics_datafile_csv}")
else:
    print("CSV file not found.")

df_para = pd.read_csv(paralympics_datafile_csv)
print(df_para.head())