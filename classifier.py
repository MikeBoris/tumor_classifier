# based off 'More Program Development' chapter 
# from Practical Computing w/ Python...
#
# requires data from UC Irvine ML Repo:
# https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data
#
#
# TODO
# venv, install libraries
#
# import libaries
import pandas as pd

def make_training_set(file_name):
	"""
	Takes file_name (str)
	Returns training set list
	"""
	# open file
	file = open('breast_cancer_training.data', 'r')
	# initialize training_set list

	# for each line in the file
		# parse the line into its 11 components
		# create a tuple for the patients
		# append to the end of the training set list
	training_set = [tuple(line.split(',')) for line in file]
	file.close()
	# return the training_set list
	print(training_set[0][0])

	# pandas version
	df = pd.read_csv('breast_cancer_training.data', sep=',', header=None)



def train_classifier(training_data):
	return []

def make_test_set(file_name):
	return []

def classify_test_set_list(test_data, classifier):
	return []

def report_results(classified):
	print('Reported the results.')



def main():
	print('Loading training data...')
	training_file_name = 'breast_cancer_training.data'
	training_set_list = make_training_set(training_file_name)
	print('Done reading training data.\n')

	print('Training classifier...')
	classifier_list = train_classifier(training_set_list)
	print('Done training classifier.\n')

	print('Reading in test data...')
	test_file_name = 'breast_cancer_test.data'
	test_set_list = make_test_set(test_file_name)
	print('Done reading test data.\n')

	print('Classifying!')
	result_list = classify_test_set_list(test_set_list, classifier_list)
	print('Done classifying.\n')

	report_results(result_list)
	print('Program finished.')



def main2():

	# load data
	df = pd.read_csv('breast_cancer_training.data', sep=',', header=None)
	# df of data

	# '"classifier": a program that takes in a new example and
	# determines, based on previous examples it observed, what
	# "class" the new example belongs to.'
	#
	# 'There are many interesting internal models that a classifer
	# could use to predict the class label of a new example.'
	#
	# Approach:
	# Look at a tumor attribute for each individual,
	# then combine the observations on that attribute into a 
	# decision value used to classify an individual for that
	# particular attribute.
	# How to find decision values?
	# For each attribute, develop two averages.
	# First average will represent average value for benign tumors.
	# Second average will represent average value for malignant tumors.
	# After training on all nine, we should end up w/ 18 averages.
	#
	# Construct classifier as follows:
	# For each attribute:
	# 	find the midpoint between benign and malignant averages
	# 	this midpoint will be our decision value,
	# 	aka class separation value
	# The classifier will consist of 9 separation values

	benign = df[df[10] == 2]
	malignant = df[df[10] == 4]
	
	for i in range(1,10):
		x = 'a{}'.format(i)
		print(malignant[i].mean())



if __name__ == '__main__':
	main2()