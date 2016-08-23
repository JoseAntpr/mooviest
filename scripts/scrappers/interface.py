import urllib.request, json
from bs4 import BeautifulSoup

# get_soup(url), return soup
#
#   Params
#       - url, url that will scrapper
#
def get_soup(url):
    error_code = False
    error_message = ""
    soup = ""
    try:
        response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html =  urllib.request.urlopen(response).read().decode("utf8")
        soup = BeautifulSoup(html, 'html.parser')
    except:
        error_code = True
        error_message = "Error call url: "+url+"\n"

    return error_code, error_message, soup
