import asyncio
import logging
import os
from pyppeteer import launch

async def gen_open_myactivity(
        screenshot_path='./screenshots/myactivity.png',
        user_data_dir='./ChromeProfile'):
    valid_dir = os.path.isdir(user_data_dir)
    logging.warning("os.path.isdir({}) = {}".format(user_data_dir, valid_dir))
    browser = await launch(
            {
                #'executablePath':'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                'userDataDir':user_data_dir,
                'headless':'false'
                }
            )
    page = await browser.newPage()
    await page.goto('https://myactivity.google.com/')
    # <a class="WpHeLc" href="https://accounts.google.com/ServiceLogin?hl=en-GB&amp;continue=https://myactivity.google.com/" aria-label="Sign In" jsname="hSRGPd"></a>
    #await page.goto('https://accounts.google.com/ServiceLogin?hl=en-GB&amp;continue=https://myactivity.google.com/')
    #await page.goto('https://stackoverflow.com/')
    await page.screenshot({'path': screenshot_path})
    logging.info("screenshot inside {}".format(screenshot_path))
    await browser.close()

def screenshot_myactivity():
    user_data_dir = "./../../../../Application Support/Google/Chrome/Default"
    logging.info("screenshotting myactivity.google.com")
    asyncio.get_event_loop().run_until_complete(
            gen_open_myactivity(
                user_data_dir=user_data_dir
                ))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    screenshot_myactivity(
            )
