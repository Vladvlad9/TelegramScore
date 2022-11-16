from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.exceptions import BadRequest

from keyboards.inline.users.main import Main, MainPage_CB
from loader import dp, bot
from states.users import MainState


@dp.message_handler(commands=["start"])
async def registration_start(message: types.Message):
    await message.answer(text="Привет!", reply_markup=await Main.start_kb())

# @dp.message_handler(commands="start")
# async def cmd_start(message: types.Message):
#     await message.answer("test",
#                          reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="test",
#                                                                                       web_app=WebAppInfo(url="https://github.com/aiogram/aiogram/issues/891"))))


@dp.callback_query_handler(MainPage_CB.filter())
@dp.callback_query_handler(MainPage_CB.filter(), state=MainState.all_states)
async def process_callback(callback: types.CallbackQuery, state: FSMContext = None):
    await Main.process_profile(callback=callback, state=state)


@dp.message_handler(state=MainState.all_states, content_types=["text", "contact"])
async def process_message(message: types.Message, state: FSMContext = None):
    await Main.process_profile(message=message, state=state)
