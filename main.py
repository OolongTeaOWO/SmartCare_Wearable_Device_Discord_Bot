# ------Discord------
from discord.ext import commands
import discord
# -------other-------
from dotenv import load_dotenv
from loguru import logger
from datetime import datetime
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
start_time = datetime.now()
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await load_all_extensions()
    logger.info(f'{bot.user} | Ready!')

async def load_all_extensions():
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'cogs')):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                logger.info(F'[初始化] 載入 Extension: {filename[:-3]}')
            except Exception as exc:
                logger.error(F'[初始化] 載入 Extension 失敗: {exc}')
    logger.info('[初始化] Extension 載入完畢')

@bot.command(name='sync', brief='Bot Slash Command Sync', description='Bot Slash Command Sync')
async def sync_command(ctx):
    await bot.tree.sync()
    await ctx.send('已更新完畢!')
    logger.debug('extentions are synced to the command tree')

@bot.command(name='status', brief="機器人狀態", description="顯示機器人目前狀態，用以除錯。\n會列出所有拓展名稱和權限")
async def status(ctx):
    if ctx.author.id not in (bot.owner_id, 541668345728991286):
        await ctx.send(embed=discord.Embed(title="權限不足", description=F"本指令只提供給機器人擁有者\n本機器人擁有者為<@{bot.owner_id}>"))
        return
    embed = discord.Embed(title="目前機器人的狀態:")
    embed.add_field(name="目前延遲", value=F"{round(bot.latency*1000)}ms", inline=False)
    exts = "\n".join(ext.replace("cogs.", "") for ext in bot.extensions)
    embed.add_field(name="已加載擴展", value=f">>> {exts}" if exts else "目前沒有任何擴展", inline=True)
    all_exts = "\n".join(filename[:-3] for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'cogs')) if filename.endswith('.py'))
    embed.add_field(name="目前擁有的擴展",value=f">>> {all_exts}" if all_exts else "找不到任何擴展", inline=True)
    embed.add_field(name="在線時間", value=f">>> <t:{int(start_time.timestamp())}:R>", inline=False)
    await ctx.send(embed=embed)
            
@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title="Healthyble功能啟用前置", description="請在伺服器新增以下幾個名稱的頻道以便啟用相關功能")
    embed.add_field(name="1.錯誤通知區:", value="如文字指令有誤可以在這裡看到")
    try:
        await guild.owner.send(embed=embed)
        print(guild.owner_id)
    except:
        print(f"{guild.owner} has their dms turned off")
    if guild.system_channel:
        await guild.system_channel.send("初次見面請多多指教!")
    else:
        pass

if __name__ == '__main__':
    bot.run(TOKEN)
