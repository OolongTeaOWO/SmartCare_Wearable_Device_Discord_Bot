# ------Discord------
from discord.interactions import Interaction
from discord.ext import commands
from discord import app_commands
import discord
# ------Other------
from datetime import datetime, timedelta, timezone

class CreateThread(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="thread_create", description="測試用")
    @app_commands.describe(channel = "選擇要發布貼文的頻道")
    @app_commands.rename(channel = "頻道")
    async def forum_create(self, interaction: discord.Interaction, channel: discord.ForumChannel):
        embed = discord.Embed(title="測試用")
        embed.add_field(name="apple", value=5, inline=False)
        taipei_timezone = timezone(timedelta(hours=8)) #獲得台北時區
        current_time = datetime.now(taipei_timezone) #將當前時間轉換成台北時區
        formatted_date_time = current_time.strftime("%Y-%m-%d %H:%M:%S") #格式化日期的字串
        await channel.create_thread(
            name = str(formatted_date_time),
            embed=embed
        )
        await interaction.response.send_message("建立完成!")

async def setup(bot):
    await bot.add_cog(CreateThread(bot))