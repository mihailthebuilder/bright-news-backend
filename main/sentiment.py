"""Function which calculates how positive a website's content is. Scores usually range between -10 and +10"""
import re
import requests
from bs4 import BeautifulSoup as bs
from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_analyze(url):
    """calculates a website's positivity"""

    # add https if not in there at start
    if url[0:8] != "https://" and url[0:7] != "http://":
        url = "https://" + url

    try:
        my_session = requests.session()
        for_cookies = requests.get(url, timeout=5).cookies
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
        }

        response = my_session.get(url, headers=headers, cookies=for_cookies, timeout=5)

        # process text into list of text pieces
        processed_li = process_request(response.text)

        # list which will hold the pieces of text together with their scores
        text_li = []

        # Initialise the 2 sentiment analysis libraries used
        afinn = Afinn()
        analyzer = SentimentIntensityAnalyzer()

        for text in processed_li:

            afinn_score = afinn.score(text)  # usually from -5 to +5
            vader_score = analyzer.polarity_scores(text)["compound"]  # from -1 to +1

            text_dict = {
                "text": text,
                "model1_score": vader_score,
                "model2_score": afinn_score,
            }

            # only consider text pieces when 2 conditions are met
            # 1) at least one non-negative sentiment score
            # 2) both scores of the same sign
            combined_score = 0
            if (afinn_score != 0 or vader_score != 0) and (
                afinn_score * vader_score >= 0
            ):
                if afinn_score > 0 or vader_score > 0:
                    combined_score = 1
                else:
                    combined_score = -1

            text_dict["combined_score"] = combined_score
            text_li.append(text_dict)

        output = {"raw_data": text_li}

        nonzero_text_count = len(
            [text_elem for text_elem in text_li if text_elem["combined_score"] != 0]
        )

        if nonzero_text_count == 0:
            output.update(
                {
                    "success": False,
                    "message": "Unable to calculate any scores.",
                }
            )

        else:

            positive_text_count = len(
                [text_elem for text_elem in text_li if text_elem["combined_score"] > 0]
            )

            output.update(
                {
                    "success": True,
                    "url_analyzed": re.sub(r"^(https://|http://)?(www\.)?|/$", "", url),
                    "score": positive_text_count / nonzero_text_count,
                }
            )

        return output

    # catch errors in requests.get statement
    except requests.exceptions.ConnectionError as error:
        return {
            "success": False,
            "message": f"An error occurred when trying to access the '{url}' URL. Error message: '{error}'",
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Something went wrong when processing the '{url}' URL.Error message: '{error}'",
        }


def process_request(response_text):

    # get the individual text pieces inside the web page as separate list elements
    soup_li = bs(response_text, "lxml").body.get_text(separator="||").split("||")

    # process each text pieces
    transformed_li = [text_transform(x) for x in soup_li]

    # filter irrelevant text pieces
    filtered_li = [x for x in transformed_li if text_filter(x)]

    # remove duplicates
    unique_li = list(set(filtered_li))

    processed_li = unique_li

    return processed_li


def text_filter(text_input):
    output = len(text_input.split()) >= 4

    reg_test = r"cookie|newsletter|copyright|trademark|mailing list|subscribe|sign up|rights reserved|this site"
    reg_result = re.search(reg_test, text_input, re.IGNORECASE)

    output = output and not (reg_result)

    return output


def text_transform(text_input):
    encoded_text = text_input.encode("ascii", "ignore")
    decoded_text = encoded_text.decode("unicode_escape")
    stripped_text = re.sub(
        r"\r|\n|\t| \(link opens in a new browser window\)", "", decoded_text
    )
    output = stripped_text
    return output