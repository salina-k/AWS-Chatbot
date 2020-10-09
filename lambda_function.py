import json
import requests
import datetime

def lambda_handler(event, context):
    City = event["currentIntent"]["slots"]["city"]
    r = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={"q": City , "appid":"06c57ad125a5b347806311fe779ba956"}).json()
    description = r["weather"][0]["description"]
    temperature = r["main"]["temp"]
    pressure = r["main"]["pressure"]
    humidity = r["main"]["humidity"]
    visibility = r["visibility"]
    wind_speed = r["wind"]["speed"]
    output = 'The weather in {} is: {} with  Humidity: {}, Temperature: {} , Pressure: {}, Visibility:{} and Wind speed: {} '.format(City, description, humidity, temperature, pressure, visibility, wind_speed)
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": output
            }
        }
    }