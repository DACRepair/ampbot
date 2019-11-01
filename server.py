import os
import discord
import re
import requests
import lxml.html as lh


class AMPBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        else:
            content = message.content
            if "http://" in content.lower() or "https://" in content.lower():
                urls = re.findall('[localhost|http|https|ftp|file]+://[\w\S(\.|:|/)]+', content)
                test = False
                for url in urls:
                    if test:
                        pass
                    else:
                        data = requests.get(url)
                        if data.status_code == 200:
                            doc = lh.fromstring(data.text)
                            for item in doc.iter('html'):
                                if "amp" in list(item.attrib.keys()):
                                    test = True
                if test:
                    await message.delete()
                    msg = "{}: Please send a real link, not an amp link you plebian!".format(message.author.mention)
                    await message.channel.send(msg)


client = AMPBot()
client.run(str(os.getenv("TOKEN")))
