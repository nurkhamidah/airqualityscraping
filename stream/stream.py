import pymongo as pm
import streamlit as st
import os

# Define database connection
con = pm.MongoClient(os.getenv("ATLAS_URL"))
db = con[os.getenv("ATLAS_DB")]
collection = db[os.getenv("ATLAS_COLLECTION")]

collection.find_one()
# Test get all data
vec_result = []
for x in collection.find():
  vec_result.append(x)

st.set_page_config(
    page_title="Air Quality Scraping Project",
    page_icon="👋",
    layout='wide',
)

st.markdown('<h1 style="text-align:center">Ini judulnya</h1>', unsafe_allow_html=True)
st.caption('<div style="text-align:center">Ini captionnya.</div>',
           unsafe_allow_html=True)

# expander for last statistics

# choose the mode
a1, a_center, a2 = st.columns([1, 2, 1])
a_options = ["Air Quality Index", "Pollution Index", "Weather Information"]
with a_center:
  appearance = st.selectbox("Mau liat apa?", a_options)