Data Scraping Assignment
1. Classwork_Data_Scrapping_wikipedia_indianaircraft.py
Description
This script scrapes data from a Wikipedia page listing active Indian military aircraft. It extracts details from the first table on the page and saves them into a CSV file.

Functionality
Sends an HTTP GET request to the Wikipedia page.
Parses HTML content to locate the first table with the wikitable class.
Extracts table headers and rows.
Saves the data to a CSV file.
Modules Used
requests: For sending HTTP requests.
bs4 (BeautifulSoup): For parsing HTML content.
csv: For writing data to a CSV file.
Output
File: indian_military_aircraft.csv
Columns: Headers from the Wikipedia table (e.g., Aircraft, Origin, etc.).

