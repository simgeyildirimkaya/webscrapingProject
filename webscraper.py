import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/simgeyildirimkaya/Desktop/chrome driver /chromedriver')
driver.get('https://www.worldcoffeeportal.com/Latest/News')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.find_all(attrs='newsItem'):
    article = a.find('h1')
    if article not in results:
        results.append(article.text)

print(results)


print(other_results)
df = pd.DataFrame({'Articles': results})
df.to_csv('coffee.csv', index=False, encoding='utf-8')