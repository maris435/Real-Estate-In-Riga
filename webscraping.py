import requests
import bs4
import re
from geopy import Nominatim
import csv
from tqdm import tqdm

# Set the initial page number
page = 1

# Create an empty list to store the extracted listings
listings = []

# Iterate over the pages until the desired page number (in my example, the site had 171 pages
while page < 172:

    # Display progress bar
    progress_bar = tqdm(total=172, desc='Progress', unit='page')
    progress_bar.update(page - 1)
    progress_bar.close()

    # Construct the URL for the current page
    scrape_page = 'https://www.ss.lv/lv/real-estate/flats/riga/all/'
    res_text = f'{scrape_page}page{str(page)}.html'

    # Initialize the geocoder
    locator = Nominatim(user_agent='myGeocoder')

    # Send a GET request to the URL and parse the HTML response
    res = requests.get(res_text)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    all_rows = soup.select('tr')

    # Iterate over each listing in a page
    for index, row in enumerate(all_rows):
        # Extract information from each listing
        listing = {}
        # Extract information from each listing
        try:
            initial_address = row.select('td:nth-child(4)')[0]
            address_parts = re.split(r'<br\s*\/?>', str(initial_address))
            listing['district'] = re.sub(r'<.*?>', '', address_parts[0])
            listing['address'] = re.sub(r'<.*?>', '', address_parts[1])
            listing['room_count'] = row.select('td:nth-child(5)')[0].text
            listing['area'] = row.select('td:nth-child(6)')[0].text
            listing['floors'] = row.select('td:nth-child(7)')[0].text
            listing['house_type'] = row.select('td:nth-child(8)')[0].text
            listing['price'] = row.select('td:nth-child(9)')[0].text

            # Geocode the address to get latitude and longitude
            location = locator.geocode(f"{listing['address']}, {listing['district']}")
            if location:
                listing['latitude'] = location.latitude
                listing['longitude'] = location.longitude

            # Add the listing to the list
            listings.append(listing)
        except:
            continue


    print(len(listings))

    # go to next page
    page += 1


# Save the listings to a CSV file
keys = listings[0].keys()
with open('riga_housing_11062023.csv', 'w', newline='', encoding='utf-8') as file:

    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(listings)
