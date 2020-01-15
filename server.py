import os
import re

import discord
import lxml.html as lh
import requests

polr_url = os.getenv("POLR_URL", None)
polr_api = os.getenv("POLR_KEY", None)


class AMPBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            content = message.content
            if "http://" in content.lower() or "https://" in content.lower():
                urls = re.findall('[localhost|http|https|ftp|file]+://[\w\S(\.|:|/)]+', content)
                test = False
                test_url = ""
                for url in urls:
                    if test:
                        pass
                    else:
                        data = requests.get(url)
                        if data.status_code == 200:
                            doc = lh.fromstring(data.text)
                            for item in doc.iter('html'):
                                if True in ["amp" in str(x).lower() for x in item.keys()]:
                                    test = True
                                    test_url = url
                            for item in doc.iter('style'):
                                if True in ["amp" in str(x).lower() for x in item.keys()]:
                                    test = True
                                    test_url = url
                if test:
                    if os.getenv("DELETE", "false").lower() == "true":
                        await message.delete()

                    tokens = {}
                    msg = os.getenv("MESSAGE", "{name} sent an amp link. Please use real links dipshit.\n||<{url}>||")
                    if "{name}" in msg:
                        tokens['name'] = message.author.mention
                    if "{url}" in msg:
                        if polr_url is not None:
                            params = dict(key=polr_api, url=test_url, is_secret="true")
                            req = requests.get(polr_url.rstrip("/") + "/api/v2/action/shorten", params=params)
                            if req.status_code == 200:
                                test_url = req.text
                        tokens['url'] = test_url

                    msg = msg.format(**tokens)
                    await message.channel.send(msg)


client = AMPBot()
client.run(str(os.getenv("TOKEN")))
