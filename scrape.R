#------------------------------------------------------
message("Loading the libraries")
library(rvest)
library(dplyr)
library(mongolite)

#------------------------------------------------------
message("Loading the URL(s)")
url <- "https://www.iqair.com/indonesia/west-java/bogor"
html <- read_html(url)

#------------------------------------------------------
message("Get AQI values")
aqi_score <- html %>% html_element(".aqi-value__value") %>% html_text()
aqi_unit <- html %>% html_element(".aqi-value__unit") %>% html_text()
aqi_desc <- html %>% html_element(".aqi-status__text") %>% html_text()

#------------------------------------------------------
message("Get air pollutant values (PM2.5 concentration")
pm25_score <- html %>% html_element(".mat-tooltip-trigger") %>% html_text()
pm25_unit <- (html %>% html_elements(".unit") %>% html_text2())[2]
pm25_desc <- paste0("PM2.5 concentration", html %>% html_element(xpath = '//*[@id="content-wrapper"]/app-routes-resolver/div/app-city/div[2]/div[2]/app-aqi-overview/div/div[2]/div[2]/app-who-guideline/div/p/text()') %>% html_text())

#------------------------------------------------------
message("Get recommendation")
recommendation <- html %>% html_elements(xpath = '//*[@id="content-wrapper"]/app-routes-resolver/div/app-city/div[2]/div[2]/app-aqi-overview/div/div[2]/div[3]/app-recommendation/div/div/table/tbody/tr/td[2]/text()') %>% html_text()

#------------------------------------------------------
message("Get US AQI rankings in Indonesia")
aqi_rank_indo <- (html %>% html_elements(".ranking__table") %>% html_table())[[1]]

#------------------------------------------------------
message("Get US AQI rankings in local location")
aqi_rank_local <- (html %>% html_elements(".ranking__table") %>% html_table())[[2]]

#------------------------------------------------------
message("Get additional informations")
info <- html %>% html_element(xpath = '//*[@id="content-wrapper"]/app-routes-resolver/div/app-city/div[2]/div[1]/app-weather/div/div[2]/table/tbody') %>% html_table()

db <- Sys.getenv("ATLAS_DB")
url <- Sys.getenv("ATLAS_URL")
collection <- Sys.getenv("ATLAS_COLLECTION")
con <- mongo(collection = collection,
             db = db,
             url = url)


