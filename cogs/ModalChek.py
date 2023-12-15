# ------Discord------
from discord.ext import commands
from discord import app_commands
import discord
# ------Other------
from ImportFunction.Modaltemplate import ModeLtemPlate
    
class ModalChek(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="modal_call", description="測試表單功能")
    async def report(self, interaction: discord.Interaction):
        await interaction.response.send_modal(ModeLtemPlate())

async def setup(bot):
    await bot.add_cog(ModalChek(bot))