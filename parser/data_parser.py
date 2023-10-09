import logging

from pyrogram.client import Client
from pyrogram.types import Message


IMAGES_PATH = 'images'
VIDEOS_PATH = 'videos'
CAPTIONS_PATH = 'captions'


class DataParser:
    def __init__(self, chat_id: str):
        self.chat_id: str = chat_id

    async def parse(self, session_string: str) -> str:
        async with Client("pasre_session", session_string=session_string) as client:

            async for message in client.get_chat_history(self.chat_id):

                if message.from_user.username == self.chat_id:
                    
                    if message.photo is not None:
                        await self.download_image(message)

                    if message.video is not None:               
                        await self.download_video(message)
                    
                    if message.caption is not None:               
                        await self.download_caption(message)
            
            return await client.export_session_string()

    @staticmethod
    async def download_image(message: Message):
        file_name = f"{IMAGES_PATH}/{message.photo.file_unique_id}"
        await message.download(file_name)
        logging.warning(f"Изображение скачано - {file_name}")

    @staticmethod
    async def download_video(message: Message):
        file_name = f"{VIDEOS_PATH}/{message.video.file_unique_id}"
        await message.download(file_name)
        logging.warning(f"Видео скачано - {file_name}")

    @staticmethod
    async def download_caption(message: Message):
        file_name = f"{CAPTIONS_PATH}/{message.id}.txt"
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(message.caption)
            logging.warning(f"Текст скачан - {file_name}")