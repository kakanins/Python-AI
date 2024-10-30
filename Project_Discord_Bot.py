import discord
import random

sad_words = ["sad", "depressed", "angry", "hurting", "stressed"]

encouragements = [
  "Cheer up! 🤗",
  "Hang in there 😉",
  "You are a great person!👍 ",
  "Come on! You can do it! 💪",
  "Stay strong 🥰 "
]

intents = discord.Intents.default()
intents.message_content = True #Configure it so that messages from the client can be read
client = discord.Client(intents=intents) #Create a connection between clients and discord. The Client class is used to interact with discord.

@client.event
async def on_message(message): #on_message()called when the bot receives a message
    if message.author == client.user:
        return

    if message.content.startswith('!hi'):
        await message.channel.send(f'Hello 👋😃')

    if message.content.startswith('!hello'):
        await message.channel.send('https://media.giphy.com/media/VOZ1LKbOfkg3S/giphy.gif')

    if any(word in message.content for word in sad_words): #If sending a sentence that contains the word in the list  sad_words
        response = random.choice(encouragements) #Select one item on the encouragements list as a response
        await message.channel.send(response)

#add code above
client.run('MTE3NjQxNzY0NzEwMjAwNTQwOQ.GtsnII.Gww5YmV8DZNqOKe_DghvlTg8HKQ4_lfp6zpFwM')

@client.event 
async def on_ready(): 
    print("We have logged in as {0.user}".format(client))

client.run("MTE3NjQxNzY0NzEwMjAwNTQwOQ.GtsnII.Gww5YmV8DZNqOKe_DghvlTg8HKQ4_lfp6zpFwM")