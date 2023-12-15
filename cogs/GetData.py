# ------Discord------
import discord
from discord.ext import commands
from core.classes import Cog_Extension
# ------Other-------->
import ast
import asyncio
import sys
from ImportFunction import Address_Locator as Address
from ImportFunction.Datetime import DatetimeGet
data = {}

class GetData(Cog_Extension):
                
    @commands.Cog.listener()
    async def on_message(self, msg):
        pass

async def setup(bot):
    await bot.add_cog(GetData(bot))