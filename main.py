import util.image as img
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome('/Users/xuyue000/Documents/chromedriver')
url = "http://www.misha.fr/papyrus_bipab/TdM.html"

driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, "html.parser")
img_num = 0
for link in soup.findAll('a', attrs={'href': re.compile("^pages_html/")}):

    # print(link.get('href'))
    tag = link.get('href')
    each_url = "http://www.misha.fr/papyrus_bipab/" + tag
    # print(each_url)
    driver.get(each_url)
    each_page_content = driver.page_source.encode('utf-8').strip()
    soup1 = BeautifulSoup(each_page_content, "html.parser")

    for link1 in soup1.findAll('a', attrs={'href': re.compile("^../images/grandes_images")}):
        original_href = str(link1.get('href'))
        grand_link = original_href.replace("..", "http://www.misha.fr/papyrus_bipab", 1)
        file_trim = str(original_href.replace("../images/grandes_images/", "", 1))
        grand_link_str = str(grand_link)
        # print(grand_link_str)
        file_name = "/Users/xuyue000/Desktop/export/" + file_trim
        img.download(grand_link_str, file_name)
        img_num += 1
        # print image name
        print(file_trim)
        # print image path
        print(str(grand_link))

# print num of img
print(img_num)
driver.quit()

print("ALL done")
