import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    citation_count = len(citations_needed)
    
    print(citation_count)
    return citation_count



def parse(markup):
    soup = BeautifulSoup(markup, "html.parser")
    
    cn = soup.find_all(class_="noprint Inline-Template Template-Fact")



    for c in cn:
        paragraph = c.parent
        print(f"Citation is needed for: {paragraph.text}")



if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Battle_of_Thermopylae"
    response = requests.get(url)
    results = parse(response.text)


get_citations_needed_count(url)
parse(url)

