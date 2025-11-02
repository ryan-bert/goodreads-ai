import os
import pandas as pd
from utils import scrape_description, print_goodreads_export

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, '../data')

def main():
    
    # Load user data from CSV
    books_df = pd.read_csv(os.path.join(DATA_DIR, 'goodreads_library_export.csv'))

    # Format columns (lowercase, replace spaces with underscores)
    books_df.columns = [col.lower().replace(' ', '_') for col in books_df.columns]

    # Select and rename relevant columns
    books_df = books_df[['book_id', 'title', 'author', 'date_read', 'my_rating', 'my_review']]

    # Print all read books
    print_goodreads_export(books_df)

    # Iterate through each book and scrape its description
    for index, row in books_df.iterrows():
        book_id = row['book_id']
        scrape_description(book_id)

if __name__ == "__main__":
    main()