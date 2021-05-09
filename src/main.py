from flask import Flask
import pickle as pkl

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def predict_film():
    model = pkl.load(open(""))

if __name__=="__main__":
    print(hello_world())