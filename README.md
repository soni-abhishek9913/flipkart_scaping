# flipkart_scaping
This project is a web scraping script built using Selenium, BeautifulSoup, and Pandas to extract mobile phone details from Flipkart under ₹50,000.
It automates browsing, collects product information across multiple pages, and saves the results into a structured CSV file for further analysis.
 Features
- Scrapes 10 pages of Flipkart search results for mobiles under ₹50,000.
- Extracts key details:
- Name
- Price
- Rating
- Description
- Stores data in a CSV file (1flipkart_all_pages.csv) for easy analysis.
- Uses Selenium for browser automation and BeautifulSoup for HTML parsing.
- Implements delays (time.sleep) to ensure pages load properly before scraping

The final dataset is saved as:
flipkart_all_pages.csv


with columns:
- Name
- Price
- Rating
- Description

