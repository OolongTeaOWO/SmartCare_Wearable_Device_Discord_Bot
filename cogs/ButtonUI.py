# ------Discord------
import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord.ui import Button, View
# ------Other------
from ImportFunction.Register import Register

primary = discord.ButtonStyle.primary
green = discord.ButtonStyle.green
danger = discord.ButtonStyle.danger

class ButtonUI(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        Register_button = Button(label="註冊使用者", style=green)
        # ------以下是callback
        async def Register_callback(interaction):
            Register_button.disabled = True
            messages = interaction.message
            await messages.edit(embed=embed, view=Basic_View)
            await interaction.response.send_modal(Register())
        Register_button.callback = Register_callback

        Basic_View = View()
        Basic_View.add_item(Register_button)

        embed = discord.Embed(title="Heathlyble健康寶互動UI",
                        description="避免在此發送訊息,否則機器人將會刷新UI位置")
        
        if member.guild.name == "Heathlyble_ForUser":
            await member.send(embed=embed, view=Basic_View)


async def setup(bot):
    await bot.add_cog(ButtonUI(bot))