from flask import Flask
import time

app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"

@app.route('/ep1') 
def ep1(): # this is the home page function that generates the page code
    time.sleep(4)
    return "ep1"

   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it
