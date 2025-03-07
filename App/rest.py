from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")

# Specify the path to GeckoDriver
geckodriver_path = "C:\\Program Files\\geckodriver.exe"

# Set up the Firefox WebDriver
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open the webpage
driver.get('https://anytrip.com.au/region/nsw?selectedStopId=au2:2121213&departureOffset=0&departureLimit=40')

# Wait for the element to be present (explicit wait)
wait = WebDriverWait(driver, 5)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'text-small.departure-time.ng-binding')))

# After the content has loaded, get the page source
page_source = driver.page_source

# Parse the HTML using BeautifulSoup
anyTripSoup = bs4.BeautifulSoup(page_source, 'html.parser')

# Select the desired element
elems = anyTripSoup.select('.text-small.departure-time.ng-binding')

print(f'Found {len(elems)} departure time(s)')

# Print out the text content of the selected element(s)
for elem in elems:
    #TODO: If repeated, don't print or add or whatever you wanna do
    print(elem.get_text(strip=True))

# Close the browser
driver.quit()