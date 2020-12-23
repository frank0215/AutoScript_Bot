import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    # print(f'{member} join!')
    channel = bot.get_channel(791294518641164288)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    # print(f'{member} leave!')
    channel = bot.get_channel(791294563875946576)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('NzkxMjgyNzE2NDU1ODYyMjcy.X-M5dA.IWvMt5mbeHKBOIAX2-v6-jW0v20')