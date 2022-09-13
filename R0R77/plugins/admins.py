import R0R77
from telethon import events, Button
from R0R77 import R0R77
from R0R77.status import *
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@R0R77.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("گه رانه وه 🔙", data="help")]])

@R0R77.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("گه رانه وه 🔙", data="help")]])

@R0R77.on(events.NewMessage(pattern="^[!?/]auth ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("ئەم فرمانە تەنها لە گروپدا بەکاردێت ❗")
       return

    if not perm.add_admins:
        await event.reply("بۆ ئەنجامدانی ئەم کارە دەبێت مۆڵەتی بلۆککردنت هەبێت 🛡️")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("ده بێت ریپله ی به کارهێنه ر بکه ی بۆ ئه وه ی به رزبکریته وه بۆ ئادمین 👥")
        return
    sed = await R0R77(GetFullUserRequest(id=user.sender_id or input_str))
    await R0R77(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=False,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank="Admin"))

    if not input_str:
        await event.reply(f"- بە سەرکەوتوویی به رزکرایه وه ✅[{sed.user.first_name}](tg://user?id={user.sender_id}) في {event.chat.title}!")
        return

    await event.reply(f"🖇️ بەکارهێنەرەکە بە سەرکەوتوویی به رزکراوه ته وه {input_str} in {event.chat.title}")
 
@R0R77.on(events.NewMessage(pattern="^[!?/]unauth ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("ئەم فرمانە تەنها لە گروپدا بەکاردێت ❗")
       return
    if not perm.add_admins:
        await event.reply("بۆ ئەنجامدانی ئەم کارە دەبێت مۆڵەتی بلۆککردنت هەبێت 🛡️")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("پێویستە ریپله ی  ئەو بەکارهێنەرە بکه یت کە دەتەوێت دایبەزێنیت 🚸")
        return
    sed = await R0R77(GetFullUserRequest(id=user.sender_id or input_str))
    await R0R77(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None), rank="Not Admin"))

    if not input_str:
        await event.reply(f"- بە سەرکەوتوویی دابەزێنراوە ✅[{sed.user.first_name}](tg://user?id={user.sender_id}) له {event.chat.title}!")
        return

    await event.reply(f"- بە سەرکەوتوویی دابەزێنراوە ✅ {input_str} in {event.chat.title}")
 

@R0R77.on(events.NewMessage(pattern="^[!?/]الرابط"))
async def invitelink(event):

    if event.is_private:
       await event.reply("ئەم فرمانە تەنها لە گروپدا بەکاردێت ❗")
       return
    link = await R0R77(ExportChatInviteRequest(event.chat_id))
    await event.reply(f"گروپەکە {event.chat.title}لینک: [لێرەدا فشار بدە]({link.link})", link_preview=False)

ADMIN_TEXT = """
**هەموو فەرمانەکانی ئەدمین پێویستە ئەدمین بن 🔰**

/auth
بۆ بەرزکردنەوەی ئەدمینی بەکارهێنەر 🚹

/unauth
بۆ دابەزاندنی بەکارهێنەر لە پلەی سەرپەرشتیکردن بە ریپله بۆی 🚸

/link
بۆ هێنانی لینکی گروپەکە تەنها فرمانەکە بنێرە ✅

/pause
بۆ کۆتایی هێنان بە کارەکە لە پەیوەندییەکەدا 📴

/skip
بۆ ئەوەی پەخشکردنی ئێستا بەجێبهێڵیت 🔃

/stop
بۆ وەستاندنی پەخشکردن ⚠️

/resume
بۆ دەستپێکردنەوەی پەخشکردن لە پەیوەندییەکدا ♻️

/shuffle
ناچار بە جێهێشتنی گروپەکە ‼️

/seek
پلەی لیستەکانی ئێستا لە کۆمەڵەکەدا پیشان دەدات 🎵
"""

PLAY_TEXT = """
**فه رمانەکان بۆ بەکارهێنەرانی ئاسایی**

/play
بۆ پەخشکردنی کلیپی دەنگی لە پەیوەندییەکەدا، فرمانەکە بنووسە ✍️

"""
