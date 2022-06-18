from aiogram import types
import requests


async def convert(message: types.Message):
    url_entity = next((entity for entity in message.entities if entity.type == "url"), None)
    
    if not url_entity:
        message.reply("Please send a link")
        return
    
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    url = message.text[url_entity.offset : url_entity.offset+url_entity.length]
    request = requests.post("https://songwhip.com/", data=url, headers=headers)
    
    if not request.ok:
        await message.reply("Broken link")
        return
    
    await message.reply(request.json()["url"], disable_web_page_preview=False)
