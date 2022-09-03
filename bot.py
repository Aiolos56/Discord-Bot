import discord
import random
import os
import time


class MyClient(discord.Client):
    async def on_readyon_ready(self):
        print(f'Connecté à {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('-Juste Prix'):
            a = True
            while a == True:  
              a = False
              b = True
              rdm = random.randint(1, 10)
              await message.channel.send("Choisissez un nombre : ")
              nbr = await self.wait_for('message')
              while b == True :
                if int(float(nbr.content)) > rdm :
                    await message.channel.send("Trop grand")
                    time.sleep(1)
                    await message.channel.send("Choisissez un nombre : ")
                    nbr = await self.wait_for('message')
                
                elif int(float(nbr.content)) < rdm :
                    await message.channel.send("Trop petit")
                    time.sleep(1)
                    await message.channel.send("Choisissez un nombre : ")
                    nbr = await self.wait_for('message')
                
                else:
                    await message.channel.send("Bravo")
                    b = False
                    time.sleep(1)
                    await message.channel.send("Voulez-vous recommencer ? [oui ou non] : ")
                    choix2 = await self.wait_for('message')

                    if str(choix2.content) == "oui":
                        a = True
                        await message.channel.send("Ok, on recommence")
                    elif str(choix2.content) == "non":  
                        a = False
                        await message.channel.send("À bientot !")
                
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTAxNTYxMzc0NzU1OTE1MzY2NA.GttPDJ.DyXljp1PX9zt6qsxt7LpH34mMr4C9aXPL2n5Ws')
