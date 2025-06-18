import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv
import asyncio
from agent import generate_response
from pprint import pprint
import random
import time


class PingCommand(Command):
    def __init__(self):
        self.latest_response_time = None

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
            current_time = time.time()
            should_respond = self.latest_response_time is None or current_time - self.latest_response_time >= 10
            print(f"Time since last response: {current_time - self.latest_response_time if self.latest_response_time else 'Never'} seconds")
            print(f"Should respond: {should_respond}")
            if not should_respond:
                return
            self.latest_response_time = current_time
            print(f"latest_response_time: {self.latest_response_time}")
            if random.random() < 0.1:  # 10% chance
                await c.react("👍")
            await c.start_typing()
            await asyncio.sleep(random.randint(1, 2))
            response = generate_response(c.message.text)
            await c.stop_typing()
            await c.send(response)

if __name__ == "__main__":
    load_dotenv()
    os.environ["SIGNAL_SERVICE"] = "127.0.0.1:8081"
    bot = SignalBot({
        "signal_service": os.environ["SIGNAL_SERVICE"],
        "phone_number": os.environ["PHONE_NUMBER"]
    })
    # exit()
    bot.register(PingCommand()) # all contacts and groups
    bot.start()
    