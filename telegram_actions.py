import asyncio
import time

async def send_a_message(client, username, message):
    await client.send_message(username, message)

async def get_messages(client, username, total_of_sms):
    from telethon import utils
    all_sms = list()
    async for message in client.iter_messages(username, limit=total_of_sms):
        all_sms.append(message.message)
    return all_sms

async def start_action(client):
    action = input("Please, select an action:\nSend message (1)\nGet last messages (2)\nQuery (3)\nType the number of option:")
    username = 'gpt3_unlim_chatbot'
    while action not in ('1', '2', '3'):
        action = input("Please, select an action:\nSend message (1)\nGet last messages (2)\nSearch (3)\nType the number of option:")
    # try:
    if action == '1':
        sms = 'Please provide a phrase to react to this: This is a very good banana'
        await send_a_message(client, username, sms)
    elif action == '2':
        messages_limit = input('Please, type number of messages to get: ')
        while not messages_limit.isdigit():
            messages_limit = input('Please, type number of messages to get: ')
        all_sms = await get_messages(client, 'gpt3_unlim_chatbot', int(messages_limit))
        print('\n'.join([f'{item}' for i,item in enumerate(all_sms)]))
    elif action == '3':
        search = input('Please, type your question:\n')
        await send_a_message(client, username, search)
        response = await get_messages(client, 'gpt3_unlim_chatbot', 1)
        while search in response[0]:
            time.sleep(5)
            response = await get_messages(client, username, 1)
        print('\n\n------------RESPONSE--------------')
        print('\n'.join(response))
        print('------------RESPONSE--------------\n\n')


