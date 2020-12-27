import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def Picture(self, ctx):
        #random_pic = random.choice(jdata['pic'])
        #pic = discord.File(random_pic)
        pics = jdata['pic']
        for pic in pics:
            await ctx.send(file=pic)

    @commands.command()
    async def Beauty(self, ctx):
        # random_pic = random.choice(jdata['url_pic'])
        beauties = jdata['url_pic']
        for beauty in beauties:
            await ctx.send(beauty)


def setup(bot):
    bot.add_cog(React(bot))