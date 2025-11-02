import requests
import bs4 as bs

BASE_URL = "https://www.goodreads.com"

def scrape_description(book_id):

    # Get the book page
    url = f"{BASE_URL}/book/show/{book_id}"
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, 'html.parser')

    # Extract the description
    description_div = soup.find('div', {'data-testid': 'description'})
    if description_div:
        description_spans = description_div.find_all('span')
        if len(description_spans) > 1:
            description = description_spans[1].text.strip()
        else:
            description = description_spans[0].text.strip()
    else:
        description = "No description available."

    return description

def 