
import os
from telethon import TelegramClient, events
import asyncio

# Get credentials from environment variables
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

# Channel and message info
channel_username = 'Idreez_01'
trigger_phrase = 'first to send'
receiver_username = '@Idreez_03'
message_to_send = "9049164098\nOpay\nOPEYEMI TOLULOPE JOSEPH"

# Use session in same folder (or change to 'data/session' if needed)
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    if trigger_phrase in event.raw_text.lower():
        await client.send_message(receiver_username, message_to_send)
        print("✅ Trigger detected. Message sent.")

async def main():
    await client.start()
    print("🤖 Bot is online and monitoring messages...")
    await client.run_until_disconnected()

# Run the bot and keep it alive
asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()
