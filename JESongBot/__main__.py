#🇱🇰SL BOTs <https://t.me/slhitbotofficial>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hello there, I'm [Song Downloader Bot 🎵](https://telegra.ph/file/ce89cf2cc05c956c600d0.jpg)
I'm a Powerful Songs Downloader bot Made by [𝐒𝐚𝐝𝐞𝐰 𝐉𝐚𝐲𝐚𝐬𝐞𝐤𝐚𝐫𝐚](t.me/darkridersslk)

😉 Just send me the song name you want to download.😋
    
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
                        "🥰𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 🙋‍♀️", url=f"https://t.me/sdSLBOTSbot?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 🇱🇰 🛠", url=f"https://t.me/darkridersslk"), 
                    InlineKeyboardButton(
                        "💬 Support", url=f"https://t.me/slhitofficialbot")
                ],[
                    InlineKeyboardButton(
                        "🇱🇰SL BOTs", url=f"https://t.me/slhitbotofficial")
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ sdSLBOTSbot is online.")
idle()
