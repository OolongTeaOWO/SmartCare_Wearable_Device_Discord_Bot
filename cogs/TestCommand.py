# ------Discord------
import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Text_Simple_Command(Cog_Extension):
                
    @commands.command(name = "ping", description="查看bot的ping")
    async def ping(self, ctx: commands.Context):
        latency = round(self.bot.latency*1000)
        red = max(0, min(int(255*(latency-50)/1000), 255))
        green = 255-red
        color = discord.Colour.from_rgb(r=red, g=green, b=0)
        embed = discord.Embed(title="目前Discord Bot的延遲", description=F"目前延遲: {latency}", color=color)
        await ctx.send(embed=embed,ephemeral=True)

async def setup(bot):
    await bot.add_cog(Text_Simple_Command(bot))