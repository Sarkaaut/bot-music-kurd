from typing import *
import random
from typing import Dict, List, Union

from ROR77 import *
from telethon import *
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotParticipantError
)

def AssistantAdd(mystic):
    async def wrapper(event):
        try:
            permissions = await event.client(GetParticipantRequest(int(event.chat_id), int(ASSISTANT_ID)))
        except UserNotParticipantError:
            if event.is_group:
                try:
                    link = await event.client(ExportChatInviteRequest(event.chat_id))
                    invitelinkk = link.link
                    invitelink = invitelinkk.replace(
                        "https://t.me/+", ""
                    )
                    await client(ImportChatInviteRequest(invitelink))
                    await event.reply(
                        f"Joined Successfully",
                    )
                except UserAlreadyParticipantError:
                    pass
                except Exception as e:
                    await event.reply(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
        return await mystic(event)

    return wrapper
