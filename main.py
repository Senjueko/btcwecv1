import json
import logging
import sys
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Firefox()

root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

URL = "https://www.nytimes.com/crosswords/game/mini"

browser.get(URL)
content = browser.page_source
soup = BeautifulSoup(content, "lxml")

ARRAY_FOR_TEXT = []

try:
    for string in soup.find_all("ol", class_="ClueList-list--2dD5- ClueList-obscured--UdyXT"):
        for litag in string.find_all('li'):
            stats = litag.text
            clue = stats[0] + ". " + stats[1:]
            ARRAY_FOR_TEXT.append(clue)
except:
    root.addHandler(handler)

ACROSS = []
DOWN = []

print("=== Across ===")
try:
    for word1 in range(int(len(ARRAY_FOR_TEXT) / 2)):
        print(ARRAY_FOR_TEXT[word1])
        ACROSS.append(ARRAY_FOR_TEXT[word1])
except:
    root.addHandler(handler)

print("=== Down ===")
try:
    for word2 in range(int(len(ARRAY_FOR_TEXT) / 2), len(ARRAY_FOR_TEXT)):
        print(ARRAY_FOR_TEXT[word2])
        DOWN.append(ARRAY_FOR_TEXT[word2])
except:
    root.addHandler(handler)

array_to_json = []  # array for writing the JSON objects

try:
    with open('btcwecv1.json', 'w', encoding="UTF-8") as json_file:

        for item in range(0, len(DOWN)):
            to_json = {"Group": "Down", "Number": ACROSS[item][0],
                       "String": ACROSS[item][3:]}  # dictionary for printing the JSON objects
            array_to_json.append(to_json)

        json.dump(array_to_json, json_file, indent=4, sort_keys=True)
        json_file.close()
except:
    root.addHandler(handler)

browser.close()
