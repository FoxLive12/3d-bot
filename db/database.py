import os
from tortoise import Tortoise

async def init_db():
    os.makedirs("data", exist_ok=True)
    
    await Tortoise.init(
        db_url="sqlite://data/bot.db",
        modules={"models": ["db.models"]}
    )
    await Tortoise.generate_schemas()