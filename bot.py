import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv
import asyncio
from agent import generate_response, download_shrek
from pprint import pprint
import random
import base64
import time
import requests

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
        if c.message.text is not None and c.message.text.startswith("@shrek"):
            current_time = time.time()
            should_respond = self.latest_response_time is None or current_time - self.latest_response_time >= 0.1
            print(f"Time since last response: {current_time - self.latest_response_time if self.latest_response_time else 'Never'} seconds")
            print(f"Should respond: {should_respond}")
            if not should_respond:
                return
            self.latest_response_time = current_time
            print(f"latest_response_time: {self.latest_response_time}")
            if random.random() < 0.5:  # 50% chance
                await c.react("👍")
            await c.start_typing()
            await asyncio.sleep(random.randint(1, 2))
            # response = generate_response(c.message.text)
            download_shrek()
            await c.stop_typing()
            r = requests.get("https://zenquotes.io/api/random")
            data = r.json()
            caption = generate_response(c.message.text.replace("@shrek", ""))
            # caption = data[0]["q"]
            await c.send("@pp " + caption, base64_attachments=[base64.b64encode(open("shrek.png", "rb").read()).decode("utf-8")])

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
    