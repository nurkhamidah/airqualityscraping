# Air Quality Statistics Scraping Project
[![Scrape Bogor Air Quality Profile](https://github.com/nurkhamidah/airqualityscraping/actions/workflows/airquality-scrape.yml/badge.svg)](https://github.com/nurkhamidah/airqualityscraping/actions/workflows/airquality-scrape.yml)

## About

*Project* ini merupakan integrasi antara **R - MongoDB Atlas - Python** yang meliputi *scraping* data dengan `rvest` pada R dan disajikan dengan Streamlit App. Informasi yang disajikan dalam project kali ini adalah beberapa indeks kualitas udara kota Bogor, Jawa Barat yang meliputi *US Air Quality Index*, *PM2.5 Index*, dan beberapa informasi mengenai cuaca terkini yang diambil dari web [berikut](https://www.iqair.com/indonesia/west-java/bogor).

## Access to the App

Aplikasi *dashboard* hasil *scraping* dapat dilihat pada link berikut:

[![Akses Project Dashboard]](https://ipb.link/airquality-mida)

[Akses Project Dashboard]: https://img.shields.io/badge/Akses_Project_Dashboard-37a779?style=for-the-badge

## Struktur Database

```
{"_id":
  {"$oid":"647f3ded75215e914d0cb981"},
  "id":[{"$numberDouble":"14.0"}],
  "date":["2023-06-06"],
  "time":["2023-06-06 21:08:45.653358"],
  "aqi_value":[{
    "score":"77",
    "unit":" US AQI ",
    "desc":"Moderate"
  }],
  "pm25_value":[{
    "score":"24.7",
    "unit":"µg/m³",
    "desc":"PM2.5 concentration in Bogor is currently 4.9 times the WHO annual air quality guideline value"
  }],
  "recommendation":[
    " Sensitive groups should wear a mask outdoors",
    " Sensitive groups should run an air purifier",
    " Close your windows to avoid dirty outdoor air",
    " Sensitive groups should reduce outdoor exercise"],
  "aqi_local_rank":[
    {"#":{"$numberInt":"1"},
    "station":"Darul Quran Mulia",
    "US AQI":{"$numberInt":"162"}},
    {"#":{"$numberInt":"2"},
    "station":"Northridge, Sentul city",
    "US AQI":{"$numberInt":"77"}}
  ],
  "aqi_indo_rank":[
    {"#":{"$numberInt":"1"},"city":"Bandung, West Java","US AQI":{"$numberInt":"171"}},
    {"#":{"$numberInt":"2"},"city":"Cileungsir, West Java","US AQI":{"$numberInt":"161"}},
    {"#":{"$numberInt":"3"},"city":"Pasarkemis, West Java","US AQI":{"$numberInt":"155"}},
    {"#":{"$numberInt":"4"},"city":"South Tangerang, Banten","US AQI":{"$numberInt":"153"}},
    {"#":{"$numberInt":"5"},"city":"Jakarta, Jakarta","US AQI":{"$numberInt":"144"}},
    {"#":{"$numberInt":"6"},"city":"Serang, Banten","US AQI":{"$numberInt":"137"}},
    {"#":{"$numberInt":"7"},"city":"Bekasi, West Java","US AQI":{"$numberInt":"115"}},
    {"#":{"$numberInt":"8"},"city":"Banjarbaru, South Kalimantan","US AQI":{"$numberInt":"107"}},
    {"#":{"$numberInt":"9"},"city":"Batam, Riau Islands","US AQI":{"$numberInt":"98"}},
    {"#":{"$numberInt":"10"},"city":"Bogor, West Java","US AQI":{"$numberInt":"91"}}
  ],
  "weather_info":[{
    "weather":"Broken clouds",
    "temperature":"78.8°F",
    "humidity":"89%",
    "wind":"1.5 mp/h",
    "pressure":"29.9 Hg"
  }]
}
```
## Contributor

Nur Khamidah, 2023
