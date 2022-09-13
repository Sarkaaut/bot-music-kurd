import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/38a7ca6bf7e732b3095da.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@R0R77"
)

CAPTION = f"**خێرایی ئێنته رنیتی بۆته که:** {ms}\n سه روک:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("خاوه ن بۆت", "https://t.me/SARKAUT")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
