# Weather API with Cache, Flask and Flask Limiter


https://github.com/benjo27maker/Weather_API_project

https://roadmap.sh/projects/weather-API


This project is a weather API written in Python with an integrated redis caches-system runnin using a flask server and features a flask limiting function. It allows users to
request weather data from a given location as well as including optional start and end time queries. It ets its data from the visual crossings weather API (https://www.visualcrossing.com)

---

## Features

- retrieve data from redis cache
- retrieve data from 3rd part APi
- store data in redis cache
- limit requests numbers per user

---

## Requirements

- python3
- Flask
- Redis
- Visual Crossing Weather API
- SSL/TLS support for redis connections

---

## Setup


### 1. Clone Repositary
```bash
git clone https://github.com/yourusername/yourrepository.git cd yourrepository
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create Environment Variables
```bash
touch.env
REDIS_PASSWORD=your_redis_password
WEATHER_API_KEY=your_visual_crossing_weather_api_key
```


---

## Usage

Example command

```bash
curl "http://127.0.0.1:5000/location?city=Edinburgh&start=2025-11-22&end=2025-11-21"
```
request takes location argument as well as start and end time queries

### 4. Run the Application
```bash
cd API
flask --app app run
```
