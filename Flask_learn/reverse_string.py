from flask import Flask
import yaml

app = Flask(__name__)

@app.route('/')


@app.route('/<str>')
def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  

 
if __name__ == '__main__':
    app.debug = True
    reverse_string("atharav")
    app.run()