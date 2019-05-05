
import numpy as np
#Defining the class and the type of input accepted = dictionary
class DataFrame:
	def __init__(self, data):
		if type(data) != dict:
			raise ValueError("DataFrame class accept only dictionaries")

		self.data = data

	#Allowing to call columns using the keys of the diccionary and indexation. object["key"]
	def __getitem__(self, colname):   
		return np.array(self.data[colname])

	#The following code allows overwriting of the list using an indexing object["key"] = value
	def _setitem_(self, index, value):
			self.data[index] = value

	#The following code allows to get a specific row from the dataframe        
	def get_row(self, index):
		l = []
		for i in self.data.keys():
			l.append(self.data[i][index])
		return l
		
	def sum(self):
		# List to build with the summatory of each column
		l = []
		# Defining the types of objects that will be taken for the sum calculation
		p_num_types = [int, float, complex]
		np_num_types = [np.int_, np.float_, np.complex_]
		# Two methods are used in case each column (key) is a list or a np.arrays:
		# In case the column is a lists:
		for columns in self.data.keys():
			if type(self.data[columns]) == list:
				c = 0
				# If all values numeric, sum will be performed and added to the list.
				for values in self.data[columns]:
					if type(values) in p_num_types:
						c += 1
				if c == len(self.data[columns]):
					l.append(np.sum(self.data[columns]))
			# In case the columns is a np.array:
			else:
				c = 0
				for values in self.data[columns]:
					# We use now the list of accepted numeric types in np.arrays
					if values.dtype in np_num_types:
						c += 1
				if c == len(self.data[columns]):
					l.append(np.sum(self.data[columns]))

		return l

	def median(self):
		l=[]
		# Defining the types of objects that will be taken for the sum calculation
		p_num_types = [int, float, complex]
		np_num_types = [np.int_, np.float_, np.complex_]
		# Two methods are used in case each column (key) is a list or a np.arrays:
		# In case the column is a lists:
		for columns in self.data.keys():
			if type(self.data[columns]) == list:
				c = 0
				# If all values numeric, sum will be performed and added to the list.
				for values in self.data[columns]:
					if type(values) in p_num_types:
						c += 1
				if c == len(self.data[columns]):
					#Sort the columns to be able to find the median
					s = np.sort(self.data[columns])
					if len(self.data[columns]) % 2 != 0:
						#If not even lenght, return the middle sorted position
						l.append(s[round(len(s) / 2)])
					else:
						#If even lenght, return the mean of the 2 median values
						l.append((s[int(len(s) / 2)] + s[int(len(s) / 2) - 1]) / 2)
			#In case numpy arrays
			else:
				c = 0
				for values in self.data[columns]:
					# We use now the list of accepted numeric types in np.arrays
					if values.dtype in np_num_types:
						c += 1
				if c == len(self.data[columns]):
					#If all numeric, use of built numpy median
					l.append(np.median(self.data[columns]))
		return(l)

	def min(self):
                l=[]
                # Definition of object types used for the calculation of the sums as Integer, Float or Complex Number
                p_num_types = [int, float, complex]
                np_num_types = [np.int_, np.float_, np.complex_]
                
                # Different methods of finding the min will be used depending on wheter the columns is a list or a numpy array
                
                # CASE 1: The columns are lists:
                for columns in self.data.keys():
                            if type(self.data[columns]) == list:
                                c = 0
                                # If all values numeric, sum will be performed and added to the list.
                                for values in self.data[columns]:
                                    if type(values) in p_num_types:
                                        c += 1
                                        
                                if c == len(self.data[columns]):
                                # Sort the columns to be able to find the min
                                s = np.sort(self.data[columns])
                                l.append(s[0])
                        # CASE 2: The columns are numpy arrays
                         else:
                                c = 0
                                for values in self.data[columns]:
                                    # We use now the list of accepted numeric types in np.arrays
                                    if values.dtype in np_num_types:
                                        c += 1
                                if c == len(self.data[columns]):
                                    #If all numeric, use of built numpy min
                                    l.append(np.min(self.data[columns]))
        return l

	def max(self):
		l = []
		# Definition of object types used for the calculation of the sums as Integer, Float or Complex Number
		p_num_types = [int, float, complex]
		np_num_types = [np.int_, np.float_, np.complex_]

		# Different methods of finding the max will be used depending on wheter the columns is a list or a numpy array

		# CASE 1: The columns are lists:
		for columns in self.data.keys():
			if type(self.data[columns]) == list:
				c = 0
				# If given values are all numeric, sum will be performed and added to the list.
				for values in self.data[columns]:
					if type(values) in p_num_types:
						c += 1
				if c == len(self.data[columns]):
					# Sorting of columns is done to find the max at the end of the list
					s = np.sort(self.data[columns])
					l.append(s[len(s) - 1])
			# CASE 2: The columns are numpy arrays
			else:
				c = 0
				for values in self.data[columns]:
					# We use now the list of accepted numeric types in np.arrays
					if values.dtype in np_num_types:
						c += 1
				if c == len(self.data[columns]):
					# If all numeric, use of built np.max function
					l.append(np.max(self.data[columns]))
		return l
   
