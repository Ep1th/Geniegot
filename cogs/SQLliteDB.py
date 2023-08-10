import random
import time
from bson import ObjectId
import discord
from discord.ext import commands
from cogs.models.ModelToSqlDB import Anekdot
import sqlite3
#newjoke = Anekdot('Shtirmina','Штирлиц играл в карты и проигрался. Но Штирлиц умел делать хорошую мину при плохой игре. Когда Штирлиц покинул компанию, мина сработала.')

class SQLDB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def choose_random_joke():
        con = sqlite3.connect('SQLDB.db')
        cur = con.cursor()
        cur.execute("SELECT content FROM jokes ORDER BY RANDOM() LIMIT 1 ")
        x = cur.fetchone()
        con.commit()
        return str(x)[2:-3]

    def choose_rd_nature():
        con = sqlite3.connect('SQLDB.db')
        cur = con.cursor()
        cur.execute("SELECT nature FROM info ORDER BY RANDOM() LIMIT 1 ")
        x = cur.fetchone()
        con.commit()
        return str(x)[2:-3]

    def choose_rd_book():
        con = sqlite3.connect('SQLDB.db')
        cur = con.cursor()
        cur.execute("SELECT bookofwise FROM info ORDER BY RANDOM() LIMIT 1 ")
        x = cur.fetchone()
        con.commit()
        return str(x)[2:-3]
    def anekdot_add_to_db(anekdot):
        #Принимает экземпляры класса Anekdot
        con = sqlite3.connect(r'D:/PYCHARM projects/Geniego/SQLDB.db')
        cur = con.cursor()
        data = [anekdot.name, anekdot.content]
        cur.execute("INSERT INTO jokes(name,content) VALUES(?, ?)", data)
        con.commit()


async def setup(bot):
    await bot.add_cog(SQLDB(bot))


if __name__ == '__main__':
    SQLDB.anekdot_add_to_db(newjoke)
