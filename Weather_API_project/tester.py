from flask import request
import requests
import os
from flask import Flask
from flask import jsonify
import requests
from dotenv import load_dotenv
import os
from flask_limiter import Limiter
import redis
from flask_limiter.util import get_remote_address
import json
import logging


load_dotenv()

redis_host='redis-19287.c338.eu-west-2-1.ec2.cloud.redislabs.com'
redis_port='19287'
redis_password=os.getenv('redis_password')
redis_username=os.getenv('redis_username')
redis_expiry=3600*3


r=redis.Redis(
    host=redis_host,
    port=redis_port,
    username=redis_username,
    password=redis_password,
)




app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=f"redis://:{redis_password}@{redis_host}:{redis_port}/0"
)




def get_weather():
    filter_end='2025-01-29'
    filter_start='2025-01-28'
    location='Edinburgh'
    redis_key=location+filter_start+filter_end

    URL=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{filter_start}/{filter_end}?key={os.getenv("API_KEY")}'


    try:
        cached_data=r.get(redis_key)
        if cached_data:
            data = json.loads(cached_data.decode('utf-8'))
            print(json.dumps(data, indent=2))
            return
        
    except redis.RedisError as redis_error:
        logging.error(f'redis error : {redis_error}')



    

    response=requests.get(URL)

    

    if response.status_code==200:
        try:
            r.setex(redis_key,redis_expiry,json.dumps(response.json()))
            logging.info('saving response to cache')
        except redis.RedisError as redis_error:
            logging.error(f'failed to cache response : {redis_error}')

        data = response.json()
        print(json.dumps(data, indent=2),200)
        return

    elif 500<=response.status_code<600:
        logging.error(f'server error occured')
        return f"request failed with response status {response.status_code}",500
    
    elif 400<=response.status_code<500:
        logging.error(f"client error occured")
        return f"client error occured request failed with response status {response.status_code}",400
    
    else:
        logging.error(f"unknown error occured")
        return f"an unknown error occured request failed with response status {response.status_code}"

    

    




get_weather()

