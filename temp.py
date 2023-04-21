# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import io
import os
import sqlite3
from PIL import Image 

# Location of the images
path = "Image"
images = []
# image_binary = bytearray(3)
image_binary = []
image_binary1 = []

# Get all names of images in the dir 
if os.path.exists(path): 
    for filename in os.listdir(path):
        if filename.endswith("jpg") or filename.endswith("jpeg"):
            images.append(filename)

# Read the images as binary data
index = 0
# for i in images:
with open(path + '/' + images[0]) as f:
    image_binary = f.read()
     #   index += 1
with open(path + '/' + images[1], 'rb') as f1:
    image_binary1 = f1.read()


# Convert the image data to binary format
img = Image.open
buf = io.BytesIO()
img.save(buf, format='JPEG')
img_data = buf.getvalue()

# Connect to database (create it if it doesn't exist)
conn = sqlite3.connect('fashionPrototyp.db')

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
                     data BLOB NOT NULL, 
                     "Product Description" TEXT)'''
cursor.execute(create_table_query)



# Insert some data into the table
cursor.execute('''INSERT INTO sample ('Image File Name', 'Outfit Type', Color, Brand, Price, data) 
               VALUES ('asos design','Casual', 'Marine blue', 'Asos', 45, ?)''', (image_binary[0]))
cursor.execute("INSERT INTO sample (Image File Name, Outfit Type, Color, Brand, Price, data) VALUES ('pierre cardin','Casual', 'Pink', 'Zarlando', 57, image_binary1)")

# Commit changes and close the connection
conn.commit()
conn.close()

'''
# path = 'C:/Program Files/SQLiteStudio/fashion.db'
path = 'fashion.db'

if os.path.isfile(path):
    try: 
        conn = sqlite3.connect(path)

        # Cursor to interact with database
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Prototyp")

        result = cursor.fetchall()
        for row in result:
            print(row)
            
        conn.close()
    except sqlite3.Error as e:
        print(e)
else:
    print("Database does not exist")
    
'''
# ---------------------------------------------

"""

from PIL import Image 
# Location of the images
path = "imageTester"
images = []

if os.path.exists(path): 
    for filename in os.listdir(path):
        if filename.endswith("jpg") or filename.endswith("jpeg"):
            images.append(filename)
    print(images)
n = 0
for i in images:
    image = Image.open(path+'/'+images[n])
    n += 1
    image.show()
"""