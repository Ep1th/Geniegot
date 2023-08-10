import random
import time
from bson import ObjectId
import discord
from discord.ext import commands
from .configs import MainConfig
#from .DataBase import Data
import sqlite3
from .SQLliteDB import SQLDB

class Func( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot

    def _emb_for_info(user):
        emb = discord.Embed(title=f"Информация о {user.display_name}", color=0x71368a)

        if user.id == 262525829815336961:
            emb.add_field(name="Натура", value='Ахуенный парень')
            emb.add_field(name="Строка из книги мудрости", value='Все прогрессы реакционны, если рушится человек')
        else:
            emb.add_field(name="Натура", value=SQLDB.choose_rd_nature())
            emb.add_field(name="Строка из книги мудрости", value=SQLDB.choose_rd_book())

        emb.set_thumbnail(url=user.avatar)
        emb.add_field(name="Имя пользователя", value=user.name)

        embed = discord.Embed()
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Присоединился в", value=str(user.joined_at)[:16])
        return emb, embed


    def create_embed(title, description = None):
        if description:
            embed = discord.Embed(title = title, description= description, color= MainConfig.EMBEDS_COLOR_PURP)

        else:
            embed = discord.Embed(title=title, color=MainConfig.EMBEDS_COLOR_PURP)

        return embed

async def setup( bot ):
    await bot.add_cog( Func(bot) )