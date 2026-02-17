import os
import random
from playwright.async_api import async_playwright
from config import PROXIES


async def get_context():
    proxy = random.choice(PROXIES)

    p = await async_playwright().start()
    browser = await p.chromium.launch(
        headless=True,
        proxy={"server": proxy} if proxy else None,
    )

    context = await browser.new_context(
        locale="ru-RU",
        storage_state="cookies.json" if os.path.exists("cookies.json") else None,
        user_agent=random.choice(
            [
                "Mozilla/5.0 (Linux; Android 13)",
                "Mozilla/5.0 (iPhone)",
            ]
        ),
    )

    return p, browser, context
