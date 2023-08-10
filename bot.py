import asyncio
import discord
from discord.ext import commands
import logging
import os
import config

discord.utils.setup_logging(level=logging.INFO, root = True)
bot = commands.AutoShardedBot(intents= discord.Intents.all(), command_prefix='"')
bot.remove_command('help')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, limit: int):
    deleted = await ctx.channel.purge(limit=limit)
    await ctx.send('{} замёл следы'.format(ctx.author.mention))
    await ctx.message.delete()

@bot.command('иди-на-хуй')
async def hui(ctx):
    k=0
    while k != 100:
        k+=1
        await ctx.send('https://tenor.com/view/%D0%B8%D0%B4%D0%B8%D0%BD%D0%B0%D1%85%D1%83%D0%B9-%D0%BF%D1%83%D0%B4%D0%B6-%D0%B8%D0%B4%D0%B8%D0%BD%D0%B0%D1%85%D1%83%D0%B9%D0%B4%D0%BE%D1%82%D0%B0-%D0%B8%D0%B4%D0%B8%D0%BD%D0%B0%D1%85%D1%83%D0%B9%D0%BF%D1%83%D0%B4%D0%B6-%D0%B8%D0%B4%D0%B8%D0%BD%D0%B0%D1%85%D1%83%D0%B9pudge-gif-26100509')

@bot.command('csn')
async def change_server_name(ctx, new_name):
    # Проверяем, что бот имеет права управления сервером
    if ctx.guild is not None and ctx.guild.me.guild_permissions.manage_guild:
        try:
            # Изменяем название сервера
            await ctx.guild.edit(name=new_name)
            await ctx.send(f'Название сервера изменено на: {new_name}')
        except discord.Forbidden:
            await ctx.send('У меня нет прав на изменение названия сервера.')
    else:
        await ctx.send('У меня недостаточно прав для управления сервером.')
@bot.command()
async def create_role(ctx):
    # Проверяем, что бот имеет права управления ролями на сервере
    if ctx.guild is not None and ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send('Введите название новой роли:')
        try:
            response = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
            role_name = response.content

            await ctx.send('Введите права для новой роли (например, "manage_messages, kick_members"):')
            response = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
            permissions_input = response.content

            # Разделяем строку с правами на список, удаляя пробелы
            permissions_list = [perm.strip() for perm in permissions_input.split(',')]
            permissions = discord.Permissions()

            # Добавляем указанные права к объекту Permissions
            for perm_name in permissions_list:
                permission = getattr(discord.Permissions, perm_name, None)
                if permission is not None:
                    permissions.update(**{perm_name: True})

            # Создаем новую роль с указанными параметрами
            new_role = await ctx.guild.create_role(name=role_name, permissions=permissions)
            await ctx.send(f'Роль "{new_role.name}" создана с указанными правами.')
        except asyncio.TimeoutError:
            await ctx.send('Время ожидания истекло. Попробуйте еще раз.')
    else:
        await ctx.send('У меня недостаточно прав для управления ролями.')

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