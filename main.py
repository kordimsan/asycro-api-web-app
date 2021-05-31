from fastapi import FastAPI, BackgroundTasks, Path
import asyncio
from threading import Thread, Lock

from worker import Worker

app = FastAPI()
worker = Worker()

Thread(target=worker.run_worker).start()

@app.get("/add")
async def add_item(
    background_tasks: BackgroundTasks, 
    num: int = Path(..., title="The num might be positive integer", ge=0, le=1000), 
    timeout: int = Path(5, title="The num might be in seconds", ge=0, le=1000)
):
    background_tasks.add_task(worker.add_task, num, timeout)
    return {"message": "task has added"}

@app.get("/list")
async def show_list():
    return worker._list

@app.get("/queue")
async def show_queue():
    return worker._queue