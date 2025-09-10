import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options
import time
from random import randrange
import os

def main():
    filename = "PATH_TO_FILENAME.csv"
    linkname = 'PATH_TO_LINKNAME.csv'
    failedname = 'PATH_TO_FAILEDNAME.csv'

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=Chrome/5.0')
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    
    if not os.path.exists(filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerow(["Page Title", "Name", "Content"])
    
    web_crawler(load_links(linkname), driver, filename, linkname, failedname)

    driver.quit()
        
def load_links(linkname):
    pending_links = []
    with open(linkname, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                pending_links.append(row[0])

    return pending_links
       
def web_crawler(pending_links, driver, filename, linkname, failedname):
    article_count = 0
    failed_links = []
    for link in pending_links.copy():
        print(f'Processing {link}')
        try:
            driver.get(link)
            time.sleep(randrange(3, 5))
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            page_title = ""
            if soup.head and soup.head.title:
                page_title = soup.head.title.text.strip()

            name = ""
            h1_tag = soup.find('h1')
            if h1_tag:
                name = h1_tag.text.strip()

            content_parts = []
            article = soup.find('ELEMENT_OR_DIV_HOLDING_MAIN_ARTICLE')

            if not article:
                print("No article found!")

            unwanted_classes = ['NAMES_OF_CLASSES']
            for unwanted in unwanted_classes:
                if article.find('div', class_=unwanted):
                    article.find('div', class_=unwanted).decompose()

            article_elements = article.select('NAMES_OF_ELEMENTS_HOLDING_CONTENT')
            for element in article_elements:
                content_parts.append(element.text.strip())
            
            content = "\n\n".join(content_parts)

            write_content(filename, page_title, name, content)
            
            article_count += 1
            print(f'Article Nr {article_count} added!')

        except Exception as e:
            print (f'Failed to process {link}: {e}')
            failed_links.append(link)

        finally:
            pending_links.remove(link)
            print(f'{len(pending_links)} articles left.')

            if article_count % 10 == 0 or len(pending_links) == 0:
                write_pending_links(linkname, pending_links)
                print('Progress saved to file.')

    if len(pending_links) == 0:
        print('All articles processed!')

    if failed_links:
        write_failed_links(failedname, failed_links)
        print(f'Saved {len(failed_links)} failed links to {failedname}"')

def write_content(filename, page_title, name, content):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow([page_title, name, content])

def write_pending_links(linkname, pending_links):
    with open(linkname, 'w') as file:
        writer = csv.writer(file)
        for link in pending_links:
            writer.writerow([link])

def write_failed_links(failedname, failed_links):
    with open(failedname, 'w', newline='') as file:
        writer = csv.writer(file)
        for link in failed_links:
            writer.writerow([link])

main()


        