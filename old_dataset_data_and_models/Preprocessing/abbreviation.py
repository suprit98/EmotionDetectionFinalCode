import re
import csv
import numpy as np
import pandas as pd
import nltk
from textblob import TextBlob
import ssl
import os
def translator(user_list):
    j = 0
    HOME_FOLDER = "./Abbreviation_data/"
    #fileName = "F:\EmotionDetection\Abbreviation_data\\formattedList.txt"
    fileName = os.path.join(HOME_FOLDER,"formattedList.txt")
    accessMode = "r"
    return_list = []
    for user_string in user_list:
        with open(fileName, accessMode) as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            user_string = re.sub('[^a-zA-Z0-9]', '', user_string)
            for row in dataFromFile:
                if user_string.upper() == row[0]:
                    user_string = row[1]
            myCSVfile.close()
        #print(user_string)
        return_list.append(user_string)
    #print(return_list)
    return return_list
