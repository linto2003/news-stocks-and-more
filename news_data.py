from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()
options.add_argument('--headless')  # Run in headless mode (no GUI)

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Define the news categories you want to scrape
news_categories = [
    "stock India","trading India"
]

# Iterate through each topic to fetch news articles
for topic in news_categories:
    with open(f'news_titles.txt', 'a') as file:
        driver.get(f'https://www.ndtv.com/search?searchtext={topic}')
        time.sleep(2)  # Wait for the page to load

        # Find all news items based on the class name
        a_tags = driver.find_elements(By.CLASS_NAME, 'src_itm-ttl')

        if not a_tags:
            print(f"No links found for category: {topic}")
            continue

        # Iterate through each news item and extract the title
        for a in a_tags:
            try:
                # Get the title
                title = a.text
                # Write the title to the file
                file.write(f"{title}\n")  # Write each title on a new line
            except Exception as e:
                print(e)

        time.sleep(1)  # Optional: wait a moment before the next iteration

# Close the driver
driver.quit()
