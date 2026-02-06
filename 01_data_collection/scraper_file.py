import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

class ImmowebScraper:
    """
    A scraper class to extract property URLs and their details from Immoweb.
    """

    def __init__(self, pages):
        # List to store base URLs for scraping
        self.urls_list = []
        self.pages = pages
        
        # List to store individual property URLs
        self.immoweb_url = []
        
        # List to store scraped property attributes
        self.features = []
        
        # HTTP headers to mimic a browser request
        self.headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) '
                'Gecko/20100101 Firefox/115.0'
            ),
            'Accept': (
                'text/html,application/xhtml+xml,application/xml;q=0.9,'
                'image/avif,image/webp,*/*;q=0.8'
            ),
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
        }

    # ------------------------------
    # Generate Base URLs for Scraping
    # ------------------------------
    def get_urls_list(self):
        """
        Generates base URLs for houses and apartments for the specified number of pages.
        """
        for i in range(1, self.pages + 1):
            url_house = f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={i}"
            url_apartment = f"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page={i}"
            self.urls_list.append(url_house)
            self.urls_list.append(url_apartment)
        
        print(f'Number of Base URLs generated: {len(self.urls_list)}')
        return self.urls_list

    # ------------------------------
    # Scrape Individual Property URLs from a Page
    # ------------------------------
    def immoweb_url_list(self, url):
        """
        Scrapes all property URLs from a given page URL.
        """
        time.sleep(0.1)  # Small delay to avoid overwhelming the server
        lst = []
        try:    
            response = requests.get(url, headers=self.headers)
            content = response.content
            soup = BeautifulSoup(content, "html.parser")
            
            # Find property links (excluding new real estate projects)
            for tag in soup.find_all("a", attrs={"class": "card__title-link"}):
                href = tag.get("href")
                if "new-real-estate-project" not in href:
                    lst.append(href)
        except Exception as e:
            print(f"Error occurred: {e}")
        
        return lst

    # ------------------------------
    # Scrape All Property URLs Using Threads
    # ------------------------------
    def immoweb_url_thread(self):
        """
        Scrapes all property URLs from the base URLs concurrently using threads.
        Saves the results to 'immoweb_url_file.csv'.
        """
        with ThreadPoolExecutor(max_workers=9) as executor:
            results = executor.map(lambda url: self.immoweb_url_list(url), self.urls_list)
            for result in results:
                self.immoweb_url.extend(result)
        
        print(self.immoweb_url)
        df = pd.DataFrame({"immoweb_url": self.immoweb_url})
        df.to_csv("immoweb_url_file.csv", index=False)
        print("URLs saved to 'immoweb_url_file.csv'")
        return self.immoweb_url

    # ------------------------------
    # Scrape Property Attributes from a URL
    # ------------------------------
    def get_attribute_value(self, url):
        """
        Scrapes property attributes (key-value pairs) from an individual property URL.
        """
        dictionary = {}
        try:    
            response = requests.get(url, headers=self.headers)
            print(response.status_code)
            content = response.content
            soup = BeautifulSoup(content, "html.parser")
            
            # Extract table rows containing property attributes
            tr_tag = soup.find_all("tr", attrs={"class":"classified-table__row"})
            print(tr_tag)
        except Exception as e:
            print(e)
        
        try:    
            for tag in tr_tag:
                th_tag = tag.find("th")
                td_tag = tag.find("td")
                
                header_name = th_tag.get_text(strip=True)
                header_data = td_tag.get_text(strip=True)
                
                print("__________________________")
                print(f"HEADER NAME: {header_name}")
                print(f"HEADER DATA: {header_data}")
                dictionary[header_name] = header_data
        except Exception as e:
            print(f"Error processing attributes: {e}")
        
        return dictionary

    # ------------------------------
    # Scrape Attributes for All URLs Using Threads
    # ------------------------------
    def thread_for_attrvalue(self):
        """
        Scrapes property attributes for all URLs in 'immoweb_url_file.csv' concurrently.
        Saves the results to 'dataset_file.csv'.
        """
        X = pd.read_csv("./immoweb_url_file.csv")
        self.immoweb_url = X["immoweb_url"][:1].to_list()  # currently using only first URL for testing
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(lambda url: self.get_attribute_value(url), self.immoweb_url)
            try:    
                for result in results:
                    self.features.append(result)
            except:
                pass
        
        print(self.features)
        df1 = pd.DataFrame(self.features)
        df1.to_csv("dataset_file.csv", index=False)
        print("Scraped dataset saved to 'dataset_file.csv'")
        return self.features
