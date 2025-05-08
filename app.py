from flask import Flask, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENWEATHER_API_KEY = os.getenv("API_KEY")  # Access my API key

def get_balloon_data():
    balloons = []
    for i in range(24):  # last 24 hours
        try:
            url = f"https://a.windbornesystems.com/treasure/{i:02}.json"
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                data = res.json()
                if isinstance(data, list):
                    for point in data:
                        if isinstance(point, list) and len(point) >= 2:
                            balloon = {
                                "lon": point[0],
                                "lat": point[1],
                                "alt": point[2] if len(point) > 2 else None
                            }
                            balloons.append(balloon)
        except Exception as e:
            print(f"Error: {e}")
            continue
    print(f"Total balloons processed: {len(balloons)}")
    return balloons

def get_weather(lat, lon):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
    try:
        res = requests.get(weather_url)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print(f"Could not get data for: ({lat}, {lon}): {e}")
    return None


@app.route("/")
def index():
    balloon_data = get_balloon_data()
    results = []

    for balloon in balloon_data[:20]:  # Limit for speed
        lat = balloon["lat"]
        lon = balloon["lon"]
        weather = get_weather(lat, lon)

        if weather and "main" in weather:
            info = {
                "lat": lat,
                "lon": lon,
                "temperature": round(weather["main"]["temp"] - 273.15, 1),
                "condition": weather["weather"][0]["description"]
            }
            results.append(info)

    return render_template("index.html", balloons=results)


if __name__ == "__main__":
    app.run(debug=True)
