#ð±ð°SL BOTs <https://t.me/slhitbotofficial>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hello there, I'm [Song Downloader Bot ðµ](https://telegra.ph/file/ce89cf2cc05c956c600d0.jpg)
I'm a Powerful Songs Downloader bot Made by [ððððð° ððð²ðð¬ðð¤ðð«ð](t.me/darkridersslk)

ð Just send me the song name you want to download.ð
    
eg: " /song Despacito "
      

"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥°ððð ð¦ð ð­ð¨ ð²ð¨ð®ð« ðð«ð¨ð®ð© ðââï¸", url=f"https://t.me/sdSLBOTSbot?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "ð¿ðð«ðð¡ð¤ð¥ðð§ ð±ð° ð ", url=f"https://t.me/darkridersslk"), 
                    InlineKeyboardButton(
                        "ð¬ Support", url=f"https://t.me/slhitofficialbot")
                ],[
                    InlineKeyboardButton(
                        "ð±ð°SL BOTs", url=f"https://t.me/slhitbotofficial")
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("â sdSLBOTSbot is online.")
idle()
