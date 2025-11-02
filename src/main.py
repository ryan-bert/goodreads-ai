import os
import pandas as pd
from utils import scrape_description

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, '../data')

def main():
    
    # Load user data from CSV
    books_df = pd.read_csv(os.path.join(DATA_DIR, 'goodreads_library_export.csv'))

    # Select and rename relevant columns
    books_df = books_df[['Book Id', 'Title', 'Author', 'Date Read', 'My Review']]
    books_df.columns = ['book_id', 'title', 'author', 'date_read', 'my_review']

    # Iterate through each book and scrape its description
    for index, row in books_df.iterrows():
        book_id = row['book_id']
        scrape_description(book_id)

if __name__ == "__main__":
    main()