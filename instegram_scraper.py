from selenium import webdriver
import time, urllib.request

#launch chrome & navigate to instegram link
url = "https://www.instagram.com/abledeskco/"

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
time.sleep(5)
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
time.sleep(5)
username.send_keys("email@gmail.com")
password.send_keys("123456789")
button.click()


time.sleep(20)
driver.get( url )


#Scoll down to the bottom of the page
heightOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var heightOfPage=document.body.scrollHeight;return heightOfPage;")
print(heightOfPage)

match=False
while(match==False):
    lastCount = heightOfPage
    time.sleep(3)
    heightOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var heightOfPage=document.body.scrollHeight;return heightOfPage;")
    if lastCount==heightOfPage:
        match=True

posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)




download_url = ''

for post in posts:
    driver.get(post)
    shortcode = driver.current_url.split("/")[-2]
    images = driver.find_elements_by_tag_name('img')
    #for image in images:
    download_url = images[1].get_attribute('src')
    urllib.request.urlretrieve(download_url, '{}.jpg'.format(shortcode))
    time.sleep( 5 )


print("Done!")
driver.close()

