# ------Discord------
import discord
from discord.ui import Button, View, Modal 
from discord.ext import commands
from discord import app_commands

primary = discord.ButtonStyle.primary
green = discord.ButtonStyle.green
danger = discord.ButtonStyle.danger

class ButtonUIS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="button_modals", description="測試表單")
    async def button_ms(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Heathlyble健康寶互動UI",
                        description="避免在此發送訊息,否則機器人將會刷新UI位置")
        Registers_button = Button(label="註冊使用者", style=green)
        Add_Device_button = Button(label="新增裝置", style=green, disabled=True)
        Feedback_button = Button(label="反映問題", style=danger, disabled=True)
        Edit_Data_button = Button(label="修改資料", style=primary, disabled=True)

        # ------以下是callback
        async def Registers_callback(interaction):
            Registers_button.disabled = True
            Add_Device_button.disabled = False
            Feedback_button.disabled = False
            Edit_Data_button.disabled = False
            if Registers_button.label == "更新個人資料":
                Registers_button.label == "註冊使用者"
            await interaction.response.edit_message(embed=embed, view=Basic_Views)

        async def Edit_Data_callback(interaction):
            Registers_button.label = "更新個人資料"
            Registers_button.disabled = False
            Edit_Data_button.disabled = True
            Add_Device_button.disabled = True
            Feedback_button.disabled = True
            await interaction.response.edit_message(embed=embed, view=Basic_Views)

        Registers_button.callback = Registers_callback
        Edit_Data_button.callback = Edit_Data_callback
        Basic_Views = View()
        Basic_Views.add_item(Registers_button)
        Basic_Views.add_item(Add_Device_button)
        Basic_Views.add_item(Feedback_button)
        Basic_Views.add_item(Edit_Data_button)

        await interaction.response.send_message(embed=embed, view=Basic_Views)

async def setup(bot):
    await bot.add_cog(ButtonUIS(bot))