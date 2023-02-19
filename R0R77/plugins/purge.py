from telethon import events, Button
from R0R77 import R0R77
from R0R77.status import *
import time

PR_HELP = """
**ئەمە لیستی فەرمانەکانی پاککردنەوەیه📋**

/cleaning
ریپله ی نامه یه ک بکه بۆ سرێنه وه ی نامه کانی خواره وه🗑️

/delet
ریپله ی نامەیەک بکه بۆ سڕینەوەی🗑️

"""

@R0R77.on(events.NewMessage(pattern=r"^[?!/]cleaning"))
@is_admin
async def purge_messages(event, perm):
    if not perm.delete_messages:
         await event.reply("سەرەتا پێویستت بە مۆڵەتی سڕینەوەیە❗")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "‼️پێویستە لە خوارەوە ریپله ی ئەو نامەیە بکه ی کە دەتەوێت بیسڕیتەوە")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"پاککراوەتەوە لە✅ {time_:0.2f} دوو سێ جرکه چاوه ریی که❤️"
    await event.respond(text, parse_mode='markdown')



@R0R77.on(events.NewMessage(pattern="^[!?/]delet$"))
@is_admin
async def delete_messages(event, perm):
    if not perm.delete_messages:
       await event.reply("- سەرەتا پێویستت بە مۆڵەتی سڕینەوەیە❗")
       return
    msg = await event.get_reply_message()
    if not msg:
      await event.reply("پێویستە لە خوارەوە ریپله ی ئەو نامەیە بکه ی کە دەتەوێت بیسڕیتەوە‼️")
      return

    await msg.delete()
    await event.delete()

@R0R77.on(events.callbackquery.CallbackQuery(data="پاککردنەوە"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("گه رانه وه🔙", data="help")]])
