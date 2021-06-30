from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def format_response(city):
    weather_key = "60ff63928fdae5f8af04f87991fa7517"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "Metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    name = weather['name']
    desc = weather['main'][0]['description']
    temp = weather['main']['temp']
    hum = weather['main']['humidity']
    return "City %s Condition: %s Temperature : %s (C) Humadity : %s word" % (
        name, desc, temp, hum)



@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        city = request.form['city']
        weather_data = format_response(city)
        return render_template('home.html', data=weather_data)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

