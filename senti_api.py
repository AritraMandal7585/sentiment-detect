# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:13:07 2024

@author: aritr
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fastapi.middleware.cors import CORSMiddleware

# Declaring our FastAPI instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Add OPTIONS method
    allow_headers=["*"],
)
 
output = {}

class ModelInput(BaseModel):
    text: str

@app.post('/sentiment')
async def sentiment(input_parameters: ModelInput):
    try:
       test_data = input_parameters.text
       nltk.download("vader_lexicon")
       sid = SentimentIntensityAnalyzer()
       score = sid.polarity_scores(test_data)["compound"]
       if score > 0:
           output["sentiment"] = "Positive"
       else:
            output["sentiment"] = "Negative"
        
       return output
       
       
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
