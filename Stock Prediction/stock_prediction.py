import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)  # to skip the first row which contains features name
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))  
			prices.append(float(row[1]))
	return

def predice_price(dates, prices, x):
	dates = np.reshape(dates, (len(dates), 1))

	# models
	svr_lin = SVR(kernel= 'linear', C=1e3)
	svr_poly = SVR(kernel= 'poly', C=1e3, degree = 2)
	svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

	# train the dataset
	svr_lin.fit(dates, prices)
	svr_poly.fit(dates, prices)
	svr_rbf.fit(dates, prices)

	# plot the data
	plt.scatter(dates, prices, color='black', label='Data')
	plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
	plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
	plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0]

get_data('aapl.csv')  # file downloaded from google finance

predicted_price = predice_price(dates, prices, 5) # date at which you want to predict the price

print(predicted_price)
	