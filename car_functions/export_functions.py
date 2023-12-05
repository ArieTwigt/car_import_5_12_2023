import os
from datetime import datetime


def export_df_to_csv(df, brand):
    """
    Exports a DataFrame to csv

    Parameters:

    * df
    """

    # specify folder the path
    folder_path = f"data/{brand}"

    # create the directory
    os.makedirs(folder_path, exist_ok=True)

    # create a string for the date and time
    current_date_time = datetime.now()

    # get the string from the date and time
    current_datetime_str = current_date_time.strftime("%Y%m%d%H%M%S")

    # specify the file path
    file_path = f"{folder_path}/export_{current_datetime_str}_{brand}.csv"

    # expor the file to csv
    df.to_csv(file_path)

    #print(f"✅ Succesfully exported {file_path}")