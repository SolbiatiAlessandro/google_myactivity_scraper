import asyncio
import logging
from pyppeteer import launch

async def gen_open_myactivity(screenshot_path='./screenshots/myactivity.png'):
    browser = await launch(
            {
                'executablePath':'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                'userDataDir':'./ChromeProfile',
                'headless':'false'
                }
            )
    page = await browser.newPage()
    # <a class="WpHeLc" href="https://accounts.google.com/ServiceLogin?hl=en-GB&amp;continue=https://myactivity.google.com/" aria-label="Sign In" jsname="hSRGPd"></a>
    #await page.goto('https://accounts.google.com/ServiceLogin?hl=en-GB&amp;continue=https://myactivity.google.com/')
    await page.goto('https://stackoverflow.com/')
    await page.screenshot({'path': screenshot_path})
    logging.info("screenshot inside {}".format(screenshot_path))
    await browser.close()

def screenshot_myactivity():
    logging.info("screenshotting myactivity.google.com")
    asyncio.get_event_loop().run_until_complete(gen_open_myactivity())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    screenshot_myactivity()
