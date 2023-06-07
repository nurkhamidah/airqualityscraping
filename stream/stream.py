import pymongo as pm
import streamlit as st
import os

# Define database connection
con = pm.MongoClient(os.getenv("ATLAS_URL"))
db = con[os.getenv("ATLAS_DB")]
collection = db[os.getenv("ATLAS_COLLECTION")]

# Test get all data
for x in collection.find():
  print(x)