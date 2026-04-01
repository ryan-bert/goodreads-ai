import os
import polars as pl
from utils import scrape_description, print_goodreads_export

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, '../data')

def main():

    # Load user data from CSV
    books_df = pl.read_csv(os.path.join(DATA_DIR, 'goodreads_library_export.csv'))

    # Format columns (lowercase, replace spaces with underscores)
    books_df = books_df.rename({col: col.lower().replace(' ', '_') for col in books_df.columns})

    # Select relevant columns
    books_df = books_df.select(['book_id', 'title', 'author', 'date_read', 'my_rating', 'my_review'])

    # Make spacing consistent (all string columns)
    books_df = books_df.with_columns(
        pl.col(col).str.replace_all(r'\s+', ' ').str.strip_chars()
        for col in books_df.columns if books_df[col].dtype == pl.Utf8
    )

    # Filter to only read books (where date_read is not null)
    books_df = books_df.filter(books_df['date_read'].is_not_null()).sort('date_read')

    # Print all read books
    print_goodreads_export(books_df)

    # Iterate through each book and scrape its description
    for row in books_df.iter_rows(named=True):
        book_id = row['book_id']
        scrape_description(book_id)

if __name__ == "__main__":
    main()