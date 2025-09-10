import csv
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


filename = 'PATH_TO_FILENAME.csv'
target = "LINK_TO_BASE_LEVEL_SITEMAP"

def main():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    write_to_csv(get_link_list(get_sitemap_links(target, driver), driver))

    driver.quit()


def get_sitemap_links(link, driver):

    site_map_links = []

    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.find_all('a')
    for i in links:
       if i.get('href').startswith('SITEMAP_STRUCTURE_FILTER_TO_GET_RELEVENT_CATEGORIES'):
                site_map_links.append(i.get('href'))

    return site_map_links
    

def get_link_list(site_map_links, driver):

    links_to_write = []

    for link in site_map_links:
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        final_links = soup.find_all('a')
        for i in final_links:
            if i.get('href').startswith('SITEMAP_STRUCTURE_FILTER_TO_GET_RELEVENT_LINKS'):
                        links_to_write.append(i.get('href'))
    
    return links_to_write

def write_to_csv(all_links):
    duplicate_list = all_links.copy()
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    duplicate_list.append(row[0])

    duplicate_list = list(set(duplicate_list))
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in duplicate_list: 
            writer.writerow([i]) 
                            
main()
