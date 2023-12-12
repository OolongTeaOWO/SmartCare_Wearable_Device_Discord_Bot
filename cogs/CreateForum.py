# ------Discord------
from discord.interactions import Interaction
from discord.ext import commands
from discord import app_commands
import discord

class CreateForum(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="創建貼文主頻道", description="測試用")
    async def forum_create(self, interaction: discord.Interaction):
        guild = interaction.guild
        await guild.create_forum(
            name="測試用貼文頻道"
        )
        await interaction.response.send_message("建立完成!")

async def setup(bot):
    await bot.add_cog(CreateForum(bot))