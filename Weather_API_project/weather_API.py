import requests 
import os
from flask import Flask
from flask import jsonify




API_KEY = os.getenv("API_KEY")

response=requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK?key={API_KEY}')

app = Flask(__name__)







if __name__=="__main__":
    app.run(debug=True)

