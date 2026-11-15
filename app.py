from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()
   # import os

app = Flask(__name__)

NASA_API_KEY =  os.getenv("NASA_API_KEY")


def get_apod():
    from datetime import datetime, timedelta

    #cuba hari ni dlu
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={today}"
    response = requests.get(url)

    #kalau hari ni error, cuba semalam
    if response.status_code  != 200:
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={yesterday}"
        response = requests.get(url) 

    if response.status_code == 200:      
        return response.json()
    return None

@app.route("/")
def home():
    apod = get_apod()
    return render_template("index.html", apod=apod)

if __name__ == "__main__":
    app.run(debug=True)
    #@app.route("/")
    #def home():
    #    return render_template("index.html")

    #if __name__ == "__main__":
    #    app.run(debug=True)