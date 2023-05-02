import discord
import os
import openai
from chatgpt import ChatGPT

# Set up the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up the ChatGPT model
chatbot = ChatGPT(engine="davinci", temperature=0.7)

# Set up the Discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        input_text = message.content[1:]
        response = chatbot.get_response(input_text)
        await message.channel.send(response)

# Run the Discord client
client.run('your_discord_bot_token_here')
