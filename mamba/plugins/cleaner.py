import os
from pyrogram import Client
from pyrogram.types import Message
from helpers.command import commandpro
from helpers.decorators import errors, sudo_users_only


@Client.on_message(commandpro(["/cl", "!cl", "Cl", "/clean", "!clean"]))
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **𝐂𝐥𝐞𝐚𝐧𝐞𝐝**")
    else:
        await message.reply_text("✅ **𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐂𝐥𝐞𝐚𝐧𝐞𝐝**")
