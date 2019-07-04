import pytest
import os
from google_myactivity_parser import Parser

def test_parser():
    try:
        htmlpage = open("testpage.html","r").read()
    except:
        htmlpage = open("tests/testpage.html","r").read()
    parser = Parser(htmlpage)
    cards = parser.get_cards()
    assert len(cards) > 0
