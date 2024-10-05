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
    
    async def update_one(self, colName:str, query: dict, new_value: dict):
        col = self.db[colName]
        await col.update_one(query, {"$set": new_value})
        
    async def update_many(self, colName:str, query: dict, new_value: dict):
        col = self.db[colName]
        await col.update_many(query, {"$set": new_value})
    
    async def purgeData(self, colName, confirm=False):
        if not confirm:
            match input("Are You Sure About Clearing {colName} Collection(s) [Y, n]"):
                case "Y":
                    return await self.purgeData(colName, True)
        
        if colName == "*":
            await self.client.drop_database("data")
        
        await self.db[colName].drop()