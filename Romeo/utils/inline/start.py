from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from Romeo import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌸 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🌸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ ʜᴇʟᴘ ✨",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✨ sᴇᴛᴛɪɴɢs ✨", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✨ sᴜᴘᴘᴏʀᴛ ✨", url=f"{config.SUPPORT_GROUP}"),
            InlineKeyboardButton(
                text="✨ ᴜᴘᴅᴀᴛᴇs ✨", url=f"{config.SUPPORT_CHANNEL}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌸 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🌸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✨ ʜᴇʟᴘ ✨", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="✨ sᴜᴘᴘᴏʀᴛ ✨", url=f"{config.SUPPORT_GROUP}"),
            InlineKeyboardButton(
                text="✨ ᴜᴘᴅᴀᴛᴇs ✨", url=f"{config.SUPPORT_CHANNEL}"
            )
        ],
     ]
    return buttons
