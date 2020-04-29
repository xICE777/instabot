from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import keys_to_typing
import random
import time
import os
print(".__           ___________________________  ")
print("|__| ____  ___\______  \______  \______  \ ")
print("|  |/ ___\/ __ \  /    /   /    /   /    / ")
print("|  \  \__\  ___/ /    /   /    /   /    /  ")
print("|__|\___  >___  >____/   /____/   /____/   ")
print("        \/    \/                           ")
print("""""")
print("Indirme islemi gerceklesiyor")
os.system("pip install selenium")
time.sleep(2)
os.system("pip install random")
time.sleep(2)
os.system("pip install time")

a = str(random.randint(70,100))
b = str(random.randint(40,70))
c = str(random.randint(0,40))
adsoyad = "Selim"+"Yilmaz{0}{1}{2}".format(a,b,c)

mail = input("Mail Adresi veya Telefon Numarası: ")
username = input("Kullanıcı adı: ")
parola = "ICE777v01"
print("""Password(Sifre) otomatik olarak tanimlanmistir.
Password(Sifre): ICE777v01
""")
time.sleep(2)
class Date():
    def __init__(self,ay,gun,yil):
            self.ay = ay
            self.gun = gun
            self.yil = yil
class Instagram(Date):
    def __init__(self,username,mail,parola,adsoyad):
        self.adsoyad = adsoyad
        self.username = username
        self.mail = mail
        self.parola = parola
        self.browser = webdriver.Chrome()


    def signUp(self):
        time.sleep(2)
        self.browser.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(2)
        action = webdriver.ActionChains(self.browser)
        usernameinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input") 
        parolainput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input")
        mailinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        adsoyadinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input")

        mailinput.send_keys(self.mail)
        time.sleep(1)
        adsoyadinput.send_keys(self.adsoyad)
        time.sleep(1)
        usernameinput.send_keys(self.username)
        time.sleep(1)
        parolainput.send_keys(self.parola)
        time.sleep(1)
        parolainput.send_keys(Keys.ENTER)
        time.sleep(2.75)

    def button(self):
        self.ay = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select")
        time.sleep(0.5)
        self.ay.click()
        time.sleep(1)
        self.ay.send_keys(Keys.ENTER)
        self.gun = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select")
        self.gun.click()
        self.gun.send_keys(Keys.ENTER)
        time.sleep(2)
        self.yil = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select")
        self.yil.click()
        time.sleep(2)
        action = webdriver.ActionChains(self.browser)
        a = 0
        while a<14:
            action.key_down(Keys.ARROW_DOWN).perform()
            a +=1
        self.yil.send_keys(Keys.ENTER)
        buton = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[5]/div[2]/button")
        buton.click()
        time.sleep(10)
        self.browser.quit()

basla = Instagram(username,mail,parola,adsoyad)
basla.signUp()
basla.button()