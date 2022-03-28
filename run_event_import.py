from sqlite3 import Date
import aiohttp
import asyncio
from datetime import datetime
import json
from utilities.timer import Timer
import logging

from event_ingestion import EventIngestionService


async def main():
    logging.basicConfig(
        filename=f"./event_import_logs/{datetime.today()}Run.log",
        level=logging.INFO,
        format="%(asctime)s:: %(message)s",
    )
    timer = Timer("Songkick Data Ingestion")
    timer.begin()

    event_service = EventIngestionService()
    await event_service.main()

    timer.stop()
    logging.info(timer.results())
    timer.reset()


if __name__ == "__main__":
    asyncio.run(main())