# -*- coding: utf-8 -*-
"""340W_parent_paper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uqNmojceSyMN8gL67jJJXfPGLeCd2icq
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-bright')

rating = pd.read_csv('/Users/utkarshsinha/Downloads/ratings.csv')
rating.head()

movie_names = pd.read_csv('/Users/utkarshsinha/Downloads/movies.csv') 
movie_names.head()

movie_data = pd.merge(rating, movie_names, on='movieId')
movie_data.head()

Trend=pd.DataFrame(movie_data.groupby ('title') ['rating'].mean ())
Trend ['total number of ratings'] = pd.DataFrame(movie_data.groupby ('title') ['rating'].count ())
Trend.head()

plt.Figure(figsize = (10, 4))
As=plt.barh (Trend['rating'].round(), Trend['total number of ratings'],color ='b')
plt.show ()

plt.Figure(figsize=(10,4))
As=plt.subplot()
As.bar(Trend.head(25).index, Trend['total number of ratings'].head(25), color='b')
As.set_xticklabels(Trend.index, rotation=40, fontsize='12',horizontalalignment="right")
As.set_title ("Total Number of reviews for each movie")
plt.show ()

movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head(50)