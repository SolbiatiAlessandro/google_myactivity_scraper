from bs4 import BeautifulSoup as bs
import logging
import uuid

class Parser():
    """
    high level parser for https://myactivity.google.com/item
    """
    def __init__(self, htmlpage):
        self.bs = bs(htmlpage, "html.parser")

        self.cards = {}
        html_cards = self.bs.findAll("md-card-content")
        logging.info("parsing cards..")
        for i, html_card in enumerate(html_cards):
            try:
                if i % 100 == 0: logging.info("parsing card {}".format(i))
                card = {}
                card_id = uuid.uuid4()
                card['uuid'] = str(card_id)
                def clean_string(s): 
                    s = s.replace('     ','').replace('\n','')
                    start, end = 0, -1
                    for char in s:
                        if char != ' ': break
                        start += 1
                    for char in s[::-1]:
                        if char != ' ': break
                        end += 1
                    return s[start:end]
                html_header = html_card.findAll(
                        "div", 
                        {"class": "fp-display-item-header"})[0]
                html_header_title = html_header.findAll(
                        "div", 
                        {"class": "fp-display-item-title"})[0]
                # html_header_title.text >> u'\n        Maps\n      '
                context = clean_string(html_header_title.text)
                # context is the website/app name where action was taken
                card['context'] = context

                # html_action >>> u'   Viewed area around London\n          \n\n'
                html_action = html_card.findAll(
                        "h4", 
                        {"ng-if": "::!detailsItem"})[0]
                action_name = clean_string(html_action.text)
                card['action_name'] = action_name

                html_hour = html_card.findAll(
                        "span", 
                        {"ng-if": "::!summaryItem"})[0]
                action_time = html_hour.text
                card['action_time'] = action_time

                html_link = html_card.findAll(
                        "h4", 
                        {"ng-if": "::!detailsItem"}
                        )[0].findAll("a")[0]
                card['action_link'] = html_link['href']

                self.cards[str(card_id)] = card
            except Exception as e:
                logging.info("couldn't read card {}".format(i))
                logging.info(e)

    def get_cards(self):
        return self.cards
