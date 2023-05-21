# -*- coding: utf-8 -*-
"""
@author: adamnjikam
"""
import json
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from jsonHandle import *

app = FastAPI()

@app.get("/option")
def testGetter(outfitType: str, color: str):
    lists = getImage(color, outfitType)
    return json.dumps(lists)

@app.get("/")
def read_root():
    return {"Beu": "Right place at the right time "}

@app.get("/filter")
def get_result_by_filter(colour: str = None, outfitType: str = None, brand: str = None):
    lists = filterSearch01(colr=colour, oType=outfitType, brnd=brand)
    return json.dumps(lists)


# Get the filter options entered. considering all posible cases 
# Code for other search options including price prefferences and others
# getting results from the json file of the database

# @app.get("/colour")
# def get_url(colour: str):
#     lists = filterSearch01(colr=colour)   
#     return json.dumps(lists)

# @app.get("/outfit/{outfitType}")
# def get_url(outfitType: str):
#     lists = getImage(outfitType=outfitType)    
#     return json.dumps(lists) 

# @app.get("/brand/{brand}")
# def get_brand(brand: str):
#     lists = getImage(brand = brand)
#     return json.dumps(lists)


        
# @app.get('outfit/{outfit}')
# def get_OutfitType(Outfit: str):
#     result = filterSearch02(OutfitType = Outfit)
#     return result
    

    
    