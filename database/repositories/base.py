from database.connector import db


class BaseRepository:
    def __init__(self, collection_name: str):
        self.collection = db[collection_name]
