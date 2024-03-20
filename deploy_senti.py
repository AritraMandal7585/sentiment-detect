# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:25:10 2024

@author: aritr
"""

input_text = "Everything that shines is not gold"

import requests

url = "http://127.0.0.1:8000/sentiment"

data = {"text": input_text}

response = requests.post(url, json=data)


if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print("Error:", response.status_code)
    print("Detail:", response.text)