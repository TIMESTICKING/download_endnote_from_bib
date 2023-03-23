import os
import re
import time
import threading
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

def get_titles(bib_file):
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = r'(?<=\s)title\s*=\s*{([^}]*)}'
    titles = re.findall(pattern, content)
    return titles


def download_endnote(title, url):
    try:
        response = requests.get(url)

        current_dir = os.getcwd() + '/refs'
        os.makedirs(current_dir, exist_ok=True)

        # random file name
        file_name = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(10))+'.enw'

        filepath = os.path.join(current_dir, file_name)

        with open(filepath, 'wb') as f:
            f.write(response.content)
            f.close()

        print(f"file has been saved successfully! {filepath}")
    except Exception as e:
        print(e, title)

    # driver.get(url)
    # time.sleep(1)
    # try:
    #     elem = driver.find_element(By.LINK_TEXT, 'EndNote')
    #     download_url = elem.get_attribute('href')
    #     response = requests.get(url)
    #     filename = os.path.basename(download_url)
    #     with open(filename, 'wb') as f:
    #         f.write(response.content)
    #     print(f'Successfully downloaded Endnote file: {filename}')
    # except Exception as e:
    #     print(e)
    #     pass



def download_article(driver, title):
    # query = f'site:scholar.google.com "{title}"'
    url = f'https://scholar.google.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={title}&btnG='
    driver.get(url)
    time.sleep(1)
    try:
        elem = driver.find_element(By.CSS_SELECTOR, 'a.gs_or_cit.gs_or_btn')
        elem.click()
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        links = soup.select('a:contains("EndNote")')[0]
        endnote_link = links['href']
        print(endnote_link)
        if endnote_link:
            download_endnote(title, endnote_link)
        else:
            print(f'Endnote download link not found for article: {title}')
    except Exception as e:
        print(e)
        pass
    # try:
    #     elem = driver.find_element(By.CSS_SELECTOR, 'span') #.find_element_by_css_selector('a[href^="/scholar?cluster"]')
    #     elem.click()
    #     time.sleep(2)
    #     download_endnote(driver, driver.current_url)
    # except Exception as e:
    #     print(e)
    #     pass


def download_all_articles(bib_file):
    titles = get_titles(bib_file)
    print(f'Total {len(titles)} titles found')
    driver = webdriver.Chrome()
    for i, title in enumerate(titles):
        print(f'Downloading article {i+1}/{len(titles)}')
        download_article(driver, title)
    driver.quit()


if __name__ == '__main__':
    bib_file = 'bib.txt'
    download_all_articles(bib_file)
