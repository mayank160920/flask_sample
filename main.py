from flask import Flask
import time

app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"

@app.route('/ep1') 
def ep1(): # this is the home page function that generates the page code
    time.sleep(5)
    return "ep1"

@app.route('/ep2') 
def ep2(): # this is the home page function that generates the page code
    time.sleep(10)
    return "ep1"

@app.route('/ep3') 
def ep3(): # this is the home page function that generates the page code
    time.sleep(15)
    return "ep1"

@app.route('/ep4') 
def ep4(): # this is the home page function that generates the page code
    time.sleep(20)
    return "ep1"

@app.route('/ep5') 
def ep5(): # this is the home page function that generates the page code
    time.sleep(25)
    return "ep1"

@app.route('/ep6') 
def ep6(): # this is the home page function that generates the page code
    time.sleep(30)
    return "ep1"
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it
