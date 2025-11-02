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

def print_goodreads_export(books_df):

    # Filter for already read books
    books_df = books_df[books_df['date_read'].notnull()]

    # Sort by date read descending
    books_df = books_df.sort_values(by='date_read', ascending=False)
    
    # Iterate through over each book
    for index, row in books_df.iterrows():
        
        # Extract and print basic info
        print(f"Title: {row['title']}")
        print(f"Author: {row['author']}")
        print(f"Date Read: {row['date_read']}")
        print(f"My Rating: {row['my_rating']}/5")
        print(f"My Review: {row['my_review']}")
        print("-" * 40)