from flask import request
import os
from flask import Flask
from flask_limiter import Limiter
import redis
from flask_limiter.util import get_remote_address
import requests
from dotenv import load_dotenv
import os
import redis
import logging
import json

# loading environment variables
load_dotenv()

# setting up redis cache 
redis_host='redis-19287.c338.eu-west-2-1.ec2.cloud.redislabs.com'
redis_port='19287'
redis_password=os.getenv('redis_password')
redis_username=os.getenv('redis_username')
redis_expiry=3600*3


# passing redis its information
r=redis.Redis(
    host=redis_host,
    port=redis_port,
    username=redis_username,
    password=redis_password,
)



# creating server to host API
app = Flask(__name__)

# setting up rate limiter for API requests
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=f"redis://:{redis_password}@{redis_host}:{redis_port}/0"
)

# creating location route to return weather data
@app.get("/location")
def weather_route():
    city = request.args.get("city", "")  
    filter_start = request.args.get("start", None) 
    filter_end = request.args.get("end", None) 
    if filter_start:
        filter_start = "/" + filter_start
    else:
        filter_start = ""

    if filter_end:
        filter_end = "/" + filter_end
    else:
        filter_end = "" 
        

    return get_weather(city,filter_start,filter_end)


def get_weather(location,filter_start,filter_end):
    '''this function requests weather data from a 3rd party API
    
    args: location (str), filter_start (str), filter_end (str)

    returns: weather data (json) or error message
    
    '''

    # creates redis key from http queries
    redis_key=location+filter_start+filter_end

    # creates a URL from the location, start time and end time
    URL=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline{location}{filter_start}/{filter_end}?key={os.getenv("API_KEY")}'

    # trying to fetch data from cache
    try:
        cached_data=r.get(redis_key)
        if cached_data:
            data = json.loads(cached_data.decode('utf-8'))
            return json.dumps(data, indent=2)
    
    except redis.RedisError as redis_error:
        logging.error(f'redis error : {redis_error}')



    
    # fetches data from 3rd party API otherwise
    response=requests.get(URL)

    
    # if request successful return data
    # stores new data in cache
    if response.status_code==200:
        try:
            r.setex(redis_key,redis_expiry,json.dumps(response.json()))
            logging.info('saving response to cache')
        except redis.RedisError as redis_error:
            logging.error(f'failed to cache response : {redis_error}')

        data = response.json()
        return json.dumps(data, indent=2),200

    # if request is unsuccessful return error message
    # 3rd party failure
    elif 500<=response.status_code<600:
        logging.error(f'server error occured')
        return f"request failed with response status {response.status_code}",500
    # error in query format in request
    elif 400<=response.status_code<500:
        logging.error(f"client error occured")
        return f"client error occured request failed with response status {response.status_code}",400
    # unknown error
    else:
        logging.error(f"unknown error occured")
        return f"an unknown error occured request failed with response status {response.status_code}"

    

    






# creates the server and makes request when the program is run
if __name__=="__main__":
    app.run(debug=True)

