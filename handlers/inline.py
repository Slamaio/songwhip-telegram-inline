import hashlib
from typing import List

import requests
from aiogram import types

from config import HEADERS


async def convert_link(url: str) -> types.InlineQueryResultArticle:
    """Convert a regular link to a songwhip link and return the inline responce item

    Args:
        url (str): URL to convert

    Returns:
        types.InlineQueryResultArticle: Inline responce item to be shown to the user
    """
    
    request = requests.post("https://songwhip.com/", data=url, headers=HEADERS)
    
    result_id = hashlib.md5(url.encode()).hexdigest()
    
    if not request.ok:
        return types.InlineQueryResultArticle(
            id=result_id,
            title="There's a problem with that URL",
            description="Either we don't support this music service or the URL is malformed. Try one from a different music service.",
            input_message_content=types.InputTextMessageContent("*There's a problem with that URL.*\n"
                                                                + "Either we don't support this music service or the URL is malformed. "
                                                                + "Try one from a different music service.",
                                                                parse_mode="Markdown"),
        )
        
    data: dict = request.json()
    
    result_title = f'{data["name"]} ({data["type"]})'
    input_content = types.InputTextMessageContent(data["url"])
    result_url: str = data["url"]
    
    # Sometimes "artists" and/or "image" keys aren't present in the api response
    # so we have to check for them
    if "artists" in data.keys():
        result_description = f'by {", ".join([artist["name"] for artist in data["artists"]])}'
    else:
        result_description = None
    result_thumb: str = data["image"] if "image" in data.keys() else None
    
    return types.InlineQueryResultArticle(
        id=result_id,
        title=result_title,
        input_message_content=input_content,
        url=result_url,
        description=result_description,
        thumb_url=result_thumb,
    )


async def search(query: str) -> List[types.InlineQueryResultArticle]:
    """Search for tracks/albums/artists based on the search querry

    Args:
        query (str): Search querry

    Returns:
        List[types.InlineQueryResultArticle]: List of inline responce items to be shown to the user
    """
    
    # TODO: Country select and results limit
    request = requests.get(f"https://songwhip.com/api/songwhip/search?q={query}&country=UA&limit=3")
    
    data = request.json()["data"]
    
    results = []
    for category in ['tracks', 'albums', 'artists']:
        for item in data[category]:
            result_id = hashlib.md5(item["sourceUrl"].encode()).hexdigest()
            result_title = f'{item["name"]} ({item["type"]})'
            input_content = types.InputTextMessageContent(f'https://songwhip.com/{item["sourceUrl"]}')
            result_url = f'https://songwhip.com/{item["sourceUrl"]}'
            
            # Sometimes "artists" and/or "image" keys aren't present in the api response
            # so we have to make checks to avoid errors
            if "artists" in item.keys():
                result_description = f'by {", ".join([artist["name"] for artist in item["artists"]])}'
            else:
                result_description = None
            result_thumb: str = item["image"] if "image" in item.keys() else None
            
            item = types.InlineQueryResultArticle(
                id=result_id,
                title=result_title,
                input_message_content=input_content,
                url=result_url,
                description=result_description,
                thumb_url=result_thumb,
            )
            
            results.append(item)
    
    return results


async def inline_handler(inline_query: types.InlineQuery):
    """Inline handler"""
    
    text = inline_query.query

    if text.startswith("https://"):
        items = [await convert_link(text)]
    else:
        items = await search(text)

    await inline_query.answer(results=items)
