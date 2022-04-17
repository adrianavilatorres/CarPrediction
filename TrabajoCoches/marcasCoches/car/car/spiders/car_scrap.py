import scrapy
import random
import time
import re
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


class CarScrapSpider(scrapy.Spider):
    name = 'car_scrap'
    allowed_domains = ['https://informatica.ieszaidinvergeles.org:10099/pia/practica2/opel.html']
    start_urls = ['http://https://informatica.ieszaidinvergeles.org:10099/pia/practica2/opel.html/']
    
    coches = []

    
        
    
    driver = uc.Chrome()

    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0']
    agents = len(user_agents) - 1

    pages = ['https://www.coches.net/segunda-mano/?MakeId=69&MinYear=2010&MaxYear=2020&MinKms=10000&pg=2']
    first = True
    
    for page in pages:
        increment = 100
        agent_number = random.randint(0, agents)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agents[agent_number]})
        driver.get(page)
        f = open("text.txt", "w")
        if first:
            button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/footer/div/button[2]")
            button.click()
            first = False
        while True:
            driver.execute_script("window.scrollTo(0, " + str(increment) + ");")
            time.sleep(0.3)
            elements = driver.find_elements(By.CLASS_NAME, 'mt-CardBasic-titleLink')
            
            for coche in elements:
                car = coche.get_attribute("href")
                print(car)
                print("====================")
                f.write(car + "\n")
                coches.append(car)
                
            increment += 200
            if len(elements) >= 30 or increment >= 6000:
                break
        time.sleep(random.randint(3, 5))
        
    