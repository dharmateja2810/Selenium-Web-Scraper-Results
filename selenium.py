#importing required modules
import time as t
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#variables
os.chdir(r'C:\Users\Sowjanya Narisetty\Desktop')
driver = webdriver.Chrome()
#file to save the data
file = open("file.txt",'a')
#link for the website
link = 'https://rvrjcce.ac.in/examcell/results/regnoresultsR.php'
driver.get(link)
t.sleep(2)
file.write("\n")
#function to get the required data from the website
def results(branch,roll_number):
    input_field = driver.find_element(by='css selector', value="input[onkeyup='showUser(this.value)']")
    for i in range(1,roll_number+1):
        count = 0
        if i<=9:
            num = '00'
        elif i<=99:
            num = '0'
        else:
            num = ''
        rno = branch+num+str(i)
        input_field.send_keys(rno)
        t.sleep(1)
        try:
            table = driver.find_element(by = By.ID,value="container")
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                for cell in cells:
                    value = cell.text
                    if count==1:
                        count=2
                        continue
                    if value=='--':
                        continue
                    else:
                        file.write(value)
                       # file.write(" "+str(count))
                        if count<=1 or count==11:
                            file.write("\n")
                        else:
                            file.write("\t")
                        count+=1
            file.write("\n")
                    
        except Exception as e:
            print(e)

        input_field.clear()
        t.sleep(1)

"""results('y22cs',198)
#results('y22cd',190)
results('y22cb',65)
results('y22co',66)
results('y22cm',195)
"""
results('y22it',133)
file.close()
driver.quit()
