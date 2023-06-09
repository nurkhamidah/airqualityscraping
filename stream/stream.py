import pymongo as pm
import streamlit as st
import os

# ------------------------ MONGO DB ATLAS ------------------------

# Define database connection
con = pm.MongoClient(os.getenv("ATLAS_URL"))
db = con[os.getenv("ATLAS_DB")]
collection = db[os.getenv("ATLAS_COLLECTION")]

# Test get all data
vec_result = []
for x in collection.find():
  vec_result.append(x)
  
# ------------------------ STREAMLIT ------------------------

# Define variables
tanggal = []
for i in range(0, len(vec_result)):
    tanggal.append(vec_result[i]["date"][0])
waktu = ["Pagi 06:00 WIB", "Siang 12:00 WIB", "Sore 18:00 WIB", "Malam 00:00 WIB"]

# Define headlines
st.markdown('<h1 style="text-align:center">Ini judulnya</h1>', unsafe_allow_html=True)
st.caption('<div style="text-align:center">Ini captionnya.</div>',
           unsafe_allow_html=True)

# Define today's statistics
with st.expander('Statistik Terakhir', expanded=True):
    e1, e2, e3, e4 = st.columns([1, 1, 1, 2])
    with e1:
      d1 = int(vec_result[len(vec_result)-1]["aqi_value"][0]["score"])-int(vec_result[len(vec_result)-2]["aqi_value"][0]["score"])
      st.metric("Air Quality Index", vec_result[len(vec_result)-1]["aqi_value"][0]["score"], delta=d1)
      st.caption(vec_result[len(vec_result)-1]["aqi_value"][0]["desc"])
    with e2:
      d2 = float(vec_result[len(vec_result)-1]["pm25_value"][0]["score"])-float(vec_result[len(vec_result)-2]["pm25_value"][0]["score"])
      st.metric("PM2.5 Pollutant Index", vec_result[len(vec_result)-1]["pm25_value"][0]["score"], delta=round(d2, 3))
      st.caption(vec_result[len(vec_result)-1]["pm25_value"][0]["desc"])
    with e3:
      d3 = float(vec_result[len(vec_result)-1]["weather_info"][0]["temperature"][:2])-float(vec_result[len(vec_result)-2]["weather_info"][0]["temperature"][:2])
      st.metric("Air Temperature", vec_result[len(vec_result)-1]["weather_info"][0]["temperature"], delta=round(d3, 3))
      st.caption("The weather in Bogor is currently "+ vec_result[len(vec_result)-1]["weather_info"][0]["weather"].lower())
    with e4:
      st.write("Some recommendations:")
      for i in vec_result[len(vec_result)-1]["recommendation"]:
        st.markdown("- " + i)
        
# Choose the mode
a1, a_center, a2 = st.columns([1, 2, 1])
with a_center:
  appearance = st.selectbox("Mau liat apa?", 
                            ["Air Quality Index", "Pollution Index", "Weather Information"])

b1, b2 = st.columns([1, 3])
with b1:
  period = st.selectbox("Berdasarkan apa?", 
                        ["Tanggal", "Waktu", "Semua aja"])
  if period == "Tanggal":
    period2 = st.selectbox("Tanggal berapa?", set(tanggal))
  if period == "Waktu":
    period2 = st.selectbox("Kapan nih?", waktu)
  if period == "Semua aja":
    period2 = "Semua"
with b2:
  if period2 == "2023-06-09":
    "Test aja ini, maasih dipusingin"
  if period2 == "Siang 12:00 WIB":
    "Ya ini juga sama pusingnya"
