from discord_webhook import DiscordWebhook
import asyncio

#Spam (up to 30 messages)
while True:
	Text = ('Message')
	Webhook = DiscordWebhook(url='Webhook_URL',content=str(Text))
	Webhook.execute()
asyncio.sleep(5)

#Normal
Text = ('Message')
Webhook = DiscordWebhook(url='Webhook_URL',content=str(Text))
Webhook.execute()

#Please Put """ and """ between which type of webhook you are using
