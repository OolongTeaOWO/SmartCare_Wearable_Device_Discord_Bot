# ------Discord------
from typing import Any
from discord.ext import commands
from discord import app_commands
from discord.interactions import Interaction
from discord.ui import Modal
from ImportFunction.TextInputEdit import TextInputs
import discord

class ModeLtemPlate(discord.ui.Modal, title="測試用表單"):
    Label_list = ["輸入使用者名稱", "輸入使用者年紀", "輸入使用者身高"]
    Placeholder_list = ["ex.John_Lin", "ex.16", "ex165"]
    Mode_list = ["Must", "Free", "Must"]
    user_name, user_age, user_height = [
        TextInputs(Mode, Label, Placeholder)
        for Mode, Label, Placeholder in zip(Mode_list, Label_list, Placeholder_list)
    ]
    async def on_submit(self, interaction: discord.Interaction):
        reponse_embed = discord.Embed(title="表單資料確認")
        for label, attribute in zip(["名稱", "年紀", "身高"], ["user_name", "user_age", "user_height"]):
            field_value = getattr(self, attribute)
            reponse_embed.add_field(name=f'使用者{label}', value=field_value, inline=False)
        await interaction.response.send_message(f'感謝您協助填寫該表單', embed=reponse_embed)
    
class Slash_Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="表單測試", description="測試表單功能")
    async def report(self, interaction: discord.Interaction):
        await interaction.response.send_modal(ModeLtemPlate())

async def setup(bot):
    await bot.add_cog(Slash_Command(bot))