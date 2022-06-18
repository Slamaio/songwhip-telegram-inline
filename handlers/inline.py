from aiogram import types


async def inline_convert(inline_query: types.InlineQuery):
    await inline_query.answer(inline_query.id, results=["Test inline result"], cache_time=1)