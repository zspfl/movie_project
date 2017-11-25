import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
from sklearn import datasets,linear_model

def get_data(filename):
    data = pd.read_csv(filename)
    X_parameter=[]
    Y_parameter = []
   # print data
  #  print zip(data['square_feet'],data['price'])
    for single_square_feet,single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
        pass
    return X_parameter,Y_parameter

print get_data("E:\\log\\input_data.csv")

def linear_model_main(X_parameters,Y_parameters,predict_value):
    #create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters,Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

def show_linear_line(X_parameters,Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color = 'blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color = 'red')
    #plt.xticks(())
    #plt.yticks(())
    plt.show()
    return

X,Y = get_data("E:\\log\\input_data.csv")
predictvalue = 700
result = linear_model_main(X,Y,predictvalue)
print X ,":", Y
show_linear_line(X,Y)
print result
