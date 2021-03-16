
#%%
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pathlib import Path
from selenium.webdriver.chrome.options import Options
import pandas as pd
from os import walk
import data # remember to reload/rerun after changes

import functions

#%%

driver = webdriver.Chrome()
driver.implicitly_wait(2) # Wait up to 5 secs before throwing an error if selenium cannot find the element (!important)
# %%
username = data.overlord_prime_account["username"]
password = data.overlord_prime_account["password"]

# %%
functions.youtube_login(driver, username, password)

# %%
# columns = ["Titel","Playlist", "Status", "Game", "Path"]
# df = pd.DataFrame(columns=columns)

# import os
# files_path = "D:\Twitch VODs\Overlord_Prime"
# for i in os.listdir(files_path):
#     if (i.find("mp4") != -1):
#         df = df.append(pd.Series(data={"Titel":i, "Playlist":"test", "Status":"not uploaded", "Game":"World of Tanks", "Path":os.path.join(files_path, i)}, name="x"))

# df.to_csv("D:\Twitch VODs\Overlord_Prime\overview.csv")






# TODO read csv with video file information for upload

df = pd.read_csv("D:\Twitch VODs\Overlord_Prime\overview.csv")

# %%
# TODO find way for repeating upload

for idx in range(0,len(df)):
    videofile = df["Path"].iloc[idx]
    functions.youtube_upload(driver, videofile)

    title = "Overlord_Prime Stream [02-01-2021] WoT"
    date=df["Titel"].iloc[idx].split("_")[0]
    title=" ".join(["Overlord_Prime Stream", date, df["Game"].iloc[idx]]) 
    functions.set_title(driver, title)

    description = data.overlord_prime_account["description"]
    functions.set_description(driver, description)

    functions.open_more_options(driver)

    ### TODO SKAL ORDNES! HERFRA OG NED
    game = df["Game"].iloc[idx]
    functions.set_category_and_game(driver, game)

    functions.made_for_kids(driver, entry=False)

    functions.set_playlist_WoT(driver)

    sleep(0.5)
    elem = driver.find_element_by_xpath('//*[@id="next-button"]/div')
    elem.click()
    sleep(0.5)
    elem = driver.find_element_by_xpath('//*[@id="next-button"]/div')
    elem.click()
    sleep(0.5)
    elem = driver.find_element_by_xpath('//*[@name="PUBLIC"]//*[@id="radioLabel"]')
    elem.click()
    sleep(0.5)
    elem = driver.find_element_by_xpath('//*[@id="done-button"]/div')
    elem.click()
    sleep(0.5)
    elem = driver.find_element_by_xpath('//*[@id="close-button"]/div')
    elem.click()

    driver.get("https://www.youtube.com/upload")

#%%

# TODO function - insert description and options






# function download video from twitch - twitchleecher? - TODO later


# TODO update spreadsheet with videofiles


def insert_files_into_spreadsheet(files, df):
    for filename in files:
        if filename not in df.values:
            print("new entry:", filename)
            temp = pd.DataFrame([[filename, "not_uploaded"]], columns=["filename","status"])
            df = df.append(temp, ignore_index=True)
        else:
            print("entry exists:", filename)
    return df

data = {"filename": [],
        "status": []}
df = pd.DataFrame(data)

mypath = "D:\\Twitch VODs"

df = pd.read_csv(mypath + "\\uploaded\\upload_list.csv")

path = mypath+data.overlord_prime_account["path"]
files = list_files_folder(path)

df = insert_files_into_spreadsheet(files, df)

df.to_csv(mypath + "\\uploaded\\upload_list.csv", index=False)

# TODO 1. find videofiles in folder for channel wanted
# TODO 2. update spreadsheet for channel videofiles
# TODO 3. look for files not uploaded
# TODO 4. upload files with title+description
# TODO 4.1 update title to fit videofile
# TODO 4.2 update title based on information from video download
# TODO 5. change status for uploaded file after upload
# TODO 6. move videofile?
