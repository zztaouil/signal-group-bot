import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv
import asyncio
from agent import generate_response
from pprint import pprint
import random

class PingCommand(Command):
    async def handle(self, c: Context):
        # print(f"Received message: {c.message.text}")
        # pprint(f"source: {c.message.source}")
        # pprint(f"source_number: {c.message.source_number}")
        # pprint(f"source_uuid: {c.message.source_uuid}")
        # pprint(f"timestamp: {c.message.timestamp}")
        # pprint(f"type: {c.message.type}")
        # pprint(f"text: {c.message.text}")
        # pprint(f"group: {c.message.group}")
        if c.message.text is not None:
            if random.random() < 0.1:  # 10% chance
                await c.react("👍")
            await c.start_typing()
            await asyncio.sleep(random.randint(1, 2))
            response = generate_response(c.message.text)
            await c.stop_typing()
            await c.send(response)

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
    