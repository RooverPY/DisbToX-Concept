##########################################################
#__________                                 
#\______   \ ____   _______  __ ___________ 
# |       _//  _ \ /  _ \  \/ // __ \_  __ \
# |    |   (  <_> |  <_> )   /\  ___/|  | \/
# |____|_  /\____/ \____/ \_/  \___  >__|   
#        \/                        \/          
##########################################################
# Credits to Roover https://github.com/ItzRover https://github.com/swishyw #
##########################################################
try:
    import os
    from utils import coloring
    from datetime import datetime
    import requests
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    import time
except ImportError:
    print(f"{coloring.WARNING}<==========[Failed to Import Neccessary Modules]==========>")
    os._exit(1)
    #Incase of import error, prints that the import failed, and exits. We import OS and Colors FIRST because of this, to print the error in color, and exit the script.
##########################################################
class tox:
  def __init__(self, choice, target, reason):
    self.choice = choice
    self.target = target
    self.reason = reason

  def execute(self):
    for i in range(100):
      options = webdriver.ChromeOptions()
      options.add_experimental_option('excludeSwitches', ['enable-logging'])
      driver = webdriver.Chrome(options=options)
      time.sleep(3)
      driver.get(f"https://disboard.org/report-server/create/{self.target}")
      name = driver.find_element_by_class_name("server-name > a").get_attribute('href') 
      print(f"\n         {coloring.BLUE}Browsing: {driver.title}")
      print(f"         {coloring.BLUE}Reported Server: {name}")
      time.sleep(3)
      select = Select(driver.find_element_by_id('reportserver-type'))
      if self.choice == "1":
        select.select_by_value('1')
      elif self.choice == "2":
        select.select_by_value('2')
      elif self.choice == "3":
        select.select_by_value('3')
      time.sleep(2)
      report_field = driver.find_element_by_id("reportserver-description")
      report_field.clear()
      report_field.send_keys(self.reason)
      driver.find_element_by_xpath('//button[normalize-space()="Submit"]').click()
      time.sleep(3)
      driver.close()
      driver.quit()
      time.sleep(1)
    print(f"         {coloring.BLUE}Finished ToX")
##########################################################
def asking():
  print(f"""
             {coloring.BLUE}╔╦╗╦╔═╗╔╦╗╔═╗═╗ ╦
             ║║║ ╚═╗ ║ ║ ║╔╩╦╝
             ═╩╝╩╚═╝ ╩ ╚═╝╩ ╚═
         {coloring.BLUE}╔═══════════════════════╗
         {coloring.BLUE}║  {coloring.WARNING}[1] Invalid Invite  {coloring.BLUE} ║ 
         {coloring.BLUE}║  {coloring.WARNING}[2] Description     {coloring.BLUE} ║ 
         {coloring.BLUE}║  {coloring.WARNING}[3] Spam/Fake     {coloring.BLUE}   ║""") 
  print(f"         {coloring.FAIL}═════════════════════════\n")

def main():
  os.system('color 1')
  asking()
  choice = input(f"         {coloring.WARNING}┌──(-RooverNET)-[/] {coloring.BLUE}Select Choice:{coloring.WARNING} [!]\n{coloring.WARNING}         └─> ")
  print("\n")
  if choice in ["1", "2", "3"]:
    os.system('cls')
    target = input(f"         {coloring.WARNING}┌──(-RooverNET)-[/] {coloring.BLUE}Enter Target Server ID:{coloring.WARNING} [!]\n{coloring.WARNING}         └─> ")
    reason = input(f"         {coloring.WARNING}Enter Report Reasoning: [!]\n         └─> ")
    tox(choice, target, reason).execute()
  else: 
    os.system('cls')
    asking()
  #Uses the main function to start the code proccess.
##########################################################
if __name__ == '__main__':
    os.system('cls')
    main()
##########################################################
# Dev Notes #
# Was getting a retarded error in console about a device not functioning so here was the solution.
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
##########################################################