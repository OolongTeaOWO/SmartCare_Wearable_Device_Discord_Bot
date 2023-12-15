import json
import discord
from ImportFunction.TextInputEdit import TextInputs

class Register(discord.ui.Modal, title="測試用表單"):
    Label_list = ["輸入使用者名稱", "輸入備用gmail"]
    Placeholder_list = ["ex.王小名 或 ex.John", "ex.xxxx@gmail.com"]
    Mode_list = ["Must", "Must"]
    user_name, user_gmail = [
        TextInputs(Mode, Label, Placeholder)
        for Mode, Label, Placeholder in zip(Mode_list, Label_list, Placeholder_list)
    ]

    async def on_submit(self, interaction: discord.Interaction):
        reponse_embed = discord.Embed(title="表單資料確認")
        user_names = ""
        user_gmails = ""
        with open('User_Data/User_Data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)
        data = {
        "discord_id": "your_discord_id",
        "discord_name": "",
        "user_name": "",
        "user_gmail": "",
        "devices": []
                }  
        for label, attribute in zip(Register.Label_list, ["user_name", "user_gmail"]):
            field_value = getattr(self, attribute)
            reponse_embed.add_field(name=f'{label}', value=field_value, inline=False)
            data[attribute] = str(field_value)
        data["discord_id"] = interaction.user.id
        data["discord_name"] = interaction.user.name
        data_list.append(data)
        with open('User_Data/User_Data.json', 'w', encoding='utf-8') as file:
            json.dump(data_list, file, indent=2, ensure_ascii=False)
        print(data["user_name"])
        await interaction.response.send_message(embed=reponse_embed)