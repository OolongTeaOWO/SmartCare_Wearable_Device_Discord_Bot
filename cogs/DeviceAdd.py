# ------Discord------
from discord.ui import Button, View
from discord.ext import commands
from discord import app_commands
import discord
# ------Other------
import json
from ImportFunction.Modaltemplate import ModeLtemPlate

check_device = True
Is_userDevice = True

class Devices_Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="新增穿戴裝置", description="測試用")
    @app_commands.describe(device_name="輸入想為該裝置定義的名稱", device_id="輸入該裝置的設備id")
    @app_commands.rename(device_name="裝置名稱", device_id="裝置id")
    async def add_device(self, interaction: discord.Interaction, device_name:str, device_id:str):
        check = True
        with open('User_Data/User_Data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)
        device_json = {
            "device_name":"",
            "device_id":""
        }
        for user in range(len(data_list)):
            if data_list[user]["discord_id"] == interaction.user.id:
                device_json["device_id"] = device_id
                device_json["device_name"] = device_name
                data_list[user]["devices"].append(device_json)
            else:
                check = False
        if check == True:
            with open('User_Data/User_Data.json', 'w', encoding='utf-8') as file:
                json.dump(data_list, file, indent=2, ensure_ascii=False)
            await interaction.response.send_message("裝置已新增", ephemeral=True)
        else:
            await interaction.response.send_message("缺少資料,你可能尚未註冊好個人資料", ephemeral=True)

        


async def setup(bot):
    await bot.add_cog(Devices_Add(bot))