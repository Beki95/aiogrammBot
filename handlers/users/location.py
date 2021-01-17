from aiogram import types
from aiogram.dispatcher.filters import Command
import requests

from keyboards.default.buttons_ import location, contact
from loader import dp


def get_address_from_coords(coords):
    PARAMS = {
        "apikey": "951c644a-c95f-428c-b34c-9753489739f2",
        "format": "json",
        "lang": "ru_RU",
        "kind": "house",
        "geocode": coords
    }

    try:
        r = requests.get(url="https://geocode-maps.yandex.ru/1.x/", params=PARAMS)
        json_data = r.json()
        address_str = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]
        country_code = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["AddressDetails"]["Country"]["CountryNameCode"]
        return address_str, f"Код страны {country_code}"

    except Exception as e:
        # единственное что тут изменилось, так это сообщение об ошибке.
        return "Не могу определить адрес по этой локации/координатам.\n\nОтправь мне локацию или координаты (долгота, широта):"


@dp.message_handler(Command("show_on_map"))
async def command_loc(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}"
                         f" Отправьте мне свою гео позицию нажав на кнопку", reply_markup=location)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def location__(message: types.Message):
    locations = message.location
    lon = locations.longitude
    lat = locations.latitude
    await message.answer(f"Спасибо за гео позицию ваша долгота-{lon}, широта-{lat}")
    coords = f"{lon, lat}"
    ad = get_address_from_coords(coords=coords)
    await message.answer(f"{ad}")


@dp.message_handler(Command("contact"))
async def get_contact(message: types.Message):
    await message.answer("Отправьте мне свои контактные данные нажав на кнопку", reply_markup=contact)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact_(message: types.Message):
    con = message.contact
    await message.answer(f"вас зовут {con.full_name},\n\n"
                         f"ваши контактные данные {con.phone_number}")
