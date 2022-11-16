from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, ReplyKeyboardMarkup, \
    KeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BadRequest
from aiogram.types.web_app_info import WebAppInfo

from loader import bot

MainPage_CB = CallbackData("MainPage", "target", "id", "editId")


class Main:
    @staticmethod
    async def start_kb() -> InlineKeyboardMarkup:
        """
        Самая стартовая клавиатура
        :return:
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Открыть сайт",
                                         web_app=WebAppInfo(url="https://github.com/aiogram/aiogram/issues/891")
                                         )
                ]
            ]
        )

    @staticmethod
    async def process_profile(callback: CallbackQuery = None, message: Message = None,
                              state: FSMContext = None) -> None:
        if callback:
            if callback.data.startswith('MainPage'):
                pass
        if message:
            await message.delete()

            try:
                await bot.delete_message(
                    chat_id=message.from_user.id,
                    message_id=message.message_id - 1
                )
            except BadRequest:
                pass

            if state:
                pass

