# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Lists to store data
products = []
prices = []
ratings = []

# Scraping Jumia website
url = "https://www.jumia.co.ke/phones-tablets/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Loop through each product on the page
for each in soup.find_all('a', class_='core'):
    name = each.find('div', class_='name')
    price = each.find('div', class_='prc')
    rate = each.find('div', class_='rev')

    # Caters for instances where the name does not exist
    if name is None:
        products.append(None)
    else:
        products.append(name.text)

    # Caters for instances where the price does not exist
    if price is None:
        prices.append(None)
    else:
        prices.append(price.text)

    # Caters for instances where the rating does not exist
    if rate is None:
        ratings.append("None")
    else:
        ratings.append(rate.text)

# Structuring and storing data in a DataFrame
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})

# Output the DataFrame to CSV file
df.to_csv('products.csv', index=False)

# Data visualization
df2 = pd.read_csv("products.csv")

# Convert 'Rating' column to string type to handle "None" values
df2['Rating'] = df2['Rating'].astype(str)

# Plotting the scatter plot for Rating against Price
plt.xlabel("Rating")
plt.ylabel("Price")
plt.title("Rating against Price")
plt.scatter(df2['Rating'], df2['Price'], marker="*", c='purple', alpha=1)
plt.show()