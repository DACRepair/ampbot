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
            print(content)
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
                                if "amp" in list(item.attrib.keys()):
                                    test = True
                                    test_url = url
                if test:
                    await message.delete()
                    msg = "{} sent an amp link. Please use real links dipshit.".format(message.author.mention)
                    if os.getenv("SPOILER", "false").lower() == "true":
                        msg = msg + "\n ||{}||".format(test_url)
                    await message.channel.send(msg)


client = AMPBot()
client.run(str(os.getenv("TOKEN")))
