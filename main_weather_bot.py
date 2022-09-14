import requests
import datetime
from config import open_weather_token, tg_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши название города!')

@dp.message_handler()
async def get_weather(message: types.Message):

    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang=ru'
        resp = requests.get(url=url)
        data = resp.json()
        
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp
        weather_description = data['weather'][0]['description']

        await message.reply(f'***{datetime.datetime.now().strftime("%d-%m-%Y %H-%M")}***\n'
            f'Погода в городе {city}\nТемпература: {cur_weather}\n'
            f'Влажность {humidity}%\nДавление {pressure} мм.рт.ст.\nВетер {wind_speed} м/c\n'
            f'Восход Солнца {sunrise_timestamp}\n'
            f'Закат Солнца {sunset_timestamp}\n'
            f'Продолжительность дня {length_of_day}\n'
            f'Описпание погоды {weather_description.title()}\n'
            f'*** Хорошего дня! ***'
            )

    except Exception as ex:
        await message.reply(ex)
        await message.reply('\U00002620 Проверьте название города! \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
