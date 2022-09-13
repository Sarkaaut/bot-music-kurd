from telethon import events, Button
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from R0R77 import R0R77
from R0R77.status import *


CLEANER_HELP = """
**ئەمانە ئەو فرمانانەن بۆ بینین و سڕینەوەی ئەکاونتە سڕاوەکان**
!سراوه کان
بۆ بینینی ئەکاونتە سڕاوەکان لە چاتدا

!پاکردنه وه ی سراوه کان
سرینه وه و باند کڕدنی ئاکاونته سراوه کان له گرووپ

"""


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@R0R77.on(events.NewMessage(pattern="^[!?/]سراوه کان ?(.*)"))
@is_admin
async def clean(event, perm):
    if not perm.ban_users:
      await event.reply("- تۆ دەسەڵاتی پێویستت نییە")
      return
    input_str = event.pattern_match.group(1)
    stats = "گروپەکە پاک و خاوێنە"
    deleted = 0

    if "clean" not in input_str:
      zombies = await event.respond("بەدوای ئەو ئەکاونتانەدا دەگەڕێت کە سڕاونەتەوە یان دوایین جار بینراون کە کۆنن")
      async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                deleted += 1
      if deleted > 0:
            stats = f".دۆزرایەوە **{deleted}** سڕاوه کان لێره\
            \nبۆ دەرکردنیان بنێرن `/سراوه کان پاکه`"
      await zombies.edit(stats)
      return

    cleaning_zombies = await event.respond("- ئەکاونتە سڕاوەکان دەردەکرێن، خولەکێک چاوەڕێ بکە")
    del_u = 0
    del_a = 0

    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await cleaning_zombies.edit("- ببورن لێرە مۆڵەتم نییە بۆ بلۆکردن")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        stats = f"پاکراوەتەوە`{del_u}` لە ئەکاونتە سڕاوەکانەوە"

    if del_a > 0:
        stats = f"پاکراوەتەوە`{del_u}` لە ئەکاونتە سڕاوەکانەوە \
        \n`{del_a}` ئەکاونتە سڕاوەکانی ئەدمین دەرنەکراون"

    await cleaning_zombies.edit(stats)

@R0R77.on(events.callbackquery.CallbackQuery(data="zombies"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline("گه رانه وه", data="help")]])
