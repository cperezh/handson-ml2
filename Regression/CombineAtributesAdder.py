from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
import numpy as np

class CombineAtributesAdder(BaseEstimator, TransformerMixin):
    
    latitude_ix, longitude_ix, total_rooms_ix, total_bedrooms_ix = 1, 0, 3, 4
    households_ix, population_ix, median_income =  6, 5, 7
    
    new_columns = ["latitude_longitud", "rooms_x_beds", "rooms_x_houses", "population_x_houses",
                   "population_x_rooms", "median_income_x_houses", "latitude_+_longitud_+_pulation"]
    
    def __init__(self,  only3=False):
        self.only3 = only3
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        latitude_longitud = X[:, type(self).latitude_ix] + X[:, type(self).longitude_ix]
        rooms_x_beds = X[:, type(self).total_rooms_ix] / X[:, type(self).total_bedrooms_ix]
        rooms_x_houses = X[:, type(self).total_rooms_ix] / X[:, type(self).households_ix]
        population_x_houses = X[:, type(self).population_ix] / X[:, type(self).households_ix]
        population_x_rooms = X[:, type(self).population_ix] / X[:, type(self).total_rooms_ix]
        median_income_x_houses = X[:, type(self).median_income] / X[:, type(self).households_ix]
        latitude_longitud_pulation = X[:, type(self).latitude_ix] + X[:, type(self).longitude_ix] 
        + X[:, type(self).population_ix]
        
            
        X = np.c_[X, latitude_longitud, rooms_x_beds, rooms_x_houses, population_x_houses,
                 population_x_rooms, median_income_x_houses, latitude_longitud_pulation]
        
        if (self.only3):
            X = X[:,[7, 8, 9]]
            
        return X

if __name__=="__main__":
    
    adder = CombineAtributesAdder()
    
    matrix = np.array([[1,2,3,4,5,6,7,8]])
    
    matrix_new = adder.fit_transform(matrix)
    
    print(matrix_new)
    