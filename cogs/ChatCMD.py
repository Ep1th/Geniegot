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



class ChatCMD( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @app_commands.command(name='info', description='info about user')
    async def _info(self, interaction: discord.Interaction, usersname: discord.Member):
        await interaction.response.send_message(embeds= Func._emb_for_info(usersname))

    #@app_commands.command(name='come', description='info about user')
    #async def _come(self, interaction: discord.Interaction, usersname: discord.Member):

    #@app_commands.command(name='cd', description='')
    #async def _i56o(self, interaction: discord.Interaction, usersname: discord.Member):
        #await interaction.response.display_avatar

    @app_commands.command(name='добавить_анекдот', description='Geniegot will add a joke to jokeslist')
    async def _addjoke(self, interaction: discord.Interaction, joke_name: str, joke: str):
        try:
            newjoke = Anekdot(joke_name, joke)
            SQLDB.anekdot_add_to_db(newjoke)
            await interaction.response.send_message(
                f'Анекдот - хуйня, но я запомнил его, {interaction.user.display_name}')
        except:
            await interaction.response.send_message(
                f'Я не смог запомнить ваш анекдот, {interaction.user.display_name}, ')



    @app_commands.command(name='вопрос_к_джиниготу', description='Geniegot will answer any question')
    async def yes_or_no(self, interaction: discord.Interaction, your_question: str):
        try:
            async def fetch_data(arg=None):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://yesno.wtf/api') as response:
                        data = await response.json()
                        #answer = data['answer']
                        image = data['image']

                        #if arg == 'answer':
                            #return answer
                        #else:
                        return image

            await interaction.response.send_message(embed=Func.create_embed(
                f"Ответом на твой вопрос: {your_question}\nБудет: ").set_image(
                url=await fetch_data()))

        except:
            await interaction.response.send_message(f'Мне нужно подумать, спроси позже, {interaction.user.mention}')

    #
    @app_commands.command(name='анекдот', description='Geniegot will tell a joke')
    async def _joke(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=Func.create_embed(SQLDB.choose_random_joke()))


async def setup(bot):
    await bot.add_cog(ChatCMD(bot))