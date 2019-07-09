high level scraper for myactivity.google.com

### CONCEPT
(from my blog)
I worked in previous days about integrating myactivity.google.com inside my dashboard. I am really fascinated by the amount of personal data I can find on myactivity, they will totally make my dashboard more rich and accurate. I opened a new standalone repo to implement this scarper at github.com/SolbiatiAlessandro/google_myactivity_scarper. I looked for couple of options and how to build this and I decided to use bs4 for the actual scraping and pyppetterr to run Chrome Headless. Where bs4 was kind of an obvious choice, I was not too familiar with headless browsers: you basically run chrome without the browser rendering. There is a nice library maintained by the Chrome/Chromium dudes called Puppeteer, you can run headless Chrome as a nodejs application, and the trick is that it can track your cookie sessions and automatically login into your google account to get your activity.


how to run tests:

```
python -m pytest tests
(for some reason running pytest doesn't work)
```
