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

class GetDtata(Cog_Extension):
                
    @commands.Cog.listener()
    async def on_message(self, msg):
        global data
        Target_channel = self.bot.get_channel(1183249213870592100)
        if msg.author != self.bot.user: #過濾來自機器人自己發的訊息
            if (msg.guild.name == 'HeathlybleData' and #檢查伺服器名稱
                msg.channel.name == '資料接收' #檢查訊息來源頻道
                ):
                data = ast.literal_eval(msg.content)
                embed = discord.Embed(
                    title="健康監測資料反饋",
                    color=discord.Color.blue())
                address_dict = {"latitude":0, "longtitude":0}
                device_name = ""
                formatted_date_time = DatetimeGet.GetNowDT()
                for key, value in data.items():
                    if key in address_dict:
                        address_dict[key] = value
                    else:
                        embed.add_field(name=key, value=value, inline=False)
                embed.add_field(name="所在位置", value=f'{Address.Address_Locator(address_dict["latitude"], address_dict["longtitude"])}')
                embed.add_field(name="日期", value=formatted_date_time)
                await Target_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GetDtata(bot))