from telethon import events, Button, types
from JE313P import JE313P
from JE313P.status import *

LOCKS_HELP = """
**ئەمانە فەرمانەکانی قفڵکردن و کردنەوەی قفڵن لە چاتدا**

!قوفڵ
بۆ قفڵکردنی شتێکی تایبەت لە چاتەکەدا

!کردنەوە
بۆ کردنەوەی مۆڵەتەکان بۆ شتێکی دیاریکراو

/دەسەڵاتەکان
بۆ پیشاندانی ئەو هێزانەی کە دەتوانیت قفڵی بکەیت

"""

@JE313P.on(events.NewMessage(pattern="^[!?/]قوفڵ ?(.*)"))
@is_admin
async def lock(event, perm):
    if not perm.change_info:
      await event.reply("بۆ بەکارهێنانی ئەم فرمانە پێویستت بە هەندێک ئیمتیازاتی بەڕێوەبەر هەیە")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("تکایە سەرەتا شتێک هەڵبژێرە بۆ ئەوەی قفڵی بکەیت")
       return
    if "پەیامەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_messages=False)
       await event.reply("- نامەکان قفڵ دەکرێن")
    elif "ڕاگەیاندن" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_media=False)
       await event.reply("- میدیا قفڵ کراوە")
    elif "ستیکەرەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_stickers=False)
       await event.reply("- ستیکەرەکان قفڵ کراون.")
    elif "گیڤه کان"in input_str:
       await JE313P.edit_permissions(event.chat_id, send_gifs=False)
       await event.reply("- گیڤه کان قفڵ کراوە")
    elif "ڕێڕەوکردن" in input_str:
       await JE313P.edit_permissions(event.chat_id, forwards=False)
       await event.reply("- ڕێڕەوکردن قفڵ کراوە")
    elif "یارییەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_games=False)
       await event.reply("- یارییەکان قفڵ دەکرێن")
    elif "لەسەر هێڵ" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_inline=False)
       await event.reply("- ئۆنلاین داخراوە")
    elif "ده‌نگدان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_polls=False)
       await event.reply("- دەنگدان داخراوە")
    elif "بەستەرەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, embed_link_previews=False)
       await event.reply("- لینکەکان قفڵ کراون")
    elif "هه موان" in input_str:
       await JE313P.edit_permissions(event.chat_id,
          send_messages=False, 
          send_media=False,
          send_stickers=False,
          send_gifs=False,
          send_games=False,
          send_inline=False,
          send_polls=False,
          embed_link_previews=False)
       await event.reply("- هەموویان قفڵ کراون")


@JE313P.on(events.NewMessage(pattern="^[!?/]!کردنەوە ?(.*)"))
@is_admin
async def unlock(event, perm):
    if not perm.change_info:
      await event.reply("بۆ بەکارهێنانی ئەمە پێویستت بە هەندێک ئیمتیازاتی بەڕێوەبەر هەیە")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("تکایە سەرەتا شتێک هەڵبژێرە بۆ ئەوەی قفڵی بکەیتەوە")
       return
    if "پەیامەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_messages=True)
       await event.reply("نووسین کراوەتەوە")
    elif "ڕاگەیاندن" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_media=True)
       await event.reply("میدیا کرایەوە")
    elif "ستیکەرەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_stickers=True)
       await event.reply("ستیکەرەکان کراوەن")
    elif "گیڤه کان"in input_str:
       await JE313P.edit_permissions(event.chat_id, send_gifs=True)
       await event.reply("گیڤه کان کرایەوە")
    elif "ڕێڕەوکردن" in input_str:
       await JE313P.edit_permissions(event.chat_id, forwards=True)
       await event.reply("ڕێڕەو کراوەتەوە")
    elif "یارییەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_games=True)
       await event.reply("یارییەکان کراوەن")
    elif "لەسەر هێڵ" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_inline=True)
       await event.reply("ئۆنلاین کراوەتەوە")
    elif "ده‌نگدان" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_polls=True)
       await event.reply("دەنگدان کراوەتەوە")
    elif "بەستەرەکان" in input_str:
       await JE313P.edit_permissions(event.chat_id, embed_link_previews=True)
       await event.reply("لینکەکان کرانەوە")
    elif "هه موان" in input_str:
       await JE313P.edit_permissions(event.chat_id,
          send_messages=True, 
          send_media=True,
          send_stickers=True,
          send_gifs=True,
          send_games=True,
          =True,
          send_polls=True,
          embed_link_previews=True)
       await event.reply("هەموویان کراوەتەوە")


@JE313P.on(events.NewMessage(pattern="^[!?/]دەسەڵاتەکان"))
async def locktypes(event):
    TEXT = """
**Locks:**

‣ پەیامەکان
‣ ڕاگەیاندن
‣ ستیکەرەکان
‣ گیڤه کان
‣ بەستەرەکان
‣ یارییەکان
‣ لەسەر هێڵ
‣ ڕێڕەوکردن
‣ ده‌نگدان
‣ هه موان
"""
    await event.reply(TEXT)

@JE313P.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("گه رانه وه", data="help")]])
