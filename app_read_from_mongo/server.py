import os

from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from dotenv import load_dotenv
from get_data_from_mongo import Get_data
load_dotenv()

app = FastAPI()

print("is connected")


@app.get("/read_from_mongo")
def read_from_mongo():
    try:
        collection_list = [os.getenv("TOPIC_TO_MONGO_ANTI"),os.getenv("TOPIC_TO_MONGO_NOT_ANTI")]
        all_data = {}
        for collection in collection_list:
                mongo_reader = Get_data(collection)
                all_data[collection] = list(mongo_reader.col.find({}, {"_id": 0}))
        return {"ok": True,"ik": all_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8008)