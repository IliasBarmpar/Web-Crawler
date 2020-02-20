import os
import time
from openpyxl import Workbook, load_workbook
from pandas import DataFrame, read_csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC

class ponsUnitTest():
    def __init__(self):
        #Loads a chromedriver as soon as you load the class    
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--disable-popup-blocking')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = dir_path + "/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chrome_options=options, executable_path= chromedriver)

    def timerPractice(self):
        time.sleep(10)

    def teardown(self):
        self.driver.close()

    def extractData(self, word):
        ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located((By.ID, "q")))
        self.driver.find_element_by_id("q").send_keys(word)
        ui.WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, "search_button"))).click()
        
        
        #parentTab = self.driver.find_element_by_id('deen')
        abc = self.driver.find_element_by_xpath("//div[@class='translations first opened']")
        item1 = ''
        item2 = ''
        i = -1
        for line in abc.text.splitlines():
            i += 1
            if i == 0:
                continue
            elif i == 1:
                item1 = line
            elif i == 2:
                item2 = line
            else:
                break
        
        #lets click now
        new_url = self.driver.current_url + "#examples"
        self.driver.get(new_url)
        cba = self.driver.find_element_by_xpath("//dl[@class='dl-horizontal']")
        itemx1 = ''
        itemx2 = ''
        i = -1
        for line in cba.text.splitlines():
            i += 1
            if i == 0:
                itemx1 = line
            elif i == 1:
                itemx2 = line
            else:
                break
        print ("items: '", item1, "' '", item2, "'")
        print ("items: '", itemx1, "' '", itemx2, "'")


    def gotoDict(self):
        self.driver.get("https://en.pons.com")
        ui.WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "qc-cmp-button"))).click()
        ui.WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "qc-cmp-save-and-exit"))).click()

        new_workbook=load_workbook('C:/Users/ilias/Desktop/testy.xlsx')
        sheet = new_workbook["Sheet1"]
        print(sheet['A2'].value)

        #dataset = pd.ExcelFile(r"C:\Users\ilias\Desktop\testForPe.xls")
        #df = dataset.parse('Sheet1')
        #print ("xxx")
        #for index, row in df.iterrows():
        #    print(index, row['Words'])
        #    self.extractData(row['Words'])
        #    abc = input()
        #print ("xxx")
        
        #print (df)
        #print (type(df))
        #for line in df:
        #    print ("line:", line)
        #self.extractData('nehmen')
        #self.extractData('lernen')
        #curr_word = 'nehmen'
        
        """
        ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located((By.ID, "q")))
        self.driver.find_element_by_id("q").send_keys(curr_word)
        ui.WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, "search_button"))).click()
        
        
        #parentTab = self.driver.find_element_by_id('deen')
        abc = self.driver.find_element_by_xpath("//div[@class='translations first opened']")
        item1 = ''
        item2 = ''
        i = -1
        for line in abc.text.splitlines():
            i += 1
            if i == 0:
                continue
            elif i == 1:
                item1 = line
            elif i == 2:
                item2 = line
            else:
                break
        

        #lets click now
        new_url = self.driver.current_url + "#examples"
        self.driver.get(new_url)
        cba = self.driver.find_element_by_xpath("//dl[@class='dl-horizontal']")
        itemx1 = ''
        itemx2 = ''
        i = -1
        for line in cba.text.splitlines():
            i += 1
            if i == 0:
                itemx1 = line
            elif i == 1:
                itemx2 = line
            else:
                break
        print ("items: '", item1, "' '", item2, "'")
        print ("items: '", itemx1, "' '", itemx2, "'")
        """
        
#<input type="submit" value="Suche" class="inp1" style="width:60px;padding:4px;-webkit-text-size-adjust: 140%">

if __name__ == "__main__":
    obj = ponsUnitTest()
    obj.gotoDict()