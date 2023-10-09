import asyncio
from pyrogram.client import Client
from pyrogram.errors.exceptions.unauthorized_401 import SessionPasswordNeeded


# Мой основной акк
api_id = 25679181
api_hash = "518b044d7ac96e733bdbbe23e7571146"
phone_number = "+79776756525"


async def manually_registration():
    client = Client("sadfksgsedfosdfsdlfsefkwelgflsadflasdlfalsdflasdlflasd", api_id, api_hash, in_memory=True)
    await client.connect()

    sent_code_info = await client.send_code(phone_number)    
    phone_code = input("Please enter your phone code: ")
    
    await client.sign_in(phone_number, sent_code_info.phone_code_hash, phone_code)

    print(await client.export_session_string())



asyncio.run(manually_registration())