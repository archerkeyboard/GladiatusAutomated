from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
#from main import chat
#from secondmain import chat2
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://s25-bg.gladiatus.gameforge.com/game/index.php?mod=overview&login=1&sh=0c0d12d435317d9c2363b4889568a6d6")

def checkHealthAndReplenish():
	health = driver.find_element_by_id("header_values_hp_percent").text
	healthNumber = int(health[:-1])
	if healthNumber < 40:
		pregled = driver.find_element_by_xpath("//a[@title = 'Преглед']")
		pregled.click()
		time.sleep(6)
		firstFoodInInventory = driver.find_element_by_xpath("//div[@id='inv']/div[1]")
		character = driver.find_element_by_id("avatar")
		ActionChains(driver).drag_and_drop(firstFoodInInventory, character).perform()
		time.sleep(4)

def work():
	leftMenu = driver.find_element_by_xpath("//div[@id='submenuhead1']/div[@class='menutab_city']/a[1]")
	leftMenu.click()
	time.sleep(3)
	workTab = driver.find_element_by_xpath("//div[@id='submenu1']/a[1]")
	workTab.click()
	time.sleep(4)
	doWork = driver.find_element_by_id("doWork")
	doWork.click()
	time.sleep(2)

def checkExistsByXpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


time.sleep(3)
firstLi = driver.find_element_by_xpath("//ul[@class='tabsList']/li[1]")
time.sleep(0.5)
firstLi.click()

email = driver.find_element_by_name('email')
email.send_keys("user@gmail.com")#enter user here

password = driver.find_element_by_name('password')
password.send_keys("password")#enter password here
time.sleep(0.5)
password.send_keys(Keys.RETURN)


time.sleep(3)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

cookiebanner5 = driver.find_element_by_xpath("//*[@class='cookiebanner5']")
cookiebanner5.click()

newbtn = driver.find_element_by_xpath("//*[@class='button button-default button-md']")

newbtn.click()

time.sleep(5)
driver.switch_to_window(driver.window_handles[-1])
title=driver.title

arenaListing = 29 #-1 actually - izpolzva se pri ataki po-dolu

n = 5
while n > 0:
	try:
		checkHealthAndReplenish()
		divTime = driver.find_element_by_id("cooldown_bar_text_expedition").text
		if divTime == "Към експедицията":
			#atakuva
			loadBar = driver.find_element_by_xpath("//div[@id='cooldown_bar_expedition']/a[1]")
			loadBar.click()
			time.sleep(5)
			attack = driver.find_element_by_xpath("//div[@class='expedition_box'][1]/div[2]/button[1]")
			attack.click()
			time.sleep(3)

		divDungeon = driver.find_element_by_id("cooldown_bar_text_dungeon").text
		if divDungeon == "Отиди в подземието":
			loadBar = driver.find_element_by_xpath("//div[@id='cooldown_bar_dungeon']/a[1]")
			loadBar.click()
			time.sleep(3)
			#check if started
			print("1")
			notStarted = checkExistsByXpath("//input[@value='Обикновено']")
			if notStarted:
				print("2")
				defaultButton = driver.find_element_by_xpath("//input[@value='Обикновено']")
				defaultButton.click()
				time.sleep(3)
			print("3")
			firstLevelGustav = checkExistsByXpath("//div[@class = 'contentItem_content'/div[1]/span[@class ='dungeoncondition_not_fulfilled']")			
			if firstLevelGustav == True:
				print("in")
				firstLevelGustavHolder = driver.find_element_by_xpath("//img [@src = '9387/img/dungeons/slices/1_1.jpg'")
				firstLevelGustavHolder.click()
			secondLevelGustav = checkExistsByXpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:255px;top:209px']")
			if secondLevelGustav == True:
				secondLevelGustavHolder = driver.find_element_by_xpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:255px;top:209px']")
				secondLevelGustavHolder.click()
			shef = checkExistsByXpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:368px;top:326px']")
			if shef == True:
				shefHolder= driver.find_element_by_xpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:368px;top:326px']")
				shefHolder.click()
			
			#piratsko dungeon - slaba sum oshte - 16lvl
			# purviLqvo = checkExistsByXpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:145px;top:367px']")
			# if purviLqvo == True:
			# 	purviLqvoHolder = driver.find_element_by_xpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:145px;top:367px']")
			# 	purviLqvoHolder.click()
			# vtoriLqvo = checkExistsByXpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:205px;top:345px']")
			# if vtoriLqvo == True:
			# 	vtoriLqvoHolder = driver.find_element_by_xpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:205px;top:345px']")
			# 	vtoriLqvoHolder.click()
			# tretiLqvo = checkExistsByXpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:296px;top:360px']")	
			# if tretiLqvo == True:
			# 	tretiLqvoHolder = driver.find_element_by_xpath("//img[@style='cursor:pointer;width:16px;height:16px;position:absolute;left:296px;top:360px']")
			# 	tretiLqvoHolder.click()
		time.sleep(4)

		arenaDiv = driver.find_element_by_id("cooldown_bar_text_arena").text
		if (arenaDiv == "Към арената"):
			klasaciq = driver.find_element_by_xpath("//a[@title = 'Класация']")
			klasaciq.click()
			time.sleep(5)
			#select = Select(driver.find_element_by_xpath("//select[@class = 'input']"))
			#select.select_by_visible_text("51-100                            ")
			#time.sleep(5)
			while n > 0:
				if arenaListing == 37: #do kude da bie, pak -1
					arenaListing = 29 #second start
					work()
				arenaPlayerName = driver.find_element_by_xpath("//tr[" + str(arenaListing) + "]/td[1]/span[1]/a[1]")
				isGuildMember = checkExistsByXpath("//tr[" + str(arenaListing) + "]/td[1]/span[1]/a[1]/span[@style='color:green;font-weight:bold;']")
				if isGuildMember == True:
					arenaListing += 1
					break
				arenaPlayerName.click()
				time.sleep(5)
				attackButton = driver.find_element_by_xpath("//input[@value='Арена']")
				attackButton.click()
				time.sleep(5)
				arenaListing += 1
				break

		time.sleep(35)
	except StaleElementReferenceException:
		print("stale")
		time.sleep(3)
		pregled3 = driver.find_element_by_xpath("//a[@title = 'Преглед']")
		pregled3.click()
	except NoSuchElementException:
		time.sleep(2)
		print("sleepy")
		pregled2 = driver.find_element_by_xpath("//a[@title = 'Преглед']")
		pregled2.click()
	except ElementClickInterceptedException:
		print("intercept")
		time.sleep(3)
		firstPopup = checkExistsByXpath("//div[@class='openX_int_closeButton']/a[1]")
		if firstPopup == True:
			loginXButton = driver.find_element_by_xpath("//div[@class='openX_int_closeButton']/a[1]")
			loginXButton.click()
			
		okButton = checkExistsByXpath("//input[@value='OK']")
		if okButton == True:
			okButtonElement = driver.find_element_by_xpath("//input[@value='OK']")
			okButtonElement.click()
	except ElementNotInteractableException:
		print("no idea what's this")
		pregled3 = driver.find_element_by_xpath("//a[@title = 'Преглед']")
		pregled3.click()

		# neButton = checkExistsByXpath("//input[@value='Не']")
		# if neButton == True:
		# 	neButton = driver.find_element_by_xpath("//input[@value='Не']")
		# 	neButton.click()

		time.sleep(3)

		#do more popups					