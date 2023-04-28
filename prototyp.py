"""
Adam Njikam
"""
import urllib.request
import os
import sqlite3
from PIL import Image
from io import BytesIO
from PIL.ExifTags import TAGS

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
    for i in images:
        with open(dir + '/' + images[index], 'rb') as f:
            image_binary.append(bytearray(f.read()))
            index += 1

# download image from url and convert into a binary object
def image_frm_url(url):
    image_url = url
    
    # download the image from the URL and save it to a file
    urllib.request.urlretrieve(image_url, "image.jpg")
    with open("image.jpg", "rb") as f:
        image_bin_data = f.read()
        
    return image_bin_data


'''
 Function adds the image url to the image description
'''
def save_img_url(img, url):
    # get the metadata of the image
    exifdata = img.getexif()

    # decode the metadata tags and print them out
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
            print(f"{tag}: {data}")

    # modify the description tag of the image
    description = url
    exifdata[TAGS["ImageDescription"]] = description
           
    
def searchDB(colr=""):
        
    # connect to the SQLite3 database
    conn = sqlite3.connect('fashionPrototyp.db')
    cursor = conn.cursor()
    
    # define the name of the table and columns in the database where the image is stored
    table_name = "sample"
    image_column_name = "Data"
    
    if not not colr:
        colour = colr
        # retrieve the image binary data from the database table
        cursor.execute("SELECT {}, {} FROM {} WHERE {} = ?".format(image_column_name, 'Url',  table_name, 'colour'), (colour,))
        rows = cursor.fetchall()

        for row in rows:
            row_id = row[0]
            row_image = row[1]
            row_url = row[2]
            img = Image.open(BytesIO(row_image))
            save_img_url(img, row_url)
            
            # do something with the image, e.g., save it to a file or display it
            img.save("image_{}.jpg".format(row_id))
            # decode the image data and create a Pillow image object

        # show the image using Pillow's built-in image viewer
        # img.show()

        # close the database connection
        cursor.close()
        conn.close()

    

