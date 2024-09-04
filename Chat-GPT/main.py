import openai
from colorama import Fore
import sys
import time
import os
import urllib
import random
#Imports

# Set up the OpenAI API client
#In secrets set key to "APIKEY" and value to your api key 
openai.api_key = os.environ['APIKEY']


def typepr(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(random.randrange(10, 30) / 1000)
#Typing Animation


# Set up the model and prompt
model_engine = "text-davinci-003"

# Generate a response
completion = openai.Completion.create(
  engine=model_engine,
  prompt=urllib.parse.quote(input(Fore.LIGHTBLUE_EX + "You: ")),
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0,
)

response = completion.choices[0].text
typepr(Fore.GREEN + "Bot: " + response + "\n")
os.system("python main.py")

#Change temperature from 0 as creative,0.5 as balanced and 0.8 as Logical
