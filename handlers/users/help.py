from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp,db


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer("Bu Bot Boyicha Savollar Bo'lsa @Just_Devoloper")