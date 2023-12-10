# ------Discord------
from discord.ext import commands
from discord import app_commands
import discord
# ------Other-------->
from typing import List

class Slash_Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Slash_Command(bot))