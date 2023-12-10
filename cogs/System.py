# ------Discord------
import discord
from discord.ext import commands
from core.classes import Cog_Extension
# -------other-------
from googletrans import Translator #把錯誤訊息轉成中文用的google翻譯api套件

translator = Translator()

class System(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        user = ctx.author
        error = translator.translate(error, dest='zh-tw').text
        embed = discord.Embed(title="糟糕!發生了一些問題!",description=str(error), color=0xe01b24)
        embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar.url)
        embed.add_field(name="內容 Context",value=ctx.message.content)

        embed_config = discord.Embed(title="缺少錯誤訊息發送頻道",description="請在伺服器內創建名為錯誤通知區的頻道", color=0xe01b24)
        if isinstance(ctx.channel, discord.channel.DMChannel):
            embed.add_field(name="頻道 Channel",value="私人 Private")
            await user.send(embed=embed)
        else:
            channel = discord.utils.get(ctx.guild.channels, name="錯誤通知區")
            server_owner = ctx.guild.owner
            if channel:
                embed.add_field(name="頻道 Channel",value=ctx.guild.name+'/'+ctx.channel.name)
                await channel.send(embed=embed)
            else:
                await server_owner.send(embed=embed_config)

async def setup(bot):
    await bot.add_cog(System(bot))