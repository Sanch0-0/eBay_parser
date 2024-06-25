# eBay Scraper
This Python script allows you to scrape product information from eBay based on a search query. It retrieves details such as product title, price, URL, and image, and saves them to an Excel file for easy viewing and analysis.

## Usage
1) Clone the repository or download the parser.py file.

2) Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```
3) Run the parser.py script using the following command:
```
python parser.py
```
4) You will be prompted to enter a product search query. Type in your desired search term and press Enter.

5) The script will start scraping eBay for product information. It will process multiple pages of search results, with each page containing up to 50 products. The number of pages to scrape can be adjusted in the script.

Once the scraping is complete, the script will save the extracted data to an Excel file named ebay_products.xlsx.

## Configuration
You can customize the search query and the number of pages to scrape by modifying the parameters in the scrape_ebay function call within the parser.py file:
```
products = scrape_ebay(text=input("Enter a product: "), total_pages=10)
```
Replace the "Enter a product: " string with your desired search query, and adjust the total_pages parameter to specify the number of pages to scrape.

## Requirements
- Python 3.x
- Requests library
- BeautifulSoup library
- Pandas library
- XlsxWriter library
- and others...
