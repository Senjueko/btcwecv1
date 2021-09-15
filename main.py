import json
import logging
from selenium import webdriver

logging.basicConfig(filename="btcwecv1.log",level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
browser = webdriver.Firefox()

URL = "https://www.nytimes.com/crosswords/game/mini"

browser.get(URL)

elements = browser.find_element_by_css_selector(".Layout-clueLists--10_Xl")
ACROSS = ""
DOWN = ""

for word1 in elements.text.split("DOWN")[0]:
    ACROSS += word1
for word2 in elements.text.split("DOWN")[1]:
    DOWN += word2


numberList = []
stringList = []

def printer(direction,number_list,string_list):
    """Function for print specific clue's side (across or down)"""

    for word in direction.splitlines():
        if word.isdigit():
            number_list.append(int(word))
        else:
            string_list.append(word)
    for i in range(0, len(number_list)):
        print(str(number_list[i]) + ". " + string_list[i + 1])
        logging.info(str(number_list[i]) + ". " + string_list[i + 1])


print("=== Across ===")
printer(ACROSS,numberList,stringList)
numberList.clear()
stringList.clear()
print("=== Down ===")
printer(DOWN,numberList,stringList)


array_to_json = [] # array for writing the JSON objects

with open('btcwecv1.json', 'w',encoding="UTF-8") as json_file:

    for item in range(0, len(numberList)):
        to_json = {"Group": "Down", "Number": numberList[item],
                   "String": stringList[item + 1]}  # dictionary for printing the JSON objects
        array_to_json.append(to_json)
        logging.info(array_to_json)

    json.dump(array_to_json, json_file, indent=4,sort_keys=True)
    json_file.close()

browser.close()
