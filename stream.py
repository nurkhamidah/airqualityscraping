# Import modules
import streamlit as st
import pymongo as pm
import pandas as pd
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

# Configuration
st.set_page_config(
    page_title="Air Quality Scraping Project Mida",
    page_icon="👋",
    layout='wide',
)

# Define variables
tanggal = []
for i in range(0, len(vec_result)):
    tanggal.append(vec_result[i]["date"][0])
waktu = ["Pagi 06:00 WIB", "Siang 12:00 WIB", "Sore 18:00 WIB", "Malam 00:00 WIB"]

# Define headlines
st.markdown('<h1 style="text-align:center">Air Quality Statistics in Bogor, West Java</h1>', unsafe_allow_html=True)

i1, i2, i3 = st.columns([1,3,1])
with i2:
    st.image("https://images.pexels.com/photos/3613020/pexels-photo-3613020.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=700)
    st.caption("Sumber: [Pexels/tomfisk](https://www.pexels.com/photo/aerial-view-of-brown-and-white-building-3613020/)")

st.caption('<div style="text-align:center">Dibuat oleh Nur Khamidah dalam rangka project ST1562 IPB University mengenai scraping data. Berikut merupakan dashboard sederhana yang berisi informasi mengenai kualitas udara, indeks polutan, dan informasi cuaca terkini di kota Bogor, Jawa Barat. Enjoy! ❤</div>',
           unsafe_allow_html=True)

st.text("")

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

# Show table
b1, b2 = st.columns([1, 3])

# Air Quality Index Table
if appearance == "Air Quality Index":
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
    if period == "Tanggal":
      d = []
      tim = []
      for i in range(0, len(vec_result)):
          if vec_result[i]["date"][0] == period2:
              d.append(vec_result[i]["aqi_value"][0])
              tim.append(vec_result[i]["time"][0])
      d1 = pd.DataFrame(d, columns=["score", "unit", "desc"])
      tim1 = pd.DataFrame(tim, columns=["time"])
      st.table(pd.concat([tim1, d1], axis=1))
    if period == "Waktu":
      id = abs(waktu.index(period2) -2)
      t = []
      dat = []
      for i in range(0, len(vec_result)):
          if i % 4 == id:
              t.append(vec_result[i]["aqi_value"][0])
              dat.append(vec_result[i]["date"][0])
              
      t1 = pd.DataFrame(t, columns=["score", "unit", "desc"])
      dat1 = pd.DataFrame(dat, columns=["date"])
      st.table(pd.concat([dat1, t1], axis=1))
    if period == "Semua aja":
      s = []
      dat = []
      tim = []
      for i in range(0, len(vec_result)):
        s.append(vec_result[i]["aqi_value"][0])
        dat.append(vec_result[i]["date"][0])
        tim.append(vec_result[i]["time"][0])
      s1 = pd.DataFrame(s, columns=["score", "unit", "desc"])
      dat1 = pd.DataFrame(dat, columns=["date"])
      tim1 = pd.DataFrame(tim, columns=["time"])
      st.table(pd.concat([dat1, tim1, s1], axis=1))
      
# Pollution Index Table
if appearance == "Pollution Index":
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
    if period == "Tanggal":
      d = []
      tim = []
      for i in range(0, len(vec_result)):
          if vec_result[i]["date"][0] == period2:
              d.append(vec_result[i]["pm25_value"][0])
              tim.append(vec_result[i]["time"][0])
      d1 = pd.DataFrame(d, columns=["score", "unit", "desc"])
      tim1 = pd.DataFrame(tim, columns=["time"])
      st.table(pd.concat([tim1, d1], axis=1))
    if period == "Waktu":
      id = abs(waktu.index(period2) -2)
      t = []
      dat = []
      for i in range(0, len(vec_result)):
          if i % 4 == id:
              t.append(vec_result[i]["pm25_value"][0])
              dat.append(vec_result[i]["date"][0])
              
      t1 = pd.DataFrame(t, columns=["score", "unit", "desc"])
      dat1 = pd.DataFrame(dat, columns=["date"])
      st.table(pd.concat([dat1, t1], axis=1))
    if period == "Semua aja":
      s = []
      dat = []
      tim = []
      for i in range(0, len(vec_result)):
        s.append(vec_result[i]["pm25_value"][0])
        dat.append(vec_result[i]["date"][0])
        tim.append(vec_result[i]["time"][0])
      s1 = pd.DataFrame(s, columns=["score", "unit", "desc"])
      dat1 = pd.DataFrame(dat, columns=["date"])
      tim1 = pd.DataFrame(tim, columns=["time"])
      st.table(pd.concat([dat1, tim1, s1], axis=1))
      
# Weather Information Table
if appearance == "Weather Information":
  cols = ["weather", "temperature", "humidity", "wind", "pressure"]
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
    if period == "Tanggal":
      d = []
      tim = []
      for i in range(0, len(vec_result)):
          if vec_result[i]["date"][0] == period2:
              d.append(vec_result[i]["weather_info"][0])
              tim.append(vec_result[i]["time"][0])
      d1 = pd.DataFrame(d, columns=cols)
      tim1 = pd.DataFrame(tim, columns=["time"])
      st.table(pd.concat([tim1, d1], axis=1))
    if period == "Waktu":
      id = abs(waktu.index(period2) -2)
      t = []
      dat = []
      for i in range(0, len(vec_result)):
          if i % 4 == id:
              t.append(vec_result[i]["weather_info"][0])
              dat.append(vec_result[i]["date"][0])
              
      t1 = pd.DataFrame(t, columns=cols)
      dat1 = pd.DataFrame(dat, columns=["date"])
      st.table(pd.concat([dat1, t1], axis=1))
    if period == "Semua aja":
      s = []
      dat = []
      tim = []
      for i in range(0, len(vec_result)):
        s.append(vec_result[i]["weather_info"][0])
        dat.append(vec_result[i]["date"][0])
        tim.append(vec_result[i]["time"][0])
      s1 = pd.DataFrame(s, columns=cols)
      dat1 = pd.DataFrame(dat, columns=["date"])
      tim1 = pd.DataFrame(tim, columns=["time"])
      st.table(pd.concat([dat1, tim1, s1], axis=1))
      
# Klasemen US AQI score
l1, l2 = st.columns([1, 1])
with l1:
  st.markdown('<h3 style="align-text:center">US AQI Rank in Indonesia</h3>', unsafe_allow_html=True)
  st.table(pd.DataFrame(vec_result[len(vec_result)-1]["aqi_indo_rank"], columns=["#", "city", "US AQI"]))
with l2:
  st.markdown('<h3 style="align-text:center">US AQI Rank in Bogor</h3>', unsafe_allow_html=True)
  st.table(pd.DataFrame(vec_result[len(vec_result)-1]["aqi_local_rank"], columns=["#", "station", "US AQI"]))

# Footer
footer="""<style>
a:link , a:visited{
color: grey;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: white;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: relative;
left: 0;
bottom: 0;
width: 100%;
margin-bottom: -10px;
background-color: transparent;
color: grey;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.github.com/nurkhamidah" target="_blank">Mida</a></p>
</div>
"""
" "
" "
" "
" "
" "
" "
st.markdown(footer,unsafe_allow_html=True)