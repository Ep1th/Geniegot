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


class EconomySys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(self.bot.guilds)

    @app_commands.command(name='добавить_анекдот', description='Geniegot will add a joke to jokeslist')
    async def _addjoke(self, interaction: discord.Interaction, joke_name: str, joke: str):
        try:
            newjoke = Anekdot(joke_name, joke)
            SQLDB.anekdot_add_to_db(newjoke)
            await interaction.response.send_message(f'Анекдот - хуйня, но я запомнил его, {interaction.user.display_name}')
        except:
            await interaction.response.send_message(
                f'Я не смог запомнить ваш анекдот, {interaction.user.display_name}, ')

#
    @app_commands.command(name='анекдот', description='Geniegot will tell a joke')
    async def _joke(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=Func.create_embed(SQLDB.choose_random_joke()))


async def setup(bot):
    await bot.add_cog(EconomySys(bot))
