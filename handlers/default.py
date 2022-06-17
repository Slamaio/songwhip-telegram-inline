from aiogram import types


async def start(message: types.Message):
    await message.reply('I am working\nTODO: Starting message')
    
    
async def help(message: types.Message):
    await message.reply('TODO: Help info')
    