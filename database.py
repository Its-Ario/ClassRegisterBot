import motor.motor_asyncio

class Database:
    def __init__(self) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
        self.db = self.client["data"]
    
    async def insert_one(self, colName: str, data: dict):
        col = self.db[colName]
        await col.insert_one(data)
    
    async def insert_many(self, colName: str, data: list[dict]):
        col = self.db[colName]
        await col.insert_many(data)
        
    async def find_one(self, colName: str, query: dict = {}):
        col = self.db[colName]
        return await col.find_one(query)
    
    async def find_all(self, colName: str, query: dict = {}):
        col = self.db[colName]
        cursor = col.find(query)
        return await cursor.to_list(length=None)
