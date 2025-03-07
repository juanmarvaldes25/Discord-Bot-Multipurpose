import requests, bs4, logging


#given a stop, get next departure
#TODO

    
    
class BusFinder:
     
        
     def __init__(self, log):
        self.base_url = "https://anytrip.com.au/region/nsw?selectedStopId=au2:"
        self.busStop = ''
        self.logger = log

     def nextDeparture(self, input_stop):
         #TODO
        try:
         self.changeSelfStop(input_stop)  # Update stop
         url = self.base_url + self.busStop + "&departureOffset=0&departureLimit=25" # Build the new URL 
         
         
         
        except Exception as e:
         self.logger.error(f'{e} in function nextDeparture')
            

       
            

#TODO : error handling and input verification
     def changeSelfStop(self, input_stop):
        if not input_stop.isnumeric() and len(input_stop) != 7:
            raise TypeError("input not numeric")
            return
        self.busStop = input_stop
    
def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)

    # ✅ Pass the logger when creating BusFinder
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