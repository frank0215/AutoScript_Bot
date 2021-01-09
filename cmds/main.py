import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('abcdefg')

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def rand_squad(self, ctx):
        online = []
        for member in ctx.guild.members:
            if str(member.status) == 'online' and not member.bot:
                online.append(member.name)
        
        random_online = random.sample(online, k=5)

        squads = 4
        for squad in range(squads):
            result = random.sample(random_online, k=5)
            await ctx.send('the {} squad: {}'.format(squad, str(result)))
            for name in result:
                random_online.remove(name)
                

    @commands.group()
    async def codetest(self, ctx):
        pass

    @codetest.command()
    async def python(self, ctx):
        await ctx.send('Python')

    @codetest.command()
    async def javascript(self, ctx):
        await ctx.send('Java')

    @codetest.command()
    async def cpp(self, ctx):
        await ctx.send('C++')

    @commands.command()
    async def cmdA(self, ctx, num:float):
        await ctx.send(num)

    @commands.command()
    async def cmdB(self, ctx, num):
        await ctx.send(num)
    

    
def setup(bot):
    bot.add_cog(Main(bot))