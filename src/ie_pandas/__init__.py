
import numpy as np
#Defining the class and the type of input accepted = dictionary
class DataFrame:
    def __init__(self, data):
        if type(data) != dict:
            raise ValueError("DataFrame class accept only dictionaries")

        self.data = data