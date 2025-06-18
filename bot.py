import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv
import asyncio

class PingCommand(Command):
    async def handle(self, c: Context):
        # if c.message.text == "Ping":
        await c.react("👍")
        await c.send("Kayna awda hadak")


if __name__ == "__main__":
    load_dotenv()
    os.environ["SIGNAL_SERVICE"] = "127.0.0.1:8080"
    bot = SignalBot({
        "signal_service": os.environ["SIGNAL_SERVICE"],
        "phone_number": os.environ["PHONE_NUMBER"]
    })
    # exit()
    bot.register(PingCommand()) # all contacts and groups
    bot.start()
    