import asyncio
import logging
from pyppeteer import launch

async def gen_open_myactivity(screenshot_path='./screenshots/myactivity.png'):
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://myactivity.google.com')
    await page.screenshot({'path': screenshot_path})
    logging.info("screenshot inside {}".format(screenshot_path))
    await browser.close()

def screenshot_myactivity():
    logging.info("screenshotting myactivity.google.com")
    asyncio.get_event_loop().run_until_complete(gen_open_myactivity())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    screenshot_myactivity()
