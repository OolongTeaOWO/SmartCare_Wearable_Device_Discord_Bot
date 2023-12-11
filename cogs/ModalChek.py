# ------Discord------
from discord.ext import commands
from discord import app_commands
from discord.interactions import Interaction
from discord.ui import Modal
import discord

class ModeLtemPlate(discord.ui.Modal, title="測試用表單"):
    user_name = discord.ui.TextInput(label = "輸入使用者名稱",
                                            placeholder = "ex.John_Lin",
                                            required = True,
                                            max_length=100,
                                            style=discord.TextStyle.short)
    user_age = discord.ui.TextInput(label = "輸入使用者年紀",
                                            placeholder = "ex.16",
                                            required = True,
                                            max_length=100,
                                            style=discord.TextStyle.short)
    user_height = discord.ui.TextInput(label = "輸入使用者身高",
                                            placeholder = "ex.165",
                                            required = True,
                                            max_length=100,
                                            style=discord.TextStyle.short)
    async def on_submit(self, interaction: discord.Interaction):
        reponse_embed = discord.Embed(title="表單資料確認")
        reponse_embed.add_field(name="使用者名稱", value=self.user_name, inline=False)
        reponse_embed.add_field(name="使用者年紀", value=self.user_age, inline=False)
        reponse_embed.add_field(name="使用者身高", value=self.user_height, inline=False)
        await interaction.response.send_message(f'感謝您協助填寫該表單', embed=reponse_embed)
    
class Slash_Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="表單測試", description="測試表單功能")
    async def report(self, interaction: discord.Interaction):
        await interaction.response.send_modal(ModeLtemPlate())

async def setup(bot):
    await bot.add_cog(Slash_Command(bot))