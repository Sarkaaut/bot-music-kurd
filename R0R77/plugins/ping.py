import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/f8334ad5e6b6203c51397.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@R0R77"
)

CAPTION = f"**خێرای بۆت:** {ms}\n سه روڪ:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("خاوه ت بۆت", "https://t.me/SARKAUT")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
