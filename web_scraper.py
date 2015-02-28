'''
Created on Feb 27, 2015

@author: rosspa
'''
import requests

def scrape(question):
    URL = "http://j-archive.com/search.php" #?search="
    URL_END = "&submit=Search"
    ANSWER_TAG = "<span id=\"answer_1\" class=\"search_correct_response\">"
    
    params = {'search' :  question, 'submit': 'Search'}
    response = requests.get(URL, params=params)
    html = response.text
    part = html[html.find(ANSWER_TAG)+len(ANSWER_TAG):]
    answer = part[1:part.find("</span>")]
# jehl
#     print response.url + "\n"
#     print response.text
#     print "answer = *" + answer + "*"
    if answer.startswith("ttp://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd\">"):
        print "No answer found for the question \""  + question + "\""
        raise Exception("No answer found for the question \""  + question + "\"")
    return "What is " + answer + "?"
    