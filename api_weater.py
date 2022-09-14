import requests
from datetime import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru'
        resp = requests.get(url=url)
        data = resp.json()
        
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise_timestamp = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp
        weather_description = data['weather'][0]['description']

        print(f'***{datetime.now().strftime("%d-%m-%Y %H-%M")}***\n'
            f'Погода в городе {city}\nТемпература: {cur_weather}\n'
            f'Влажность {humidity}%\nДавление {pressure} мм.рт.ст.\nВетер {wind_speed} м/c\n'
            f'Восход Солнца {sunrise_timestamp}\n'
            f'Закат Солнца {sunset_timestamp}\n'
            f'Продолжительность дня {length_of_day}\n'
            f'Описпание погоды {weather_description.title()}\n'
            f'Хорошего дня!'
            )

    except Exception as err:
        print(err)
        print('Проверьте название города')


def main():
    city = input('City: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()

