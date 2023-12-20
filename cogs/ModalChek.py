# ------Discord------
from discord.ui import Button, View
from discord.ext import commands
from discord import app_commands
import discord
import asyncio
# ------Other------
from ImportFunction.Modaltemplate import ModeLtemPlate

green = discord.ButtonStyle.green
class ModalChek(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="modal_call", description="測試表單功能")
    async def report(self, interaction: discord.Interaction):
        await interaction.response.send_modal(ModeLtemPlate())
    
    @app_commands.command(name="button_modal", description="測試表單")
    async def button_m(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Heathlyble健康寶互動UI",
                        description="避免在此發送訊息,否則機器人將會刷新UI位置")
        Registers_button = Button(label="註冊使用者", style=green)
        # ------以下是callback
        async def Registers_callback(interaction):
            Registers_button.disabled = True
            messages = interaction.message
            await messages.edit(embed=embed, view=Basic_Views)
            await interaction.response.send_modal(ModeLtemPlate())

        Registers_button.callback = Registers_callback

        Basic_Views = View()
        Basic_Views.add_item(Registers_button)

        await interaction.response.send_message(embed=embed, view=Basic_Views)

async def setup(bot):
    await bot.add_cog(ModalChek(bot))