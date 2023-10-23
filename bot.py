import discord 
import responses

intents = discord.Intents.default()
intents.message_content = True 
intents.voice_states = True
client = discord.Client(intents=intents)

async def send_message(message, user_message, is_private):
    username = str(message.author)
    if username == 'allfc#0':
        try:
            response = responses.lara_responses(user_message)
            if response:
                await message.channel.send(response)
                
        except discord.errors.Forbidden:
            print("O bot não tem permissão para enviar mensagens neste canal.")
        except Exception as e:
            print(e)
    else:
        try:
            response = responses.handle_responses(user_message)
            if response:
              await message.channel.send(response)
        except discord.errors.Forbidden:
            print("O bot não tem permissão para enviar mensagens neste canal.")
        except Exception as e:
            print(e)

@client.event
async def on_ready():
    print(f'{client.user} está em execução!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} disse: '{user_message}' ({channel})")

    if user_message and len(user_message) > 0 and user_message[0] == '!':
        
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

TOKEN = 'olaaa'
client.run(TOKEN)


