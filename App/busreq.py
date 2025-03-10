import requests, bs4, logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4

class BusFinder:
    
    #selenium setup
     
     
        
     def __init__(self, log):
        self.base_url = "https://anytrip.com.au/region/nsw?selectedStopId=au2:"
        self.busStop = ''
        self.logger = log
        self.firefox_options = Options()
        self.firefox_options.add_argument("--headless")
        self.geckodriver_path = "C:\\Program Files\\geckodriver.exe"
        self.s = Service(self.geckodriver_path)
        self.driver = webdriver.Firefox(service=self.s, options = self.firefox_options)
     
     def verifyDepartureN(self, n):
         if str(n).isnumeric() and (int(n) <= 50) and int(n) >= 1:
             return True
         raise TypeError("Number of departures is not numeric or not in range 1-50")
        
          
     def nextDeparture(self, input_stop, n = '25'):
        payload = []
        try:
         self.changeSelfStop(input_stop)  # Update stop
         self.verifyDepartureN(n)
         url = self.buildURL(self.busStop, n) # Build the new URL 
         self.logger.info(f'the URL is {url}')
         
         #selenium
         busSoup = self.seleniumSetup(url, 'text-small.departure-time.ng-binding')
         elements = busSoup.select('.flex-shrink-0.ng-scope.ng-isolate-scope') 
         
         for elem in elements:
             bus_no = elem.find('strong', class_ = 'ng-binding')
             print(bus_no.get_text(strip=True))
             
             bus_name = elem.find('strong', class_ = 'text-gray-dark ng-binding')
             print(bus_name.get_text(strip=True))
             
             
             time = elem.find('div', class_='text-small departure-time ng-binding')
             print(time.get_text(strip=True))
             
             #if early  or on time
             
             span_existent_toPayload = busSoup.new_tag("span", **{"class": "text-info ng-binding ng-scope"})
             span_existent_toPayload.string = "timetabled"
             
             span = elem.find('span', class_="text-success ng-scope")
             if not span == None:
                 print(span.get_text(strip=True))
                 span_existent_toPayload = span
                 
             early_span = elem.find('span', class_= "text-info ng-binding ng-scope")
             if not early_span == None:
                 print(early_span.get_text(strip=True))
                 span_existent_toPayload = early_span
                 
             late_span = elem.find('span', class_= "text-danger ng-binding ng-scope")
             if not late_span == None:
                 print(late_span.get_text(strip=True))
                 span_existent_toPayload = late_span
                 
             
                 
             print('------')
            
             payload.append(bus_no.get_text(strip=True) +' ' + bus_name.get_text(strip=True) + '' +  time.get_text(strip=True) +' '+ span_existent_toPayload.get_text(strip=True) + ' | ' )
          
          
         
         self.driver.quit()
         print(payload)
         return payload
         
        except Exception as e:
         self.logger.error(f'{e} in function nextDeparture')
         data = []
         return data
     
     def seleniumSetup(self, input_url, class_for_driver): #only use classname in EC.presence_of_element_located, returns BeautifulSoup Object
        self.driver.get(input_url)
        wait = WebDriverWait(self.driver, 7)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_for_driver)))
        page_source = self.driver.page_source
        busSoup = bs4.BeautifulSoup(page_source, 'html.parser')
        return busSoup
        
    
     def getStationName(self, input_stop): #get the name of the station
        payload = ''
        try:
   
         self.changeSelfStop(input_stop)  # Update stop
         url = self.buildURL(self.busStop) # Build the new URL 
         self.logger.info(f'the URL is {url}')
         
         #selenium
         busSoup = self.seleniumSetup(url, 'text-small.departure-time.ng-binding')
         searcher = busSoup.select('#atapp-root > div.ng-scope.flex-fill.d-flex.flex-column.min-h-0 > div > anytrip-live-map > div > div.d-none.d-md-flex.flex-shrink-0.anytrip-livemap-bar.d-flex.anytrip-livemap-bar-expanded > div.d-flex.flex-column.flex-fill.min-h-100.max-h-100.max-w-100.ng-scope > div:nth-child(1)') 
         nameElem = searcher[0].find('div', class_= 'text-small text-truncate ng-binding')
         
         if nameElem:
             station_name = nameElem.get_text(strip=True)
             payload + station_name
             print("Station name:", station_name)
         else:
             print("Element not found.") 
            
         return payload
            
            
        except Exception as e:
            self.logger.error(f'{e}')
        
     
     def getNextStop(self): #TODO
         payload =''
         
     
     def buildURL(self, stationID, n = '25'):
        return self.base_url + stationID + "&departureOffset=0&departureLimit=" + str(n)
     
        
     def changeSelfStop(self, input_stop):
        if not input_stop.isnumeric() or len(input_stop) > 7 or len(input_stop) < 6:
            raise TypeError("input not numeric")
            
        else: 
            self.busStop = input_stop
        
    
    
def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)

    # ✅ Pass the logger when creating BusFinder
    bus_finder = BusFinder(logger)

    # Test nextDeparture method with a sample stop ID
    test_stop = "212110"  # Replace with an actual stop ID if needed
    bus_finder.nextDeparture(test_stop)
    #bus_finder.getStationName(test_stop)

if __name__ == "__main__":
    main()
        
        
        
            
        
    



