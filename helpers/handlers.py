from pyrogram.raw.base import Update
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.stream import StreamAudioEnded
from config import client, call_py
from helpers.queues import QUEUE, clear_queue, get_queue, pop_an_item


async def skip_current_song(chat_id):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            return 1
        else:
            songname = chat_queue[1][0]
            url = chat_queue[1][1]
            link = chat_queue[1][2]
            type = chat_queue[1][3]
            Q = chat_queue[1][4]
            if type == "Audio":
                await call_py.change_stream(
                    chat_id,
                    AudioPiped(
                        url,
                        HighQualityAudio(),
                    ),
                )
            pop_an_item(chat_id)
            return [songname, link, type]
    else:
        return 0


async def skip_item(chat_id, h):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        try:
            x = int(h)
            songname = chat_queue[x][0]
            chat_queue.pop(x)
            return songname
        except Exception as e:
            print(e)
            return 0
    else:
        return 0


@call_py.on_stream_end()
async def on_end_handler(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        chat_id = update.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op == 0:
            await client.send_message(
                chat_id, "__ᴇᴍᴘᴛʏ ǫᴜᴇᴜᴇ, ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ__"
            )
        else:
            await client.send_message(
                chat_id,
                f"**🎵 ɴᴏᴡ ᴘʟᴀʏɪɴɢ** \n[{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
