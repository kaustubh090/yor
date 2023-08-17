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
            text = f"<b>Premium Benefits & Perks</b>
Direct Channel Links, No Ad Links
Special Access In Events

<b>Pricing Rates</b>
1 Day - INR 20
7 Days - INR 40
1 Month - INR 100
3 Months - INR 200
6 Months - INR 400
9 Months - INR 600
12 Months - INR 800    

<b>Want To Buy?</b>
Pay Using UPI killuaog@upi
Send Screenshot to @killua_og and in this bot (To Process Auto Verification)

<b>We Have Limited Seats For Premium Users</b>",
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
