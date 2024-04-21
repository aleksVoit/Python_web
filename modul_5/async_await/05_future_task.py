import asyncio
from time import sleep, time
from faker import Faker
from timing import async_timed

fake = Faker("uk-UA")


# Awaitable -> Coroutine
# Awaitable -> Future -> Task


async def async_get_user_fm_db(uuid: int, future: asyncio.Future):
    await asyncio.sleep(0.5)
    future.set_result({"id": uuid, "username": fake.user_name(), "email": fake.email()})


def make_request(uuid: int) -> asyncio.Future:
    future = asyncio.Future()
    asyncio.create_task(async_get_user_fm_db(uuid, future))
    return future


@async_timed("test future")
async def main():
    users = []
    for i in range(1, 6):
        users.append(make_request(i))
    print([user.done() for user in users])
    result = await asyncio.gather(*users)
    print([user.done() for user in users])
    return result


if __name__ == "__main__":

    start = time()
    users = asyncio.run(main())
    # run() - performs next 3 lines
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # users = loop.run_until_complete(main())
    print(users)