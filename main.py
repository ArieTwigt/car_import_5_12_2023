from car_functions.import_functions import import_brand
from car_functions.conversion_functions import convert_list_to_df
from car_functions.export_functions import export_df_to_csv

from tqdm import tqdm


# get the brand from the input
selected_brands = input("Insert the brands:\n")

# split the string into a list with seperate values
selected_brands_list = selected_brands.split(" ")

# iterate over every brand in the list
for selected_brand in tqdm(selected_brands_list):
    #print(f"Importing {selected_brand}")

    # import the brand
    cars_list = import_brand(selected_brand)

    # convert the list to a DataFrame
    cars_df = convert_list_to_df(cars_list)

    # export the data frame to csv
    export_df_to_csv(cars_df, selected_brand)
