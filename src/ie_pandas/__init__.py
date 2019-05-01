
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
