#encoding:utf8
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model

def get_data(filename):
    data = pd.read_csv(filename)
    flash_x_parameter = []
    flash_y_parameter = []
    arrow_x_parameter = []
    arrow_y_parameter = []
    for x1,y1,x2,y2 in zip(data['flash_episode_number'],data['flash_us_viewers'],data['arrow_episode_number'],data['arrow_us_viewers']):
        flash_x_parameter.append([float(x1)])
        flash_y_parameter.append(float(y1))
        arrow_x_parameter.append([float(x2)])
        arrow_y_parameter.append(float(y2))
    return flash_x_parameter,flash_y_parameter,arrow_x_parameter,arrow_y_parameter

def more_viewers(x1,y1,x2,y2):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1,y1)
    predicted_value1 = regr1.predict(9)
    print predicted_value1
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2,y2)
    predicted_value2 = regr2.predict(9)
    print predicted_value1 ,":", predicted_value2
    if predicted_value1 > predicted_value2:
        print "flash tv"
    else:
        print "arrow tv"

def show_viewers(x1,y1,x2,y2):
    regr1 = linear_model.LinearRegression()
    print x1,":",y1
    regr1.fit(x1,y1)
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2,y2)
    print "x=", x1, ":", regr1.predict(x1)
    plt.scatter(x1,y1,color = "blue",label="flash")
    plt.plot(x1, regr1.predict(x1), color='blue')
    plt.scatter(x2,y2,color = "red",label="arrow")
    plt.plot(x2, regr2.predict(x2), color='red')
    plt.legend()
    plt.show();
    return
x1,y1,x2,y2 = get_data("E:\log\movie.csv")

more_viewers(x1,y1,x2,y2)
show_viewers(x1,y1,x2,y2)

import  sklearn
print dir(sklearn)