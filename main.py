# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from selenium.webdriver.common.by import By
import pytest


caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_v8.1 (403424005)_apkpure.com.apk"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

# Acionador do Script / código

if __name__ == '__main__':

#    def testMultiplyManyNumbers():
        # Conexao com o Salce Labs, aponta o DataCenter, meu usuário e chave
        driver = webdriver.Remote("https://up202101652:f4d70a49-450d-4300-9c67-7586816a1597@ondemand.eu-central-1.saucelabs.com:443/wd/hub", caps)
        resultado_esperado = '333333333'

        # Realiza a conta
        el1 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_1")
        el1.click()
        el2 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_2")
        el2.click()
        el3 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_3")
        el3.click()
        el4 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_4")
        el4.click()
        el5 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_5")
        el5.click()
        el6 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_6")
        el6.click()
        el7 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_7")
        el7.click()
        el9 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_9")
        el9.click()
        el99 = driver.find_element(By.ACCESSIBILITY_ID, "multiply")
        el99.click()
        el10 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_2")
        el10.click()
        el11 = driver.find_element(By.ID, "com.google.android.calculator:id/digit_7")
        el11.click()
        el12 = driver.find_element(By.ACCESSIBILITY_ID, "equals")
        el12.click()
        resultado_final = driver.find_element(By.ID, "com.google.android.calculator:id/result_final")
        print(f'resultado_final = {resultado_final.text} \n resultado_esperado = {resultado_esperado}')
        assert resultado_final.text == resultado_esperado
        driver.quit()
