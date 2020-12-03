import joblib

class Modelo():
    
    def __init__(self, nombre=None, modelo=None):
        self.nombre = nombre
        self.modelo = modelo
        
    def save(self):
        joblib.dump(self.modelo,self.nombre+".pkl")
        
    def load(self, nombre):
        self.nombre = nombre
        self.modelo = joblib.load(nombre+".pkl")