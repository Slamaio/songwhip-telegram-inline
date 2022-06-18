import hashlib

from aiogram import types
import requests


async def inline_convert(inline_query: types.InlineQuery):
    
    text = inline_query.query
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    request = requests.post("https://songwhip.com/",
                            data=text, headers=headers).json()
    
    input_content = types.InputTextMessageContent(request["url"])
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    
    item = types.InlineQueryResultArticle(
        id=result_id,
        title=request["name"],
        description=f'by {", ".join([artist["name"] for artist in request["artists"]])}',
        input_message_content=input_content,
        thumb_url=request["image"],
        url=request["url"],
    )

    await inline_query.answer(results=[item], cache_time=1)
