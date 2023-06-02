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

import asyncio

import speedtest
from pyrogram import filters

from FallenMusic import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ ڕاکردنی تاقیکردنەوەی خێرایی دابەزاندن...**")
        test.download()
        m = m.edit("**⇆ تاقیکردنەوەی خێرایی دابەزاندن ئەنجام بدە...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ ئەنجامی تاقیکردنەوەی خێرایی هاوبەش بکە...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) | filters.command([" تاقیکردنەوە","xiray","خيراي","سە ریعی","خێرایی"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("**⎊ تاقیکردنەوەی خێرایی ئەنجام بدە...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""🎶 **ئەنجامی تاقیکردنەوەی خێرایی بۆت میوزیک ** 
    
<u>**🚹 کلایەنت :**</u>
**🛜 دابینکه‌ری خزمه‌تگوزاری ئینته‌رنێت :** {result['client']['isp']}
**🇺🇸 وڵات :** {result['client']['country']}
  
<u>**📶 سێرڤەر :**</u>
**🏷️ ناوەکە :** {result['server']['name']}
**🌐 وڵات :** {result['server']['country']}, {result['server']['cc']}
**⚙️ رام :** {result['server']['sponsor']}
**📬 کاتی وەڵامدانەوە :** {result['server']['latency']}  
**📊 پینگ :** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
