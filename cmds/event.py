import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from cmds.main import Main

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

    # 處理"指令"發生的錯誤 Error Handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send('need a parameter')
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send('wrong command')
        else:
            await ctx.send("it doesn't occur!")

    # 指令個別專用的錯誤處理
    @Main.cmdB.error
    async def cmdB_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send('input parameter')

    # @commands.Cog.listenter()
    # async def on_reaction_add(self, reaction, user):
    #     print(reaction+ '\n' + user)

    @commands.Cog.listener()
    async def on_raw_raction_add(self,data):
        # print(data.emoji)
        # print(data.member)
        # 新增反應貼圖獲取身分組
        # 1. 使用者新增反應
        # 2. 判斷反應貼圖
        # 3. 給於身分組
        if str(data.emoji) == '':
            guild = self.bot.get_guild(data.guild_id) # 取得當前所在伺服器
            role = guild.get_role() # 取得伺服器內指定的身分組
            await data.member.add_roles(role) # 給於該成員身分組




        

    


def setup(bot):
    bot.add_cog(Event(bot))
