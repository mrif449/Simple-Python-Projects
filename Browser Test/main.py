import time
from selenium import webdriver
import webbrowser
import os


# create an instance of a web driver
def get_default_browser():
    browser = webbrowser._tryorder
    for b in browser:
        path = webbrowser.get(b).path
        if path is not None:
            return b
    return None


#SELECT THE NAME FOR YOUR WEB BROWSER

driver = webdriver.Chrome()
#driver = webdriver.Edge()




# start the timer
start_time = time.time()

# open 50 tabs of "github.com"
for i in range(300):
    driver.execute_script("window.open('https://mrif449.github.io/portfolio/index.html');")

# wait for all tabs to load
time.sleep(0)

# calculate the time taken
time_taken = time.time() - start_time

# close all tabs and the driver
driver.quit()

# give a score based on the time taken
if time_taken < 20:
    score = "A"
elif 20 <= time_taken < 30:
    score = "B"
elif 30 <= time_taken < 40:
    score = "C"
elif 40 <= time_taken < 50:
    score = "D"
else:
    score = "E"

print(f"Time taken: {time_taken:.2f} seconds")
print(f"Grade: {score}")

quit = input("Press Enter to Quit: ")
