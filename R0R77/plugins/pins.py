import os

from telethon import Button, events, types
from R0R77.status import *
from R0R77 import *


PINS_TEXT = """
**🔰فەرمانەکانی دامەزراندن و لابردنی نامەکان لە گروپەکەدا**

/Installations
🖇️ریپله ی ئەو نامەیە بکه کە دەتەوێت دایبمەزرێنیت

/uninstall
📨ریپله ی ئەو نامانەی کە دەتەوێت پینیان لێ بکەیتەوە

/Uninstall for all
📭بۆ لابردنی هەموو نامە پین کراوه کانی ناو گروپەکە

/Pinned messages
📮بۆ پیشاندانی نامە پین کراوەکان لە گروپەکەدا

"""

@R0R77.on(events.NewMessage(pattern="^[?!/]Pinned messages"))
async def get_pinned(event):
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await R0R77.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
    tem = f"نامەی پینکراو لە چاتدا{event.chat.title} ئه و <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)

@R0R77.on(events.NewMessage(pattern="^[!?/]Installations ?(.*)"))
@is_admin
async def pin(event, perm):
    if not perm.pin_messages:
       await event.reply("پێویستە سەرەتا مۆڵەتی دامەزراندنت هەبێت🔰")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("پێویستە سەرەتا ریپله ی نامەکە بکه یت🖇️")
       return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
       await R0R77.pin_message(event.chat_id, msg, notify=True)
       return
    await R0R77.pin_message(event.chat_id, msg)   

@R0R77.on(events.NewMessage(pattern="^[!?/]uninstall ?(.*)"))
@is_admin
async def unpin(event, perm):
    if not perm.pin_messages:
       await event.reply("پێویستە سەرەتا مۆڵەتی دامەزراندنت هەبێت🔰")
       return
    chat_id = (str(event.chat_id)).replace("-100", "")
    ok = await R0R77.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await R0R77.unpin_message(event.chat_id, ok)
    await event.reply(f"دامەزراندنەکە بە سەرکەوتوویی هەڵوەشایەوە✅   [بۆ ئەم پەیامە](t.me/{event.chat.username}/{ok.id}).", link_preview=False)


@R0R77.on(events.NewMessage(pattern="^[!?/]Uninstall for all$"))
async def unpinall(event, perm):
    if not perm.pin_messages:
       await event.reply("پێویستە سەرەتا مۆڵەتی دامەزراندنت هەبێت🔰")
       return
    UNPINALL = """
ئایا دڵنیای کە نامەکان هەڵدەگریت؟
"""

    await R0R77.send_message(event.chat_id, UNPINALL, buttons=[
    [Button.inline("دووپات کردنەوە", data="unpin")], 
    [Button.inline("هەڵوەشاندنەوە", data="cancel")]])

@R0R77.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await R0R77.unpin_message(event.chat_id)
        await event.edit("هەموو نامەکان بە سەرکەوتوویی لابراون✅")
        return 

    await event.answer("پێویستە سەرەتا خاوەنی گروپەکە بیت🔱")

@R0R77.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):

    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("پرۆسەی لابردنی دامەزراندن بۆ هەموو نامەکان هەڵوەشاوەتەوە‼️")
        return 

    await event.answer("پێویستە سەرەتا خاوەنی گروپەکە بیت🔱")


@R0R77.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("گه رانه وه🔙", data="help")]])
