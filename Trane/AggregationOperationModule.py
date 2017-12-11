import pandas as pd
"""
Module functions:
These are the aggregation operations possible under the Aggregation Operation class.
Methods can be added here under 2 constraints.
1. Create a function with the dataframe as input and return a new dataframe.
2. Add the function to the dictionary of possible operations.
"""
def last(dataframe):
	df = dataframe.copy()
	return df.tail(n = 1)
def first(dataframe):
	df = dataframe.copy()
	return df.head(n = 1)
def last_minus_first(dataframe):
	df = dataframe.copy()
	last_row = last(df)
	first_row = first(df)
	new_df = pd.concat([first_row, last_row])
	return new_df.diff().dropna()
def count(dataframe):
	raise NotImplementedException
def sumup(dataframe):
	raise NotImplementedException

possible_operations = {
	"last" : last,
	"first": first,
	"last minus first" : last_minus_first,
	"count": count,
	"sum": sumup
}
