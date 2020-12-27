import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # print(f'{member} join!')
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # print(f'{member} leave!')
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f'{member} leave!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        # if msg.content.endswith('apple'):
        #     await msg.channel.send('hi')
        
        # if msg.content == 'apple' and msg.author != self.bot.user:
        #     await msg.channel.send('apple')

        keyword = ['apple', 'pen', 'pie', 'abc']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('apple')

def setup(bot):
    bot.add_cog(Event(bot))
