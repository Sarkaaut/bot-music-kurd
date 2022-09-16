import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/f8334ad5e6b6203c51397.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@SARKAUT"
)

CAPTION = f"**خێرای بۆت:** {ms}\n سه روڪ:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("که ناڵی بۆت", "https://t.me/Trpay_dllm")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
