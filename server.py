import os
import discord


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
                if "ampproject.org" in content.lower():
                    await message.delete()
                    msg = "{}: Please send a real link, not an amp link you plebian!".format(message.author.mention)
                    await message.channel.send(msg)


client = AMPBot()
client.run(str(os.getenv("TOKEN")))
