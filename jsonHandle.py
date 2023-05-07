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
    

def getImage(colour):
    """
    Gets images and their respective Url based on the colour
    
    Paramters: 
        Colour: Colour given by user as filter
    """
    
    lists = []
    #open json file
    with open("data.json", "r") as f:
        data = json.load(f)
    
    # Iterate over table with matching colour
    for row in data["sample"]:
        result = []
        if row["Colour"].lower() == colour.lower():
            result.append(row["Data"])
            result.append(row["Url"])
            lists.append(result)

            # img_file = io.BytesIO(bytearray(result[0].encode('iso-8859-1')))
            # img = Image.open((img_file))
            # img.show()
            
# getImage("Blue")

saveDB_toJson()







