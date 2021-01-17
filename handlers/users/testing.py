from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram import types

from states import Test

"""Команда тест с использованием state"""


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1.\n\n"
                         "Вы часто занимаетесь бессмысленными делами "
                         "(Бесцельно блуждаете по интернету, просто смотрите телевизор тратите своё время на всякую "
                         "чуж?)")

    await Test.Q1.set()


# await Test.first()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    #
    # await state.update_data(
    #     {
    #         "answer1": answer
    #     }
    # )

    # async with state.proxy() as data:
    #     data["answer1"] = answer

    await message.answer("Вопрос №2. \n\n"
                         "Ваша память ухудшилась и вы помнито то, что было давно, но забываете недавнее состояние")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы!!!")
    await message.answer(f"Ответы 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    # Сброс пользователя из машины состояния
    await state.finish()

    # Сброс пользователя из машины состояния 2
    # await state.reset_state()

    # Сброс пользователя из машины состояния но при этом храним данные которые в нем сохранены data
    # await state.reset_state(with_data=False)
