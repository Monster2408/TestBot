# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import locale
locale.setlocale(locale.LC_ALL, '')
from datetime import datetime
import traceback 
import pytz
from japanera import EraDate
import asyncio

import Var

class MyBot(commands.Bot):
    def __init__(self, prefix: str, intents: discord.Intents):
        super().__init__(command_prefix=prefix, intents=intents)

    async def setup_hook(self):
        # スラッシュコマンドの同期をここで実行
        try:
            synced = await self.tree.sync(guild=None)
            print(f"Synced global commands. {synced}")
            for guild in self.guilds:
                synced = await self.tree.sync(guild=discord.Object(id=guild.id))
                print(f"Synced guild command(id={str(guild.id)}). {synced}")
        except Exception:
            traceback.print_exc()  # どこでエラーが発生したか表示

    async def on_ready(self):
        try:
            print('-----')
            print(self.user.name)
            print(f'{self.user.name}のバージョンはv{Var.BOT_VERSION}')
            print(f'{Var.BOT_MODULE}のバージョンはv{discord.__version__}')
            print('-----')
            await self.wait_until_ready()
            await self.change_presence(status=discord.Status.online, activity=discord.Game("/help"))
        except Exception:
            traceback.print_exc()

async def main():
    bot = MyBot(intents=discord.Intents.all(), prefix='!?')
    await bot.start(token=Var.token)

if __name__ == '__main__':
    asyncio.run(main())