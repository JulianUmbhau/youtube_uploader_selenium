from os import error
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def youtube_login(driver, username, password):
    driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
    elem = driver.find_element_by_xpath('//*[@id="identifierId"]')
    elem.send_keys(username)
    elem.send_keys(Keys.ENTER)
    elem = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    elem.send_keys(password)
    elem.send_keys(Keys.ENTER)
    # try:
    #     elem = WebDriverWait(driver, 1).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]'))
    #         )
    #     elem.click()
    #     code = input("Please enter code")
    #     sleep(1)
    #     elem = driver.find_element_by_xpath('//*[@id="idvPin"]')
    #     elem.send_keys(code)
    #     elem.send_keys(Keys.ENTER)
    # except TimeoutException:
    #     pass
    sleep(2)
    driver.get("https://www.youtube.com/upload")


def youtube_upload(driver, videofile):
    driver.get("https://www.youtube.com/upload")
    elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    elem.send_keys(videofile)  # Window$


def set_title(driver, title):
    elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="textbox" and @class="style-scope ytcp-mention-textbox"]'))
        )
    elem.clear()
    sleep(0.1)
    elem.send_keys(title)


def set_description(driver, description):
    elem = driver.find_element_by_xpath('//*[@id="description-container"]//*[@id="textbox" and @class="style-scope ytcp-mention-textbox"]')
    elem.clear()
    sleep(0.1)
    elem.send_keys(description)


def made_for_kids(driver, entry):
    if entry == True:
        elem = driver.find_element_by_xpath('//*[@id="made-for-kids-group"]/paper-radio-button[1]')
        elem.click()
    else:
        elem = driver.find_element_by_xpath('//*[@id="made-for-kids-group"]/paper-radio-button[2]')
        elem.click()


def set_playlist_WoT(driver):
    elem = driver.find_element_by_xpath('//*[@id="basics"]/ytcp-video-metadata-playlists/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[2]/div')
    elem.click()
    elem = driver.find_element_by_xpath('//*[@id="checkbox-label-0"]/span')
    elem.click()
    elem = driver.find_element_by_xpath('//*[@id="dialog"]/div[2]/ytcp-button[3]/div')
    elem.click()


def set_category_and_game(driver, game):
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="category"]//*[@id="trigger"]/ytcp-dropdown-trigger/div/div[2]/span'))
        )
    elem.click()
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@test-id="CREATOR_VIDEO_CATEGORY_GADGETS"]/ytcp-ve/div/div/yt-formatted-string'))
        )
    elem.click()
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="category-container"]//*[@class="style-scope ytcp-form-autocomplete"]//*[@type="text"]'))
        )
    elem.clear()
    elem.send_keys(str(game))
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="text-item-2"]/ytcp-ve/div/div/yt-formatted-string/span[1]'))
        )
    elem.click()


def open_more_options(driver):
    elem = driver.find_element_by_xpath('//*[@id="toggle-button"]/div')
    elem.click()


def upload_buttons(driver):
    sleep(0.5)
    elem = driver.find_element_by_xpath('//*[@id="next-button"]/div')
    elem.click()
    sleep(0.5)
    elem = driver.find_element_by_xpath('//*[@id="next-button"]/div')
    elem.click()
    sleep(0.5)
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@name="PUBLIC"]//*[@id="radioLabel"]'))
        )
    elem.click()
    sleep(0.5)
    elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="done-button"]/div'))
        )
    elem.click()
    elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="close-button"]/div'))
        )
    elem.click()
    

