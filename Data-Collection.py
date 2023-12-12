import bs4
from bs4 import BeautifulSoup
import lxml
import requests
import csv

# Getting access to the data
url_list = ['https://www.carrefour.ke/mafken/en/c/FKEN1600000', 'https://www.carrefour.ke/mafken/en/c/FKEN1660000', 'https://www.carrefour.ke/mafken/en/n/c/clp_FKEN1700000', 
            'https://www.carrefour.ke/mafken/en/n/c/clp_FKEN1500000', 'https://www.carrefour.ke/mafken/en/c/FKEN21000000', 'https://www.carrefour.ke/mafken/en/c/FKEN6000000']
# Create a CSV file to store the data
csv_filename = 'scraped_list.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)
    
    # Write headers to the CSV file
    csv_writer.writerow(['Category-of-Product', 'Name-of-Product'])

    # Scraping the HTML Contents
    for url in url_list:
        response = requests.get(url)

        if response.status_code == 200:

            

            csv_writer.writerow([url, title_content, price_content])
            print(f"Scraped data from {url}")

        else:
            print(f'Error Found while trying to access {url}. Status Code{response.status_code}')

print("Hongera, Data saved successfully!")

