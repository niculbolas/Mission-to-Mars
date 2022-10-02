# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
browser = Browser('chrome', headless=True)

url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Loop over the 4 hemisphere images
for i in range(4):
    # Find and click on a thumbnail
    browser.find_by_css('img[class="thumb"]')[i].click()
    
    # Grab the title
    title = browser.find_by_css('h2[class="title"]').text
    
    # Look at the original link and grab the hyperlink reference
    url = browser.links.find_by_text('Sample')["href"]
    
    # Add the found data to our list  
    hemisphere_image_urls.append({'img_url':url, 'title':title})

    # Back to previous page
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()