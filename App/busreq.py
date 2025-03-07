import requests, bs4, logging


#given a stop, get next departure
#TODO
class BusFinder:
    
    
    def __init__(self, log): #needs a logger in constructor
        self.website = requests.get('https://anytrip.com.au/region/nsw?selectedStopId=au2:')
        self.busStop = ''
        self.logger = log
        
    def nextDeparture(self, input_stop):
        self.changeSelfStop(input_stop) #changes input stop
        try:
            self.website.raise_for_status()
            anyTripSoup = bs4.BeautifulSoup(self.website, 'html.parser')
            self.logger.info(type(anyTripSoup))
            
            elems = anyTripSoup.select('#atapp-root > div.ng-scope.flex-fill.d-flex.flex-column.min-h-0 > div > anytrip-live-map > div > div.d-none.d-md-flex.flex-shrink-0.anytrip-livemap-bar.d-flex > div.d-flex.flex-column.flex-fill.min-h-100.max-h-100.max-w-100.ng-scope > div:nth-child(6) > anytrip-departure-group > div > anytrip-departure-item:nth-child(1) > a > div.flex-fill.ml-1.mb-0.lh-125 > div:nth-child(2) > div:nth-child(1)')
            self.logger.info(type(elems))
            self.logger.info(len(elems))
            
            for i in elems:
                self.logger.info('elems attriubtes are: ' + elems[i].attrs)
            
            return
            
        except Exception as e:
            self.logger.error(e)
            
        
    def changeSelfStop(self, input_stop):
        #error handling here for bus stop syntax
        self.busStop = input_stop
        self.website = self.website + ''.join(self.busStop) + ''.join('&departureOffset=0')
        self.logger.info('website to request it: ' + self.website)
        return True
    
def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)

    # Create BusFinder instance
    bus_finder = BusFinder(logger)

    # Test nextDeparture method with a sample stop ID
    test_stop = "2121213"  # Replace with an actual stop ID if needed
    bus_finder.nextDeparture(test_stop)

if __name__ == "__main__":
    main()
        
        
        
            
        
    



#given a stop, get next N departures
#TODO

#given a stop, get next departure with realtime info on delay (delay value: scrape )
#TODO

#given a stop, get next N departures with realtime info on delays


#remind me at x : set a reminder to depart at x time the next day