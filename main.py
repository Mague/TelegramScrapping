#!/usr/bin/env python3

from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
def settings(path="config"):
	result = {}
	with open(path,'r',encoding='utf-8') as file:
		for line in file:
			data = line.split("=")
			key = data[0].strip()
			value = data[1].strip()
			if value.isnumeric():
				result[key] = int(value)
			else:
				result[key] = value
			##print(result)
	return result
async def update_handler(res):
	data = str(res)
	try:
		print(data)
	except exception as e:
		print(e)
data_config = settings()

session = "EasyTradingVE"
client = TelegramClient(
			session,
			int(data_config['api_id']),
			data_config['api_hash'],
			proxy = None
			#update_workers=4
			#spawn_read_thread=False
		)

client.add_event_handler(update_handler)
with client.start("+584267257288"):
	print('Ctrl+C para detener')
	client.run_until_disconnected()