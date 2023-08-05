import asyncio
import discord
from discord.ext import commands
import logging
import os
import config

discord.utils.setup_logging(level=logging.INFO, root = True)
bot = commands.AutoShardedBot(intents= discord.Intents.all(), command_prefix='"')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(bot.guilds)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            if filename != '__init__.py':
                await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(config.TOKEN)


asyncio.run(main())