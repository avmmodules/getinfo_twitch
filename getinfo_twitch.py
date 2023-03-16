'''
    Description: Get info of Twitch channel with python.
    Author: aulerjbailey
    Version: 1.0.0
    Video: https://youtu.be/yUS4Zf1FLcs
'''
from twitch import TwitchClient

id = 'YOUR_CLIENT_ID'
channel_id = 'CHANNEL_ID'

# authenticate
client = TwitchClient(client_id=id)

# search channel
channel = client.channels.get_by_id(channel_id)

# prints the info
print(f'Soy {channel.name} y tengo {channel.followers} suscriptores')
