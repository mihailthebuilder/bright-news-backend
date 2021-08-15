"""website -> text tokens"""
import re
import requests
from bs4 import BeautifulSoup as bs


def request(url):
    """sends a request to the URL"""

    # add https if not in there at start
    if url[0:8] != "https://" and url[0:7] != "http://":
        url = "https://" + url

    my_session = requests.session()
    for_cookies = requests.get(url, timeout=5).cookies
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
    }

    return my_session.get(url, headers=headers, cookies=for_cookies, timeout=5)


def process(site_text):
    """html text -> tokens"""

    # get the individual text pieces inside the web page as separate list elements
    soup_li = bs(site_text, "lxml").body.get_text(separator="||").split("||")

    # process each text pieces
    transformed_li = [text_transform(x) for x in soup_li]

    # filter irrelevant text pieces
    filtered_li = [x for x in transformed_li if text_filter(x, transformed_li)]

    # remove duplicates
    unique_li = list(set(filtered_li))

    processed_li = unique_li

    return processed_li


def text_filter(text_input, text_li):
    # only consider phrases that have at least 5 words
    long_enough = len(text_input.split()) >= 5

    # remove site generic text by looking at specific keywords they use
    reg_test = r"cookie|newsletter|copyright|trademark|mailing list|subscribe|sign up|rights reserved|this site"
    generic = re.search(reg_test, text_input, re.IGNORECASE)

    # remove text that's included in another piece of text
    copy = False
    for text in text_li:
        if text_input in text:
            copy = True
            break

    return long_enough and not (generic or copy)

def text_transform(text_input):
    encoded_text = text_input.encode("ascii", "ignore")
    decoded_text = encoded_text.decode("unicode_escape")
    stripped_text = re.sub(
        r"\r|\n|\t| \(link opens in a new browser window\)", "", decoded_text
    )
    output = stripped_text
    return output
