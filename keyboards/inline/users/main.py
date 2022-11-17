from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, ReplyKeyboardMarkup, \
    KeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BadRequest
from aiogram.types.web_app_info import WebAppInfo

from config import CONFIG
from loader import bot

MainPage_CB = CallbackData("MainPage", "target", "id", "editId")


class Main:
    @staticmethod
    async def start_ikb() -> InlineKeyboardMarkup:
        """
        Самая стартовая клавиатура
        :return:
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Открыть сайт",
                                         web_app=WebAppInfo(url=CONFIG.WEBAPPURL)
                                         )
                ]
            ]
        )

    @staticmethod
    async def open_site_kb() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            row_width=2,
            resize_keyboard=True,
            one_time_keyboard=True,
            keyboard=[
                [
                    KeyboardButton(text='Сайт',
                                   web_app=WebAppInfo(url=CONFIG.WEBAPPURL + "/form"),
                                   callback_data=MainPage_CB.new("Site", 0, 0))
                ]
            ]
        )

    @staticmethod
    async def process_profile(callback: CallbackQuery = None, message: Message = None,
                              state: FSMContext = None) -> None:
        if callback:
            if callback.data.startswith('MainPage'):
                data = MainPage_CB.parse(callback_data=callback.data)

                if data.get("target") == "Site":
                    print('is work')

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
                if await state.get_state() == "MainState:SiteState":
                    pass

