import re
import csv
import numpy as np
import pandas as pd
import nltk
from textblob import TextBlob
import ssl
import os
import string


def spell_corrector(words):
    '''tagged_text = nltk.tag.pos_tag(text.split())
    edited_tagged_text = [word for word,tag in tagged_text if tag!='NNP' and tag!='NNPS']
    edited_text = ' '.join(edited_tagged_text)
    #print(tagged_text)
    #Removing repeated characters to be done before expanding abbreviations
    new_edited_text = ""
    for word in edited_text.split():
        if len(word)>=2:
            new_word = word[0] + word[1]
            ct=2
            for i in range(2,len(word)):
                if not(word[i]==new_word[ct-1] and word[i]==new_word[ct-2]):
                    new_word=new_word + word[i]
                    ct=ct+1
        else:
            new_word = word
        new_edited_text = new_edited_text + " " + new_word
    new_edited_text = TextBlob(new_edited_text).correct()
    return new_edited_text'''
    corrected_word_list = []
    for word in words:
        if len(word)>=2:
            new_word = word[0] + word[1]
            ct=2
            for i in range(2,len(word)):
                if not(word[i]==new_word[ct-1] and word[i]==new_word[ct-2]):
                    new_word=new_word + word[i]
                    ct=ct+1
        else:
            new_word = word
        new_word = TextBlob(new_word).correct()
        corrected_word_list.append(str(new_word))
    #print(corrected_word_list)
    return corrected_word_list

