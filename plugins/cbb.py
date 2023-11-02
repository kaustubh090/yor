#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Premium Benefits & Perks</b>\n<i>Direct Channel Links, No Ad Links</i>\n<i>SpecialAccess In Events</i>\n\n<b>Pricing Rates</b>\n<code>1</code> Day - <code>INR 20</code>\n<code>7</code> Days - <code>INR 40</code>\n<code>1</code> Month - <code>INR 100</code>\n<code>3</code> Months - <code>INR 200</code>\n<code>6</code> Months - <code>INR 400</code>\n<code>9</code> Months - <code>INR 600</code>\n<code>12</code> Months - <code>INR 800</code>\n\n<b>Want To Buy?💓</b>\n<b>»</b> Pay Using UPI <code>vilaskachole68414-1@okicici</code>\n<b>»</b> Send Screenshot to @killua_og and in this bot <i>(To Process Auto Verification)</i>\n\n○ <b>We Have Limited Seats For Premium Users</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
