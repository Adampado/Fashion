# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 01:02:56 2023

@author: adamnjikam
"""

import os
import sqlite3

# Location of the images
default_path = "Image"

images = []
image_binary = []
# image_binary = bytearray(3)

# Get all images from given path and their names and BLOB
def image_to_binary(dir=default_path):

    # Get all names of images in the dir 
    if os.path.exists(dir): 
        for filename in os.listdir(dir):
            if filename.endswith("jpg") or filename.endswith("jpeg"):
                images.append(filename)
    # Read the images as binary data
    index = 0
    for i in range(len(images)):
        print("iteration number", i)
        with open(dir + '/' + images[i], 'rb') as f:
            image_binary.insert(i, bytearray(f.read()))
           # image_binary.append(bytearray(f.read()))
            index += 1

image_to_binary()
# --------------------------------------------------------

# Connect to database (create it if it doesn't exist)
conn = sqlite3.connect('fashionPrototypTest.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create a table with some columns
create_table_query = '''CREATE TABLE IF NOT EXISTS sample 
                    (Id INTEGER PRIMARY KEY,
                      "Image File Name" TEXT, 
                      "Outfit Type" TEXT,
                      Color TEXT,
                      Brand TEXT,
                      Price INTEGER,
                      Description TEXT,
                      data BLOB, 
                      )'''
                    
cursor.execute(create_table_query)
# --------------------------------------------------------

insert_query = "INSERT INTO sample ('Image File Name', 'Outfit Type', Color, Brand, Price, 'Description', data) VALUES (?,?,?,?,?,?,?)"
 
# get_image_sql = "SELECT data FROM sample WHERE Id = ?"

cursor.execute(insert_query, ('asos_design.jpeg','Casual', 'Marine blue', 'Asos', 45, 'Striped shirt', sqlite3.Binary(image_binary[0]),))
cursor.execute(insert_query, ('athletic_tshirt.jpeg', 'Athletic', 'Blue', 'Nike', 29.99, 'Dri-FIT, short sleeve', sqlite3.Binary(image_binary[1]),))
cursor.execute(insert_query, ('formal_black_suit.jpg', 'Formal', 'Black',  'Hugo', 299.99, 'Slim fit, two-piece',sqlite3.Binary(image_binary[2]),))
# cursor.execute(insert_query, ('casual_red_dress.jpg', 'Casual',	'Red', 'Zara', 49.99, 'A-line, floral',))

# --------------------------------------------------------
# cursor.execute(get_image_sql, (1,))
# result = cursor.fetchone()[0]
# img_data = bytes(result)

# Write the binary image data to a file
# with open('retrieved_image.jpg', 'wb') as f:
    # f.write(img_data)
# --------------------------------------------------------

# Commit changes and close the connection
cursor.close()
# conn.commit()
conn.close()
