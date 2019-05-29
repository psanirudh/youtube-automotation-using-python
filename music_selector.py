from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def skip_ad():
##<button class="ytp-mute-button ytp-button" title="Unmute (m)">

    try:
        me = driver.find_element_by_xpath("//button[contains(@class,'ytp-mute-button ytp-button')]")
        ad_container=driver.find_element_by_xpath("//div[contains(@class,'ytp-ad-text')]")##-ad-simple-ad-badge" id="simple-ad-badge:l" style=""><div class="ytp-ad-text" id="simple-ad-badge:m" style="">Ad 1 of 2 ·</div></span><span class="ytp-ad-duration-remaining" id="ad-duration-remaining:n" style=""><div class="ytp-ad-text" id="ad-text:o" style="">0:14</div></span><span class="ytp-ad-hover-text-button ytp-ad-info-hover-text-button" id="ad-info-hover-text-button:p" style=""><button class="ytp-ad-button ytp-ad-button-link ytp-ad-clickable" id="button:q" style=""><span class="ytp-ad-button-icon"><svg fill="#fff" height="100%" version="1.1" viewBox="0 0 48 48" width="100%"><path d="M0 0h48v48H0z" fill="none"></path><path d="M22 34h4V22h-4v12zm2-30C12.95 4 4 12.95 4 24s8.95 20 20 20 20-8.95 20-20S35.05 4 24 4zm0 36c-8.82 0-16-7.18-16-16S15.18 8 24 8s16 7.18 16 16-7.18 16-16 16zm-2-22h4v-4h-4v4z"></path></svg></span></button><div class="ytp-ad-hover-text-container ytp-ad-info-hover-text-short">Why this ad?<div class="ytp-ad-hover-text-callout"></div></div></span><button class="ytp-ad-button ytp-ad-visit-advertiser-button ytp-ad-button-link" id="visit-advertiser:t" aria-label="simplilearn.com/senior-data-scie..." style=""><span class="ytp-ad-button-text">simplilearn.com/senior-data-scie...</span><span class="ytp-ad-button-icon"><svg fill="#fff" height="100%" version="1.1" viewBox="0 0 48 48" width="100%"><path d="M0 0h48v48H0z" fill="none"></path><path d="M38 38H10V10h14V6H10c-2.21 0-4 1.79-4 4v28c0 2.21 1.79 4 4 4h28c2.21 0 4-1.79 4-4V24h-4v14zM28 6v4h7.17L15.51 29.66l2.83 2.83L38 12.83V20h4V6H28z"></path></svg></span></button></div><div class="ytp-ad-player-overlay-skip-or-preview"><div class="ytp-ad-skip-ad-slot" id="skip-button:f" style=""><div class="ytp-ad-preview-slot" id="preskip-component:g" style="display: none;"><span class="ytp-ad-preview-container countdown-next-to-thumbnail" style="display: none;"><div class="ytp-ad-text ytp-ad-preview-text" id="ad-text:h" style="display: none;">1</div><span class="ytp-ad-preview-image"><img class="ytp-ad-image" id="ad-image:i" src="https://i.ytimg.com/vi/xsbLtHql4g8/mqdefault.jpg" alt="" style="display: none;"></span></span></div><div class="ytp-ad-skip-button-slot" id="skip-button:j" style=""><span class="ytp-ad-skip-button-container" style="opacity: 0.5;"><button class="ytp-ad-skip-button ytp-button"><div class="ytp-ad-text ytp-ad-skip-button-text" id="ad-text:k" style="">Skip Ads</div><span class="ytp-ad-skip-button-icon"><svg height="100%" version="1.1" viewBox="0 0 36 36" width="100%"><use class="ytp-svg-shadow" xlink:href="#ytp-id-45"></use><path class="ytp-svg-fill" d="M 12,24 20.5,18 12,12 V 24 z M 22,12 v 12 h 2 V 12 h -2 z" id="ytp-id-45"></path></svg></span></button></span></div></div></div><div class="ytp-ad-player-overlay-progress-bar"></div><div class="ytp-ad-player-overlay-instream-user-sentiment"></div><div class="ytp-ad-info-dialog-background" id="ad-info-dialog:r" style="display: none;"><div class="ytp-ad-info-dialog-container"><div class="ytp-ad-info-dialog-form"><div class="ytp-ad-info-dialog-title">This ad is based on:</div><ul class="ytp-ad-info-dialog-ad-reasons"><li>The time of day, the website you were viewing or your general location (for example country or city).</li><li>This ad was shown based on your recent searches from your Google account.</li><li>Information in your Google Account.</li><li>The gender you added to your Google Account</li><li>Advertisers who want to reach people interested in both high-end and mainstream goods and services.</li></ul><div class="ytp-ad-info-dialog-message"><span><span><br></span><span>Visit Google's </span><a href="https://adssettings.google.com" target="_blank" class="ytp-ad-has-logging-urls">Ad Settings</a><span> to learn more about how ads are targeted or to opt out of personalized ads.</span></span></div><div class="ytp-ad-info-dialog-mute-container"></div><div class="ytp-ad-info-dialog-confirm-container"><button class="ytp-ad-info-dialog-confirm-button">CLOSE</button></div></div></div><button class="ytp-ad-button ytp-ad-info-dialog-close-button ytp-ad-button-link" id="button:s" style="display: none;"><span class="ytp-ad-button-icon">
        if(ad_container.text=="Ad ·" and me.get_attribute("title")=="Mute (m)"):
            me.click()
        msg=driver.find_element_by_xpath("//span[contains(@class,'ytp-ad-skip-button-container')]")
        ##time.sleep(3)
        msg.click()
        me = driver.find_element_by_xpath("//button[contains(@class,'ytp-mute-button ytp-button')]")
        if(me.get_attribute("title")=="Unmute (m)"):
            me.click()
        print("cool")
    except:
        a=0##print("sad")

  


z=[]
no_songs=int(input("enter number of songs:"))
print("enter "+str(no_songs)+" songs:")
for i in range(no_songs):
    temp=input("")
    z.append(temp)
driver = webdriver.Chrome(r'C:\Users\anirudh\Downloads\setup for downloaded files\chromedriver.exe')
#put your chrome driver path above

driver.get('https://www.youtube.com')
for no in range(no_songs):
    #a=input("enter what you want")
    element = driver.find_element_by_id("search")
    for i in range(60):
        element.send_keys(Keys.BACKSPACE)
    element.send_keys(z[no])
    print("done")
    searbtn = driver.find_element_by_id("search-icon-legacy")
    searbtn.click()
    time.sleep(3)
    arrow = driver.find_element_by_xpath('//div[@id="dismissable" and @class="style-scope ytd-video-renderer"]')
    arrow.click()
    time.sleep(3)
    dur=driver.find_element_by_xpath("//span[contains(@class,'ytp-time-duration')]")
    a=dur.text
    print(a)
       
    while(True):
        skip_ad()
        repl=driver.find_element_by_xpath("//button[contains(@class,'ytp-play-button ytp-button')]")
        print(repl.get_attribute("title"))
        answer=repl.get_attribute("title")
        if(answer=="Replay"):
            print("finished")
            break

print("the end...")

