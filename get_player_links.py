import pandas as pd
from selenium import webdriver

""" ΓΙΑ ΝΑ ΠΑΤΗΘΕΙ ΤΟ LOAD MORE ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΓΙΝΕΙ ΜΕ ΤΗΝ BEAUTIFULSOUP ΟΠΟΤΕ ΘΑ ΧΡΗΣΙΜΟΠΟΙΗΣΩ ΤΗΝ
ΒΙΒΛΙΟΘΗΚΗ SELENIUM """

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from random import randint

from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions


def random_time(start , end):
    return randint(start,end)

def open_page(homepage_url):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito') #Ανοιγει incognito για να μην κραταει το ιστορικο
    options.add_argument('--headless') #Δεν φαινεται το ανοιχτο παραθυρο
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options = options)
    
    driver.get(homepage_url)
    
    return driver


def load_more(driver = open_page("https://fminside.net/players")):    
    """ Στο load more μετα απο καποιες επαναληψεις εβγαζε σφαλμα οτι δεν βρεθηκε το κουμπι loadmore
        επειδη ουσιαστικα οταν το εψαχνε δεν ειχε φορτωθει ακομα στο DOM. Για αυτο χρησιμοποιω την
        WebDriverWait του selenium"""
    # while True:
    for i in range(1000):
        
        """ ΜΕ ΤΗΝ ΠΑΡΑΚΑΤΩ ΕΝΤΟΛΗ ΓΙΝΕΤΑΙ ΕΛΕΓΧΟΣ ΣΤΟ DOM ΓΙΑ ΤΗΝ ΥΠΑΡΞΗ ΤΗΣ ΚΛΑΣΗΣ LOAD MORE
            ΔΙΝΟΝΤΑς ΠΕΡΙΘΩΡΙΟ 20 ΔΕΥΤΕΡΟΛΕΠΤΩΝ ΝΑ ΦΟΡΤΩΘΕΙ"""
        WebDriverWait(driver, timeout=30 ).until(expected_conditions.presence_of_element_located((By.CLASS_NAME , "loadmore"))) 
      
        more_button = driver.find_element(By.CLASS_NAME , "loadmore")        
        driver.execute_script("arguments[0].click();", more_button)

        print(i)
    
    page_source = driver.page_source
    return page_source

def start_scrapping(homepage_url = "https://fminside.net/players"):
    
        
    homepageAfterLoadMore = load_more() #με αυτο τον τροπο θα φορτώσω πρώτα την τελική σελίδα και μετά θα
                                        #παιρνω μια λιστα με τα λινκσ συνολικά
    
    soup = BeautifulSoup(homepageAfterLoadMore , 'lxml')
    
    links = soup.find_all("a",href=True)
    urls = []
    for link in links:
        if "players/3" in link["href"]:urls.append("https://fminside.net"+link["href"])
    urls = pd.DataFrame(urls)
    urls.to_csv("player_links.csv" , sep = "-", header = None, index = False)
    return urls

urls = start_scrapping()    



