from flask import request
import os
from flask import Flask
from flask import jsonify
import requests
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()

API_KEY=os.getenv("API_KEY")

app = Flask(__name__)




@app.route("/weather", methods=["GET"])
def get_weather():
    filter_end=request.args.get('end',"")
    filter_start=request.args.get('start',"")
    location=request.args.get('location')



    URL=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{filter_start}/{filter_end}?key={API_KEY}'

    response=requests.get(URL)
    return jsonify(response.json())





if __name__=="__main__":
    app.run(debug=True)

