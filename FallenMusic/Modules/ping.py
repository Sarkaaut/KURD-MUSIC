# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from FallenMusic import BOT_NAME, StartTime, app
from FallenMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping") | filters.command(["پینج","پینگ"],prefixes= ["/", "!","","#"]))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} ⚡"
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""🛜 پینگ : `{resp}Ms`

<b><u>{BOT_NAME} بارودۆخه‌كه‌ :</u></b>

♻️ **کاتی جێبەجێکردن :** {uptime}
⚙️ **رام :** {mem}
🔰 **یەکەی پرۆسێسکردنی ناوەندی :** {cpu}
📶 **تویک :** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("گروپی بۆت", url=config.SUPPORT_CHAT),
                    InlineKeyboardButton(
                        "کە ناڵی بۆت",
                        url="https://t.me/ChanallBots",
                    ),
                ],
            ]
        ),
    )
