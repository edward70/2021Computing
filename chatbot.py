print("remember to have selenium webdriver + chrome webdriver installed and close chrome tabs")

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os
import time

chrome_options = Options()
username = os.getlogin()
chrome_options.add_argument("--user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\".format(username))
chrome_options.add_argument("--log-level=3")
driver = Chrome(executable_path='C:\\chromedriver\\chromedriver.exe', options=chrome_options)

driver.get("https://suzannecoryhs-vic.compass.education/")

time.sleep(5)

news = driver.find_elements_by_css_selector(".newsfeed-newsItem-container .ellipse")
classes = driver.find_elements_by_css_selector(".ext-evt-bd")

class Perceptron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def inference(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        sum += self.bias
        if sum >= 0:
            return 1
        elif sum < 0:
            return 0

newsPerceptron = Perceptron([1,-1], -1)
schedulePerceptron = Perceptron([-1, 1], -1)

#while True:
#    command = input("Type message to chatbot: ")
#   if "quit" in command or "stop" in command:
#        print("quitting chatbot")
#        exit(0)
#    elif "news" in command:
#        print("=== News ===")
#        for i in news:
#            print(i.text)
#            print("======")
#    else:
#        print("command not understood")

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    newsinput = 0
    scheduleinput = 0
    if "news" in message.content:
        newsinput += 1
    if "post" in message.content:
        newsinput += 1
    if "schedule" in message.content:
        scheduleinput += 1
    if "classes" in message.content:
        scheduleinput += 1
    a = newsPerceptron.inference([newsinput, scheduleinput])
    b = schedulePerceptron.inference([newsinput, scheduleinput])

    if a:
        reply = f'=== News ===\n'
        for i in range(3):
            reply += news[i].text + f"\n"
            reply += f'======\n'
        await message.channel.send(reply)
    if b:
        reply = f'=== Schedule ===\n'
        for i in classes:
            reply += i.text + f"\n"
        await message.channel.send(reply)

with open('token.txt', 'r') as f:
    client.run(f.read())
