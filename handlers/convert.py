import requests
from aiogram import types

from config import HEADERS


async def convert(message: types.Message):
    """Generate a songwhip link from a regular music link"""
    
    await message.answer_chat_action("typing")
    
    url_entity = next((entity for entity in message.entities if entity.type == "url"), None)
    
    if not url_entity:
        await message.reply("Please send a link")
        return
    
    url = message.text[url_entity.offset : url_entity.offset+url_entity.length]
    request = requests.post("https://songwhip.com/", data=url, headers=HEADERS)
    
    if not request.ok:
        await message.reply("*There's a problem with that URL\.*\n"
                            + "Either we don't support this music service or the URL is malformed\. "
                            + "Try one from a different music service\.",
                            parse_mode="Markdown")
        return
    
    data: dict = request.json()
    
    reply_text = f'*{data["name"]} ({data["type"]})*\n' \
                 + (f'by {", ".join([artist["name"] for artist in data["artists"]])}\n\n'
                    if "artists" in data.keys()
                    else "\n\n") \
                 + data["url"]
                 
    await message.reply(reply_text, parse_mode="Markdown")
