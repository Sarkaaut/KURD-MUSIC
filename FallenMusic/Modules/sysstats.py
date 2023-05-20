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

import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from FallenMusic import BOT_NAME, SUDOERS, app
from FallenMusic.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) | filters.command(["بارودۆخه‌كه‌","ئامارەکان"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"ɢᴇᴛᴛɪɴɢ {BOT_NAME} System Start it Ll Take A While..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "شکستی هێنا لە هێنانی"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
⎊ <u>**{BOT_NAME} ئاماری سیستەم **</u>

**پایتۆن :** {pyver.split()[0]}
**پیرۆگرام :** {pyrover}
**پەیوەندییەکانی بی تی جی :** {pytgver}
**سۆدۆرس :** `{sudoers}`
**یەکەکان :** `{mod}`

**ئایبی :** {ip_address}
**ماک :** {mac_address}
**ناوی هۆست :** {hostname}
**پلاتفۆرم :** {sp}
**چارەسەرکەر :** {processor}
**بنيان :** {architecture}
**وەشانی پلاتفۆرم :** {platform_release}
**وەشانی پلاتفۆرم :** {platform_version}

        <b><u>کۆگا</b><u/>
**بەردەست :** {total[:4]} ɢɪʙ
**بەکارهێنەر :** {used[:4]} ɢɪʙ
**ئازاد :** {free[:4]} ɢɪʙ

**رام :** {ram}
**ناوەکی فیزیکی :** {p_core}
**کۆی گشتی ناوکەکان :** {t_core}
**فرێکوێنسی سی پی یو :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="سڕینەوە",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
