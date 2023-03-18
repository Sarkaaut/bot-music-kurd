from telethon import events, Button, types
from R0R77 import R0R77
from R0R77.status import *
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest


MISC_HELP = """
**چەند فەرمانێکی سادە بۆ دۆزینەوە و دەست🚸**

/id
ریپله ی به کارهێنه ر بکه بۆ ئه وه ی ئایدیه که ی بزانیت 🆔

/info
بۆ پیشاندانی زانیاری بەکارهێنەر بە ریپله ی💳
"""

@R0R77.on(events.NewMessage(pattern="^[!?/]id"))
async def id(event):

    if event.is_private:
       await event.reply(f"ئایدی به رێزت`{event.sender_id}`.")
       return

    ID = """
**ئایدی گرووپ 🔰:** `{}`
**ئایدی به کارهێنه ر 🆔:** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.chat_id, event.sender_id))
      return

    await event.reply(f"به کارهێنه ر {msg.sender.first_name} /n ئایدی `{msg.sender_id}`.")
 
@R0R77.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):

    sed = await R0R77(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await R0R77(GetFullUserRequest(event.sender_id))
    text = "**📜⏐↫ زانیاری بەکارهێنەر**\n\n"
    text += "**🗒️⏐↫ ناوی یه که م** {}\n"
    text += "**🪪⏐↫ ناوی دووم** {}\n"
    text += "**🆔⏐↫ ئایدی** `{}`\n"
    text += "**🎫⏐↫ ناسنامه** @{}\n"
    text += "**📸⏐↫ ژماره ی وێنه** `{}`\n"
    text += "**💎⏐↫ بایو** `{}`\n"
    text += "**لینکی ئەکاونتەکەی :** [کلیک ئێره بکه](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await R0R77.send_message(event.chat_id, text.format(hn.user.first_name, hn.user.last_name, event.sender_id, event.sender.username, sed.count, hn.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    ha = await R0R77.get_entity(input_str)
    hu = await R0R77(GetFullUserRequest(id=input_str))
    sedd = await R0R77(P(user_id=input_str, offset=42, max_id=0, limit=80))

    textn = "**📜⏐↫ زانیاری بەکارهێنەر**\n\n"
    textn += "**🗒️⏐↫ ناوی یه که م** {}\n"
    textn += "**🪪⏐↫ ناوی دووم** {}\n"
    textn += "**🆔⏐↫ ئایدی** `{}`\n"
    textn += "**🎫⏐↫ ناسنامه** @{}\n"
    textn += "**📸⏐↫ ژماره ی وێنه** `{}`\n"
    textn += "**💎⏐↫ بایو** `{}`\n"
    textn += "** لینکی ئەکاونتەکەی:** [کلیک ئێره بکه](tg://user?id={})\n"

    await event.reply(textn.format(ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id))
   

@R0R77.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("🔙گه رانه وه", data="help")]])
