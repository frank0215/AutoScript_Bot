import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import sys
sys.path.append('D:\\Python\\Github\\AutoScript_Bot')
import crawl
import crawl2
import crawl3
import datetime

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
    async def Beauty(self, ctx, stop=1, page=1):
        # random_pic = random.choice(jdata['url_pic'])
        arts = crawl.askArticle(page)
        imglist = crawl.saveImg(arts, stop)
        count = 0
        for img in imglist:
            await ctx.send(img)
            count += 1
        await ctx.send(f'{count} images have been presented')

    @commands.command()
    async def AV(self, ctx, stop=1, page=1):
        arts = crawl2.askArticle(page)
        imglist = crawl2.saveImg(arts, stop)
        count = 0
        for img in imglist:
            await ctx.send(img)
            count += 1
        await ctx.send(f'{count} images have been presented')

    @commands.command()
    async def AV2(self, ctx, start_date, period=0, pages=1):
        articlelist = crawl3.askArticle(start_date, period, pages)
        imglist, datelist, count = crawl3.saveImg(articlelist)
        for i, imgs in enumerate(imglist):
            await ctx.send(datetime.datetime.strftime(datelist[i], '%Y/%m/%d'))
            for img in imgs:
                await ctx.send(img)
            
        await ctx.send(f'{count} images have been presented')

    



def setup(bot):
    bot.add_cog(React(bot))