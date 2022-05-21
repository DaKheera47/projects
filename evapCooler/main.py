# python_test.py
import requests

api_key = "e2702472a730b34849ba95a819481586"
complete_url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q=rawalpindi"

response = requests.get(complete_url)
x = response.json()

y = x["main"]

humidity = round(y["humidity"], 1)
temp = round(y["temp"] - 273.15, 1)

tempTable = {
    25: [12.0, 13.0, 14.5, 15.7, 17.5, 19.1, 21.5, 22.3, 23.7],
    27: [13.5, 14.5, 16.5, 17.4, 20.0, 21.2, 23.0, 24.6, 27.0],
    30: [15.5, 16.5, 19.0, 20.4, 22.5, 23.9, 26.0, 27.6, 30.0],
    32: [17.0, 18.0, 21.0, 22.6, 25.0, 26.6, 29.0, 30.4, 32.0],
    35: [19.0, 20.0, 23.0, 24.8, 27.5, 29.1, 31.5, 33.1, 35.0],
    37: [20.5, 22.7, 25.0, 26.8, 29.5, 31.1, 33.5, 37.0, 37.0],
    40: [22.0, 23.8, 26.5, 28.3, 31.0, 33.0, 40.0, 40.0, 40.0],
    42: [23.0, 25.0, 28.0, 29.8, 32.5, 42.0, 42.0, 42.0, 42.0],
    45: [24.0, 25.9, 28.9, 30.8, 45.0, 45.0, 45.0, 45.0, 45.0],
}
# 25: [{10: 12.0}, {20: 13.0}, {30: 14.5}, {40: 15.7}, {50: 17.5}, {60: 19.1}, {70: 21.5}, {80: 22.3}, {90: 23.7}],
# 27: [{10: 13.5}, {20: 14.5}, {30: 16.5}, {40: 17.4}, {50: 20.0}, {60: 21.2}, {70: 23.0}, {80: 24.6}, {90: 27.0}],
# 30: [{10: 15.5}, {20: 16.5}, {30: 19.0}, {40: 20.4}, {50: 22.5}, {60: 23.9}, {70: 26.0}, {80: 27.6}, {90: 30.0}],
# 32: [{10: 17.0}, {20: 18.0}, {30: 21.0}, {40: 22.6}, {50: 25.0}, {60: 26.6}, {70: 29.0}, {80: 30.4}, {90: 32.0}],
# 35: [{10: 19.0}, {20: 20.0}, {30: 23.0}, {40: 24.8}, {50: 27.5}, {60: 29.1}, {70: 31.5}, {80: 33.1}, {90: 35.0}],
# 37: [{10: 20.5}, {20: 22.7}, {30: 25.0}, {40: 26.8}, {50: 29.5}, {60: 31.1}, {70: 33.5}, {80: 37.0}, {90: 37.0}],
# 40: [{10: 22.0}, {20: 23.8}, {30: 26.5}, {40: 28.3}, {50: 31.0}, {60: 33.0}, {70: 40.0}, {80: 40.0}, {90: 40.0}],
# 42: [{10: 23.0}, {20: 25.0}, {30: 28.0}, {40: 29.8}, {50: 32.5}, {60: 42.0}, {70: 42.0}, {80: 42.0}, {90: 42.0}],
# 45: [{10: 24.0}, {20: 25.9}, {30: 28.9}, {40: 30.8}, {50: 45.0}, {60: 45.0}, {70: 45.0}, {80: 45.0}, {90: 45.0}],


def getOutputTemp(valueInTable):
    for i, ele in enumerate(tempTable):
        if ele == valueInTable:
            if humidity >= 0 and humidity <= 10:
                return tempTable[ele][0]

            if humidity >= 10 and humidity <= 20:
                return tempTable[ele][1]

            if humidity >= 20 and humidity <= 30:
                return tempTable[ele][2]

            if humidity >= 30 and humidity <= 40:
                return tempTable[ele][3]

            if humidity >= 40 and humidity <= 50:
                return tempTable[ele][4]

            if humidity >= 50 and humidity <= 60:
                return tempTable[ele][5]

            if humidity >= 60 and humidity <= 70:
                return tempTable[ele][6]

            if humidity >= 70 and humidity <= 80:
                return tempTable[ele][7]

            if humidity >= 80 and humidity <= 90:
                return tempTable[ele][8]



if temp >= 25 and temp <= 27:
    outputTemp = getOutputTemp(25)

elif temp >= 27 and temp <= 30:
    outputTemp = getOutputTemp(27)

elif temp >= 30 and temp <= 32:
    outputTemp = getOutputTemp(30)

elif temp >= 32 and temp <= 35:
    outputTemp = getOutputTemp(32)

elif temp >= 35 and temp <= 37:
    outputTemp = getOutputTemp(35)

elif temp >= 37 and temp <= 40:
    outputTemp = getOutputTemp(37)

elif temp >= 40 and temp <= 42:
    outputTemp = getOutputTemp(40)

elif temp >= 42 and temp <= 45:
    outputTemp = getOutputTemp(42)

print(f"{humidity = }%")
print(f"{temp = }°C")
print(f"{outputTemp = }°C")
