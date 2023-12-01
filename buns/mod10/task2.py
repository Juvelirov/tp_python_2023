import requests
import re

def get_subheadings(link):
    response = requests.get(link)
    text_html = response.text
    regex = r'<h3.*?>(.*?)</h3>'
    subheadings = re.findall(regex, text_html)
    return subheadings

link = 'http://www.columbia.edu/~fdc/sample.text_html'
subheadings = get_subheadings(link)
print(subheadings)

