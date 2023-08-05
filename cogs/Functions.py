import random
import time
from bson import ObjectId
import discord
from discord.ext import commands
from .configs import MainConfig
#from .DataBase import Data
import sqlite3

class Func( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot



    def create_embed(title, description = None):
        if description:
            embed = discord.Embed(title = title, description= description, color= MainConfig.EMBEDS_COLOR)

        else:
            embed = discord.Embed(title=title, color=MainConfig.EMBEDS_COLOR)

        return embed

async def setup( bot ):
    await bot.add_cog( Func(bot) )