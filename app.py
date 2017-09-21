from splinter import Browser
import pandas as pd

url = 'https://google.com'

# open a browser
browser = Browser('chrome')
browser.visit(url)

# Width, Height
browser.driver.set_window_size(640, 480)

# set HTML XPATH to variable
search_bar_xpath = '//*[@id="lst-ib"]'

# index 0 to select from the list
search_bar = browser.find_by_xpath(search_bar_xpath)[0]

# fill() and click() can be used for user logins as well!
search_bar.fill("Battlefield 1")

# Now let's set up code to click the search button! 

search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]' 
search_button = browser.find_by_xpath(search_button_xpath)[0]
search_button.click() # simulates a click

# finds all h3 tags with class 'r', returns all a tags within
search_results_xpath = '//h3[@class="r"]/a'
search_results = browser.find_by_xpath(search_results_xpath)

scraped_data = []
for search_result in search_results:
  # the data in .text can be cleaned with .replace() .encode() and .strip() to name a few
     title = search_result.text.encode('utf8')  # utf8?
     link = search_result["href"]
     scraped_data.append((title, link))  # put in tuples

# pandas dataframe
df = pd.DataFrame(data=scraped_data, columns=["Title", "Link"])
df.to_csv("links.csv")