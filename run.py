#!/usr/bin/python3
import asyncio
import discord
import settings
import sql_driver
import time

from command import (please_make_decision,
                     russian_roulette,
                     weather,
                     keywords,
                     keyword_manager,)

token = settings.TOKEN

client = discord.Client()
russian_roulette = russian_roulette.Game()
weather = weather.Now()
connection, cursor =  sql_driver.db_init()

@client.event
async def on_ready():
    '''
    un-certified
    who cames here?
    logging function
    '''
    response = client.user.name + ' 님이 들어오셨어요!'
    # add logger on this line
    print(response)
    
@client.event
async def on_member_join(member):
    '''
    un-certified
    if user come, bot send DM to user.
    '''
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello! {member.name}. welcome to this channel'
    )

@client.event
async def on_message(message):
    '''
    this async function check message event.
    please route message to 'command module'
    '''
    global cursor
    global connection

    # check message event
    # print('message log >> {}'.format(message.content))

    print(message.author.name)
    # Bot Loop-back Test
    if message.author.name == settings.DISCORD_BOT_NAME:
        try:
            pass # do something on this line
        except Exception as e:
            pass # clear exception by ref 'e'

    # User message event
    else:
        print ('message content : {}'.format( message.content ) )
        # if you says 'hey kiddo ~~~ ?', this bot response "YES: ㅇㅇ" or "NO: ㄴㄴ"
        if message.content[:9] == 'hey kiddo' and message.content[-1] == '?':
            response = please_make_decision.action()
            await message.channel.send(response)

        # if you says '!댄스타임', this bot start twerking.
        elif message.content == '!댄스타임':
            if settings.DANCE is True:
                settings.DANCE = False
            else:
                settings.DANCE = True
                while settings.DANCE:
                    await message.channel.send('))')
                    time.sleep(0.5)
                    await message.channel.send('((')
                    time.sleep(0.5)
                    
        # if you says '!발사', this bot start russian roulette game.
        elif message.content.find('!발사') == 0:
            response = russian_roulette.action()
            await message.channel.send(response)

        # if you says '!날씨 (지역)', this bot scrape weather info from NAVER
        elif message.content[:3] == '!날씨':
            response = weather.check_param(message)
            await message.channel.send(response)
        
        elif message.content[:2] == '추가':
            dataset = message.content.split(';')
            print(dataset)
            if len(dataset) == 3:
                if dataset[1] in settings.BANNED_KEYWORD:
                    await message.channel.send(settings.MESSAGE_CANNOT_USE_THIS_KEYWORD)
                else:
                    connection, result_message = keyword_manager.insert_keyword(connection, cursor, str(dataset[1]), str(dataset[2]))
                    connection.commit()
                    await message.channel.send(result_message)
        
        # this block checking other static keywords
        # please check 'command/keywords.py'
        else: 
            other_response = keywords.search(connection, cursor, message)
            if other_response == settings.ERROR_SQL_CONNECTION:
                connection, cursor = sql_driver.db_init()
                other_response = keywords.search(connection, cursor, message)
            else:
                pass
            if other_response:
                await message.channel.send(other_response)
    
# run client on this line
client.run(token)
