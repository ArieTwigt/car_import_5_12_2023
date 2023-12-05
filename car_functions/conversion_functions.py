import pandas

def convert_list_to_df(cars_list):
    """
    Converts a cars_list to a pandas DataFrame

    Parameters:

    * cars_list
    
    """

    # conver the list to a pandas DataFrame
    cars_df = pandas.DataFrame(cars_list)

    # specify the columns
    selected_columns = ['kenteken', 'merk', 'handelsbenaming', 'eerste_kleur', 'catalogusprijs']

    # filter the DataFrame for the selected columns
    cars_df_filtered = cars_df[selected_columns]

    return cars_df_filtered
