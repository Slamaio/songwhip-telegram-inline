from aiogram import types


async def start(message: types.Message):
    await message.answer(f"*Hello, {message.from_user.first_name}\!*\n\n"
                        +"I'm an _Unofficial_ Songwhip bot that can operate in the inline mode, so you don't even have to add me to your chat\!\n\n"
                        +"Try me right now: type `@songwhip_inline_bot` followed by a song name/link and I will convert it for you",
                        parse_mode="MarkdownV2")
    
    
async def help(message: types.Message):
    await message.answer("• *Convert a link:*\n    `/convert <link\>`\n"
                        + "• *Convert a link in the inline mode:*\n    `@songwhip_inline_bot <link\>`\n"
                        + "• *Search for a track/album/artist in the inline mode:*\n    `@songwhip_inline_bot <text\>`\n\n"
                        + "/help to show this message",
                        parse_mode="MarkdownV2")
