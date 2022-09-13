import SARKAUT
from telethon import events, Button
from SARKAUT import SARKAUT
from SARKAUT.status import *
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@SARKAUT.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« گه رانه وه", data="help")]])

@SARKAUT.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« گه رانه وه", data="help")]])

@SARKAUT.on(events.NewMessage(pattern="^[!?/]unauth ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("ئەم فرمانە تەنها لە گروپدا بەکاردێت")
       return

    if not perm.add_admins:
        await event.reply("بۆ ئەنجامدانی ئەم کارە دەبێت مۆڵەتی بلۆکردنت هەبێت")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("پێویستە وەڵامی بەکارهێنەر بدەیتەوە بۆ ئەوەی باری بکات")
        return
    sed = await SARKAUT(GetFullUserRequest(id=user.sender_id or input_str))
    await SARKAUT(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=False,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank="Admin"))

    if not input_str:
        await event.reply(f"- بە سەرکەوتوویی بارکرا [{sed.user.first_name}](tg://user?id={user.sender_id}) لە {event.chat.title}!")
        return

    await event.reply(f"بەکارهێنەرەکە بە سەرکەوتوویی بارکراوە {input_str} in {event.chat.title}")
 
@SARKAUT.on(events.NewMessage(pattern="^[!?/]unauth ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("ئەم فرمانە تەنها لە گروپدا بەکاردێت")
       return
    if not perm.add_admins:
        await event.reply("بۆ ئەنجامدانی ئەم کارە دەبێت مۆڵەتی بلۆککردنت هەبێت")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("پێویستە وەڵامی ئەو بەکارهێنەرە بدەیتەوە کە دەتەوێت دایبەزێنیت")
        return
    sed = await SARKAUT(GetFullUserRequest(id=user.sender_id or input_str))
    await SARKAUT(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None), rank="Not Admin"))

    if not input_str:
        await event.reply(f"- بە سەرکەوتوویی دابەزێنراوە[{sed.user.first_name}](tg://user?id={user.sender_id}) له {event.chat.title}!")
        return

    await event.reply(f"- بە سەرکەوتوویی دابەزێنراوە {input_str} in {event.chat.title}")
 

@SARKAUT.on(events.NewMessage(pattern="^[!?/]link"))
async def invitelink(event):

    if event.is_private:
       await event.reply("ئەم فرمانە تەنها لە گروپدا بەکاردێت !")
       return
    link = await SARKAUT(ExportChatInviteRequest(event.chat_id))
    await event.reply(f"گروپەکە {event.chat.title}لینک: [کرتەی ئێرە بکە]({link.link})", link_preview=False)

ADMIN_TEXT = """
**✘ هەموو فەرمانەکانی ئەدمین پێویستە ئەدمین بن**

/auth
( بۆ بەرزکردنەوەی ئەدمینی بەکارهێنەر )

/unauth
( بۆ دابەزاندنی بەکارهێنەر لە پلەی سەرپەرشتیکردن بە وەڵامدانەوەی بۆی )

/link
بۆ هێنانی لینکی گروپەکە تەنها فرمانەکە بنێرە

/pause
بۆ کۆتایی هێنان بە کارەکە لە پەیوەندییەکەدا

/skip
بۆ ئەوەی پەخشکردنی ئێستا بەجێبهێڵیت

/stop
بۆ وەستاندنی پەخشکردن

/resume
بۆ دەستپێکردنەوەی پەخشکردن لە پەیوەندییەکدا

/shuffle
ناچار بە جێهێشتنی گروپەکە

/seek
بۆ دەستپێکردنەوەی پەخشکردن ائیستا
"""

PLAY_TEXT = """
**✘ فەرمانە ئاساییەکانی بەکارهێنەر**

/play
بۆ پەخشکردنی کلیپی دەنگی لە پەیوەندییەکەدا، فرمانەکە بنووسە

"""
