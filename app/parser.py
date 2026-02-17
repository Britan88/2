import asyncio
import random
from browser import get_context
from db import save_products

SEARCH_URL = "https://www.wildberries.ru/catalog/0/search.aspx?search={query}"


async def parse_wb(query="наушники"):
    p, browser, context = await get_context()
    page = await context.new_page()

    await page.goto(SEARCH_URL.format(query=query))
    await asyncio.sleep(random.uniform(2, 4))

    for _ in range(3):
        await page.mouse.wheel(0, random.randint(300, 700))
        await asyncio.sleep(random.uniform(1, 2))

    cards = await page.query_selector_all(".product-card__wrapper")

    items = []
    for c in cards:
        try:
            title = await c.query_selector_eval(".product-card__name", "el=>el.textContent")
            price = await c.query_selector_eval(".price__lower-price", "el=>el.textContent")
            link = await c.query_selector_eval("a", "el=>el.href")

            items.append({
                "name": title.strip(),
                "price": float("".join(filter(str.isdigit, price))),
                "link": link,
            })
        except Exception:
            pass

    save_products(items)
    await context.storage_state(path="cookies.json")
    await browser.close()
    await p.stop()
