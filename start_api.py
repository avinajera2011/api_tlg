start = True
import asyncio
import gc
import importlib
import sys

from telegram_api import *

ex = 'n'

async def main():
    me = await client.get_me()
    await start_action(client)

if __name__ == "__main__":
    while ex != 'y':
        from telegram_actions import *
        # client = await main()
        with client:
            client.loop.run_until_complete(main())
        ex = input('Do you want to exit y/n?')
        importlib.reload(sys.modules['telegram_actions'])

