# -*- coding: utf-8 -*-
"""
@author: adamnjikam
"""
import json
import sqlite3

def saveDB_toJson():
    """
    Saves DB in Json file
    
    Paramters:
    None
    
    Returns:
    None.
    """
    
    # Connect to the database
    conn = sqlite3.connect("fashionPrototyp.db")
    cur = conn.cursor()

    # Execute a query to fetch data from the database
    cur.execute("SELECT * FROM sample")

    # Convert the data to a list of dictionaries
    data = []
    for row in cur.fetchall():
        data.append({
            "id": row[0],
            "ImageFileName": row[1],
            "OutfitType": row[2],
            "Colour": row[3],
            "Brand": row[4],
            "Price": row[5],
            "Description": row[6],
            "Data": row[7].decode('iso-8859-1'),
            "Url": row[8],
            "Style": row[9],
            "Patterns": row[10],
            "Season": row[11],
            "Accessories": row[12]
        })

    conn.close()

    dataset = {'sample': data}
    # Open file for writing
    with open("data.json", "w+") as json_file:
        # Write the JSON data to the file
        json.dump(dataset, json_file)
    

def getImage(colour=None, outfitType=None, brand=None):
    """
    Gets images and their respective Url from json file based on the colour
    
    Paramters: 
        Colour: Colour given by user as filter
    """
    lists = []
    #open json file
    with open("data.json", "r") as f:
        data = json.load(f)
    
    if colour is not None and outfitType is not None:
        for row in data["sample"]:
            result = []
            if row["Colour"].lower() == colour.lower() and row["OutfitType"].lower() == outfitType.lower():
                result.append(row["Data"])
                result.append(row["Url"])
                lists.append(result)
                break
            
    output = data["sample"]
    if colour:
        for row in output:
            result = []
            if row["Colour"].lower() == colour.lower():
                result.append(row["Data"])
                result.append(row["Url"])
                lists.append(result)
    
    # if outfitType:
    #     for row in data["sample"]:
    #         result = []
    #         if row["OutfitType"].lower() == outfitType.lower():
    #             result.append(row["Data"])
    #             result.append(row["Url"])
    #             lists.append(result)

    
            
            # img_file = io.BytesIO(bytearray(result[0].encode('iso-8859-1')))
            # img = Image.open((img_file))
         
            # img.show()
    # return a list of containing lists of image (as binary data) and url pair
    return lists

# getImage("Blue")

def filterSearch01(colr = None, oType = None, brnd = None):
    """
    Searches through json file using the filter options taken in as function argument
    
    Paramters: 
        colr: Colour given by user as filter
        oType: outfit type
        brnd: brand
    Return:
        returns a list of data(image)-Url pairs
    """
    #open json file
    with open("data.json", "r+") as f:
        data = json.load(f)
    
    filtered_product = data["sample"]
    # Apply color filter
    if colr: 
       filtered_product = [product for product in filtered_product if colr.lower() in product['Colour'].lower()]

    if oType:
       filtered_product = [product for product in filtered_product if oType.lower() in product["OutfitType"].lower()]
       
    if brnd:
       filtered_product = [product for product in filtered_product if brnd.replace(" ", "").lower() in product["Brand"].replace(" ", "").lower()]
       
    lists = []
    
    for product in filtered_product:
        result = []
        result.append(product['Data'])
        result.append(product['Url'])
        lists.append(result)
        
    return lists

# still needs to be fixed
def filterSearch02(outfit=None, colour=None, Brand=None, Price=None, Style=None, Patterns=None, Season=None, Accessories=None ):
    """
    Searches through database using the filter options taken in as function argument
    
    Paramters: 
        Colour: Colour given by user as filter
        
    """
    
    # Connect to the database
    conn = sqlite3.connect("fashionPrototyp.db")
    cur = conn.cursor()
    
    query = "SELECT Data, Url FROM sample WHERE 1=1"
    parameters = []
    
    if outfit:
        query += " AND OutfitType = {}".format(outfit)
        # query += f" AND OutfitType = '{OutfitType}'"
        # parameters.append(OutfitType)
        # parameters.append(f"OutfitType = '{OutfitType}'")
    if colour:
        parameters.append(f"Colour = '{colour}'")
    if Brand:
        parameters.append(f"Brand = '{Brand}'")
    if Style:
        parameters.append(f"Style = '{Style}'")
    if Patterns:
        parameters.append(f"Patterns = '{Patterns}'")
    if Season:
        parameters.append(f"Season = '{Season}'")
    if Accessories:
        parameters.append(f"Accessories = '{Accessories}'")
        
    if parameters:
        # query += " AND ".join(parameters)
        #exeute dynamic query
        cur.execute(query)
   
    for row in cur.fetchall():
        print(row)
        
    # Close the database connection
    conn.close()
    
    # results = []
    # for row in rows:
    #     result = {}
    #     for idx, column in enumerate(cur.description):
    #         result[column[0]] = row[idx]
    #     results.append(result) 
    # json_data = json.dumps(results)
        
    return

# saveDB_toJson()
# filterSearch02(outfit="casual")





