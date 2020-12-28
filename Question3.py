#Question3
#MLP for Regression

from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd

x_train=pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 3/train_data.txt',sep='\t')
y_train=pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 3/train_truth.txt',sep='\t')
x_test=pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 3/test_data.txt',sep='\t')
L=len(x_test)
y_predicted=np.arange(L)

#Some parameters in the MLPRegressor function
#hidden_layer_sizes:the ith element represents the number of neurons in the ith hidden layer
#activation:activation function for the hidden layer
#tanh:the hyperbolic an function, returns f(x)=tanh(x)
#solver:the solver for weight optimization
#adam: a stochastic gradient-based optimizer

model=MLPRegressor(activation='tanh', alpha=1e-06,
       beta_1=0.9, beta_2=0.995, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4,4,4,4), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)
model.fit(x_train,y_train)

y_predicted=model.predict(x_test)

np.savetxt("C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 3/test_predicted.txt",y_predicted,fmt='%.18e',header='y',comments ='')