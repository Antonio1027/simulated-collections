from bson import ObjectId


class MockInsertOneResult:
    def __init__(self, inserted_id):
        self.inserted_id = inserted_id


class MockDeleteResult:
    def __init__(self, deleted_count):
        self.deleted_count = deleted_count


class MockCollection:
    def __init__(self, initial_data=None):
        self.data = initial_data or {}

    async def find_one(self, query):
        _id = query.get("_id")
        return self.data.get(_id)

    async def find(self, query):
        cliente_id = query.get("cliente_id")
        for doc in self.data.values():
            if doc.get("cliente_id") == cliente_id:
                yield doc

    async def insert_one(self, document):
        _id = document.get("_id", "mock_id")
        self.data[ObjectId(_id)] = document
        return MockInsertOneResult(_id)

    async def update_one(self, query, update):
        _id = query.get("_id")
        if _id in self.data:
            self.data[_id].update(update.get("$set", {}))
            return None
        return None

    async def delete_one(self, query):
        _id = query.get("_id")
        if _id in self.data:
            del self.data[_id]
            return MockDeleteResult(1)
        return MockDeleteResult(0)
