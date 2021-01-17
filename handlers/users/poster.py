from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import admins, chanels
from keyboards.inline.check import confermation_keyboard, post_callback
from loader import dp, bot
from states.poster import New_post


@dp.message_handler(Command("create_post"))
async def command_create_post(message: types.Message):
    await message.answer("Оправьте текст на публикацию")
    await New_post.EnterMessage.set()


@dp.message_handler(state=New_post.EnterMessage)
async def new_post(message: types.Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("Вы собераетесь отправить пост на публикацию", reply_markup=confermation_keyboard)
    await New_post.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=New_post.Confirm)
async def post(call: types.CallbackQuery, state: FSMContext):
    global id
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    await call.answer()
    id = call.message.chat.id
    await call.message.answer("Вы отправили пост на публикацию ждите ответа")
    await bot.send_message(chat_id=admins[0], text=f"Пользователь {mention} Хочет сделать пост")
    await bot.send_message(chat_id=admins[0], text=f"{text}", parse_mode="HTML",
                           reply_markup=confermation_keyboard)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=New_post.Confirm)
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Вы отменили публикацию")


@dp.message_handler(state=New_post.Confirm)
async def _post(message: types.Message):
    await message.answer("Выберите опубликовать или отклонить")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=admins)
async def admin_post(call: types.CallbackQuery):
    await call.answer("Вы одобрили публикацию", show_alert=True)
    target_channel = chanels[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)
    await bot.send_message(chat_id=id, text="Ваш пост был принят")


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=admins)
async def admin_cancel(call: types.CallbackQuery):
    await call.answer("Вы отклонили пост", show_alert=True)
    await call.message.edit_reply_markup()
    await bot.send_message(chat_id=id, text="Ваш пост был отколнен")
