import os

from telethon import Button, events

from SARKAUT import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@SARKAUT"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@SARKAUT.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/SARKAUT")]]
    await SARKAUT.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
