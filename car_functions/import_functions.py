import requests


def import_brand(brand):
    """
    Import cars from the RDW API given a brand

    Parameters:

    * brand
    
    """

    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint 
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # check the status_code
    if response.status_code != 200:
        raise ValueError(f"Error for {brand}")

    # get the data from the response
    data = response.json()

    # check if the data is not empty
    if len(data) == 0:
        raise ValueError(f"No cars found for {brand}")

    return data

