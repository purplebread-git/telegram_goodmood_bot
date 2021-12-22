from aiogram_broadcaster import TextBroadcaster

import asyncio


async def main():

    # Initialize a text broadcaster (you can directly pass a token)
    broadcaster = TextBroadcaster('454025767', 'hello!', bot_token='2123244588:AAGv96QmBN7OPqmmH945_Lhx1ql1yp4_r1A')

    # Run the broadcaster and close it afterwards
    try:
        await broadcaster.run()
    finally:
        await broadcaster.close_bot()



asyncio.run(main())