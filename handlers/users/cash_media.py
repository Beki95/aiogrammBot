from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, MediaGroup
from loader import dp, bot


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def content_photo(message: types.Message):
    await message.reply(f"ваша фото {message.photo[-1].file_id}")


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def content_video(message: types.Message):
    await message.reply(f"{message.video.file_id}")


@dp.message_handler(Command("get_cat"))
async def command_get_cat(message: types.Message):
    photo_file_id = "AgACAgIAAxkBAAIElV_x9CvQzLU8UQAB7kcqDxfk4DEt6wACfLAxG8yCkUtq2o-lYT7D3ShM1JouAAMBAAMCAAN5AAOhMAACHgQ"
    photo_url = "https://i.pinimg.com/736x/9e/a7/3e/9ea73ea048f8ad0ab3a10eb3161f9398.jpg"
    photo_bites = InputFile(path_or_bytesio="photos/file_2.jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption="это фото кота /more_cats")


@dp.message_handler(Command("more_cats"))
async def command_more_cats(message: types.Message):
    albom = MediaGroup()
    photo_id = "AgACAgIAAxkBAAIElV_x9CvQzLU8UQAB7kcqDxfk4DEt6wACfLAxG8yCkUtq2o-lYT7D3ShM1JouAAMBAAMCAAN5AAOhMAACHgQ"
    photo_url = "https://i.pinimg.com/736x/9e/a7/3e/9ea73ea048f8ad0ab3a10eb3161f9398.jpg"
    photo_bites = InputFile(path_or_bytesio="photos/file_2.jpg")
    video = "BAACAgIAAxkBAAIEvF_x-xgpWMNhe5RB4sHArJyifFSrAALfCgACzIKRS9Sr8WC9cEdIHgQ"
    albom.attach_photo(photo_id)
    albom.attach_photo(photo_bites)
    albom.attach_photo(photo_url, caption="https://i.pinimg.com/736x/9e/a7/3e/9ea73ea048f8ad0ab3a10eb3161f9398.jpg")
    albom.attach_video(video)
    # await bot.send_media_group(chat_id=message.from_user.id, media=albom)
    await message.answer_media_group(media=albom)

