import random
import time
from bson import ObjectId
import discord
from discord.ext import commands
from .configs import MainConfig
#from .DataBase import Data

class DB( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot


async def setup( bot ):
    await bot.add_cog( DB(bot) )