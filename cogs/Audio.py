import asyncio
import random
import time
from bson import ObjectId
import discord
from discord.ext import commands
from .configs import MainConfig
# from .DataBase import Data
from discord import app_commands
from .Functions import Func
from .SQLliteDB import SQLDB
from cogs.models.ModelToSqlDB import Anekdot
import aiohttp

class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass






async def setup(bot):
    await bot.add_cog(Audio(bot))