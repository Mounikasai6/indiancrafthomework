import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page for active Indian military aircraft
url = "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"

# Fetch the webpage content
response = requests.get(url)
a = response.content
soup = BeautifulSoup(a, 'html.parser')

# Locate the first table with the class 'wikitable'
table = soup.find(class_='wikitable')

if table:
    # Extract the header row
    headers = [header.text.strip() for header in table.find_all('th')[:6]]

    # Extract all rows in the table
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all(['td', 'th'])  # Include both <td> and <th> cells
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)

    # Save the table data to a CSV file
    with open('indian_military_aircraft.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the headers
        csvwriter.writerow(headers)
        # Write the rows
        csvwriter.writerows(rows)

    # Print the data
    print("Table extracted and saved to 'indian_military_aircraft.csv'.")
    print("Preview:")
    print(headers)
    for row in rows[:5]:  # Preview the first 5 rows
        print(row)

else:
    print("Table not found!")